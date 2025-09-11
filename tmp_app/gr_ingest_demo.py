import sys
from pathlib import Path
import gradio as gr

sys.path.append(str(Path(__file__).parent))
import gr_pg1_ingest
import gr_pg2_fail_events
import gr_pg3_fail_stats



with gr.Blocks() as demo:
    
    gr.Markdown("""
        ### Spector.AI ML Model Development Assistant
        """)
    gr_pg1_ingest.demo.render()
with demo.route("Failure Events"):
    gr_pg2_fail_events.demo.render()
with demo.route("Failure Groups"):
    gr_pg3_fail_stats.demo.render()


if __name__ == "__main__":
    demo.queue()
    demo.launch(server_name="0.0.0.0", allowed_paths=["/*"], server_port=8082)




