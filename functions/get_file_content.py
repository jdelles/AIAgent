from pathlib import Path

MAX_CHARS = 10000 

def get_file_content(working_directory, file_path):
    try:
        base = Path(working_directory).resolve()
        target = (base / file_path).resolve()
        target.relative_to(base)
    except ValueError:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not target.is_file():
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with target.open("r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS + 1)  # Read 1 extra char to detect truncation
        if len(content) > MAX_CHARS:
            return content[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]'
        return content
    except Exception as e:
        return f"Error: {str(e)}"

