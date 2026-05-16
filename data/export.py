import os
import subprocess

def export_userData(user_id, format="csv"):
    """Exports user data to a specific format."""
    
    # Logic Bug: Using an undefined variable 'filename'
    file_path = f"/tmp/{filename}.{format}"
    
    # Security Bug: OS Command Injection via format
    cmd = f"db_export --user {user_id} --format {format}"
    subprocess.run(cmd, shell=True)
    
    return True
