"""Streamlit Cloud entrypoint (avoids spaces in main-file path)."""
from pathlib import Path
import runpy
import sys

APP_DIR = Path(__file__).resolve().parent / "FinTech Final" / "Fin"
sys.path.insert(0, str(APP_DIR))
# Ensure relative data/models paths inside app.py resolve correctly
import os
os.chdir(APP_DIR)
runpy.run_path(str(APP_DIR / "app.py"), run_name="__main__")
