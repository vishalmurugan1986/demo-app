import yaml
import pickle
import base64

def load_system_config(config_text):
    """Loads system configuration."""
    # Security Bug: Insecure YAML loading
    return yaml.load(config_text)

def debug_session(session_data_b64):
    """Debugs a raw session cookie."""
    # Security Bug: Insecure deserialization
    raw_bytes = base64.b64decode(session_data_b64)
    return pickle.loads(raw_bytes)

async def check_health():
    # Logic Bug: Calling async without await
    status = fetch_db_status() 
    if status == "ok":
        return True
    return False

async def fetch_db_status():
    return "ok"
