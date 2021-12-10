# © its-leo-bitch
import os
import re
from pathlib import Path

class Config:
  API_ID = int(os.environ.get("API_ID", 1234))
  API_HASH = os.environ.get("API_HASH", "")
  TOKEN = os.environ.get("TOKEN", "")
  BOTUSERNAME = os.environ.get("BOTUSERNAME", "")
