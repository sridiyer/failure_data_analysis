#from src.llms.prompts.jin_triage_tags_extraction import JINDAL_TRIAGE_TAGS_EXTRACTION_PROMPT
#from src.llms.prompts.jin_capa_data_prompt import JINDAL_CAPA_TAGS_EXTRACTION_PROMPT
from src.llms.prompts.jin_triage_delay_only import JINDAL_TRIAGE_TAGS_EXTRACTION_PROMPT
from src.llms.goog_gemini import invoke_gemini_for_extraction

def extract_jinal_cobble_history_triage_tags(notes1: str, notes2: str) -> dict:
    """
    Extract tags from notes1 and notes2.
    """
    
    prompt = JINDAL_TRIAGE_TAGS_EXTRACTION_PROMPT
    prompt = prompt.format(data_from_delay_desc_file=notes1, data_from_capa_file=notes2)
    try:
        response = invoke_gemini_for_extraction(prompt)
    except Exception as e:
        return e
        resp_text = prompt
    
    """
    final_string = TEST_STR.format(variable_1=ex_result1, variable_2=ex_result2)

    substitutions = {
        "variable_1": notes1,
        "variable_2": notes2
    }
    final_string_alt = TEST_STR.format_map(substitutions)

    """
    # invoke the LLM with the prompt.
    return response

def extract_jinal_capa_tags(capa_notes1: str) -> dict:
    """
    Extract tags from notes1 and notes2.
    """
    
    prompt = JINDAL_CAPA_TAGS_EXTRACTION_PROMPT
    prompt = prompt.format(data_from_capa_file=capa_notes1)
    try:
        response = invoke_gemini_for_extraction(prompt)
    except Exception as e:
        return e
        resp_text = prompt
    
    """
    final_string = TEST_STR.format(variable_1=ex_result1, variable_2=ex_result2)

    substitutions = {
        "variable_1": notes1,
        "variable_2": notes2
    }
    final_string_alt = TEST_STR.format_map(substitutions)

    """
    # invoke the LLM with the prompt.
    return response