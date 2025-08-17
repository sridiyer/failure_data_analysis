import json
import os
from dotenv import load_dotenv
from google import genai
from google.genai.types import (
    FunctionDeclaration,
    GenerateContentConfig,
    GoogleSearch,
    HarmBlockThreshold,
    HarmCategory,
    Part,
    SafetySetting,
    Tool,
    ToolCodeExecution,
)

# Load environment variables
load_dotenv()

# safety filters etc: https://github.com/GoogleCloudPlatform/generative-ai/blob/main/gemini/getting-started/intro_gemini_2_5_pro.ipynb

MODEL_ID = "gemini-2.5-pro"    
GOOG_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOG_API_KEY:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

client = genai.Client(api_key=GOOG_API_KEY)
#chat_client = client.chats.create(model=MODEL_ID)

system_instruction = """
  You are an expert industrial engineer with expertise in analyzing
  industrial equipment and systems.
"""
gem_config=GenerateContentConfig(
        temperature=2.0,
        top_p=0.95,
        candidate_count=1,
    )

def extract_json_from_llm_output(llm_output_string: str) -> dict:
    """
    Extracts a JSON string embedded within an LLM output string,
    removes the typical ```JSON and ``` markers, and converts
    it into a Python dictionary.

    Args:
        llm_output_string: The raw string output from the LLM,
                           expected to contain a JSON block.

    Returns:
        A Python dictionary parsed from the extracted JSON string.

    Raises:
        ValueError: If the input string does not contain the expected
                    JSON markers or if the JSON is invalid.
        json.JSONDecodeError: If the extracted string is not valid JSON.
    """
    if not isinstance(llm_output_string, str):
        raise TypeError("Input must be a string.")

    lines = llm_output_string.strip().splitlines()

    if not lines:
        raise ValueError("Input string is empty.")

    # Check for and remove the ```JSON marker at the beginning
    if lines[0].strip().upper() == "```JSON":
        lines.pop(0)
    else:
        # If the first line isn't the marker, we assume the JSON starts there,
        # but we should still look for the end marker.
        # This handles cases where the marker might be missing.
        # However, for strict adherence to the problem description,
        # we could raise an error here if the marker is strictly expected.
        pass # Or raise ValueError("LLM output does not start with ```JSON") for stricter check


    # Check for and remove the ``` marker at the end
    if lines and lines[-1].strip() == "```":
        lines.pop(-1)
    else:
        # Similar to the start marker, handle cases where it might be missing.
        # For strict adherence, an error could be raised.
        pass # Or raise ValueError("LLM output does not end with ```") for stricter check

    if not lines:
        raise ValueError("No content found after removing markers.")

    # Join the remaining lines to form the JSON string
    json_string = "\n".join(lines)

    # Ensure the string looks like it could be JSON (starts with { or [ and ends with } or ])
    # This is a basic check, json.loads will do the thorough validation.
    stripped_json_string = json_string.strip()
    if not ((stripped_json_string.startswith('{') and stripped_json_string.endswith('}')) or \
            (stripped_json_string.startswith('[') and stripped_json_string.endswith(']'))):
        raise ValueError(f"Extracted string does not appear to be a valid JSON object or array: {stripped_json_string[:50]}...")


    try:
        # Convert the JSON string to a Python dictionary
        data_dict = json.loads(json_string)
        return data_dict
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Error decoding JSON: {e.msg}", e.doc, e.pos)

def invoke_gemini_for_extraction(prompt: str) -> dict:


    response = client.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=GenerateContentConfig(
        system_instruction=system_instruction,
        ),
    )

    out_dict = extract_json_from_llm_output(response.text)

    return out_dict

def get_gemini_response(prompt: str, session_type: str) -> str:
    global chat_client
    
    if session_type == "New Session":
        chat_client = client.chats.create(model=MODEL_ID,  history=[])

    response = chat_client.send_message(prompt)
    #print (f"gemini_response: {response.text}")
    return response.text

def get_gemini_response_session(chat_session, prompt: str) -> str:
    """Sends a prompt to a specific chat session and returns the text response."""
    print(f"\n>> Sending to session: {prompt}")
    try:
        response = chat_session.send_message(prompt)
        print(f"<< Received from session: {response.text}")
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"Error: {e}"


if __name__ == "__main__":
    prompt = "Describe the State of Texas"
    chat_response = get_gemini_response(prompt)
    print(chat_response)
    next_prompt = "What is its capital?"
    print(get_gemini_response(next_prompt))
    next_prompt = "What is its largest city?"
    print(get_gemini_response(next_prompt))
    next_prompt = "What is its population?"
    print(get_gemini_response(next_prompt))
    next_prompt = "What is its area?"
    print(get_gemini_response(next_prompt))