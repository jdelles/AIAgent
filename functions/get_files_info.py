from pathlib import Path

def get_files_info(working_directory, directory=None):
    try:
        base = Path(working_directory).resolve()
        if directory is None:
            target = base
        else:
            target = (base / directory).resolve()
        try:
            target.relative_to(base)
        except ValueError:
            return f'Error: Cannot list "{directory}" as it is outside the working directory.'

        if not target.is_dir():
            return f'Error: "{directory} is not a directory'

        lines = []
        for item in sorted(target.iterdir(), key=lambda x: x.name):
            try:
                size = item.stat().st_size
                is_dir = item.is_dir()
                lines.append(f'- {item.name}: file_size={size} bytes, is_dir={is_dir}')
            except Exception as e:
                return f'Error: Failed to get info for "{item.name}": {str(e)}'

        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}" 

