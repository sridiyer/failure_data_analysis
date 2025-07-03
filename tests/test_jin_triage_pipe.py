import sys
from pathlib import Path
import asyncio
sys.path.append(str(Path(__file__).parent.parent))

from src.ext_pipe.triage_jinal_cobble_history import triage_jindal_delays_data





if __name__ == "__main__":
    out_df = asyncio.run(triage_jindal_delays_data())
    print(out_df.head())
    