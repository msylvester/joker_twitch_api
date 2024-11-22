import os

def load_tokens(file_path):
    """
    Reads tokens from a file and sets them as environment variables.

    Args:
        file_path (str): Path to the file containing tokens in KEY=VALUE format.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Token file not found: {file_path}")
    
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            try:
                key, value = line.split("=", 1)
                os.environ[key] = value
                # print(f"Set environment variable: {key}")
            except ValueError:
                print(f"Invalid line in token file: {line}")
