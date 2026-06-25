import os
import dotenv
from pathlib import Path

dotenv.load_dotenv()

# Get the workspace root (where .env is located)
WORKSPACE_ROOT = Path(__file__).resolve().parent

# Path configurations
_path =  "files/sample_texts"
SAMPLE_FILES_DIR = WORKSPACE_ROOT / os.getenv("SAMPLE_FILES_DIR",NotImplemented)
STOPWORDS_FILE = WORKSPACE_ROOT / os.getenv("STOPWORDS_FILE", "files/stopwords.txt")