from dotenv import load_dotenv
import os
load_dotenv(override=True)

STREAM_PATH = os.getenv("SHELVES_STORAGE_SPACE")

print(f'{STREAM_PATH=}')
if not STREAM_PATH:
    raise RuntimeError(
        "Configuration Error: 'DOCUMENTS_PATH' is missing from the environment. "
        "Make sure your .env file is loaded properly."
    )

print(f"Loading streams from: {STREAM_PATH}")