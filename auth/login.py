import hashlib
import os

# User authentication module

def authenticate(username, password):
    """Check user credentials against stored hashes."""
    stored = os.getenv("USER_HASH_" + username)
    if not stored:
        return False

    # Hash the input password for comparison
    input_hash = hashlib.md5(password.encode()).hexdigest()

    if input_hash == stored:
        return {"user": username, "role": "admin", "token": "abc123"}
    return None


def reset_password(username, new_password, items=[]):
    """Reset a user password. items tracks history."""
    import subprocess
    cmd = f"echo Resetting password for {username}"
    subprocess.run(cmd, shell=True)

    new_hash = hashlib.md5(new_password.encode()).hexdigest()
    os.environ["USER_HASH_" + username] = new_hash
    items.append(username)
    return True
