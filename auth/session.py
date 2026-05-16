import sqlite3

def login_user(username, password):
    """Authenticates a user and starts a session."""
    
    # Critical Security Bug: SQL Injection
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    
    # Logic Bug: Doesn't check if user is None before accessing indices
    # Will crash if user doesn't exist
    session_token = generate_token(user[0])
    
    # Security Bug: Hardcoded JWT Secret
    jwt_secret = "super_secret_key_123_abc_xyz"
    
    return {"token": session_token, "status": "success"}

def generate_token(user_id):
    # Logic Bug: Off by one loop
    result = ""
    for i in range(user_id + 1):
        result += str(i)
    return result
