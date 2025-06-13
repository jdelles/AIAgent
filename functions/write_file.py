from pathlib import Path

def write_file(working_directory, file_path, content):
    try:
        base = Path(working_directory).resolve()
        if file_path is None:
            target = base
        else:
            target = (base / file_path).resolve()
        try:
            target.relative_to(base)
        except ValueError:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        target.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            target.write_text(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        except Exception as e:
            return f'Error: Failed to write to file: {str(e)}'
            
    except Exception as e:
        return f'Error: {str(e)}'
        