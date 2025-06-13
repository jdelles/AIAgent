from pathlib import Path
import subprocess

def run_python_file(working_directory, file_path):
    try:
        base = Path(working_directory).resolve()
        target = (base / file_path).resolve()
        try:
            target.relative_to(base)
        except ValueError:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not target.exists():
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
    except Exception as e:
        return f"Error: {str(e)}"

    try:
        result = subprocess.run(
            ['python3', str(target)],
            capture_output=True,
            text=True,
            timeout=30,
            cwd=str(base)
        )
        
        output_parts = []

        if result.stdout:
            output_parts.append(f"STDOUT:\n{result.stdout.strip()}")
        if result.stderr:
            output_parts.append(f"STDERR:\n{result.stderr.strip()}")
        
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if len(result.stdout) == 0 and len(result.stderr) == 0:
            output_parts.append("No output produced.")
            
        return "\n".join(output_parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"
            
