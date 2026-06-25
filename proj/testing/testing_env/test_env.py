import os

# 1. Fetch the path from the environment variable
STREAM_PATH = os.getenv("DOCUMENTS_PATH")

print(f'{STREAM_PATH=}')
# 2. Safety check: Raise a clear error if the environment isn't set up right
if not STREAM_PATH:
    raise RuntimeError(
        "Configuration Error: 'DOCUMENTS_PATH' is missing from the environment. "
        "Make sure your .env file is loaded properly."
    )

# 3. Use STREAM_PATH safely in your code downstream
print(f"Loading streams from: {STREAM_PATH}")