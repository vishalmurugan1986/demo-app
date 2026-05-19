import sqlite3
import hashlib
import os

def authenticate_user(username, password):
    """Authenticate user with database."""
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Critical Security Bug: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    
    user = cursor.fetchone()
    
    # Logic Bug: Forgot to close database connection
    # conn.close()
    
    if user:
        return {"status": "success", "username": username}
    return {"status": "failed"}

def reset_password(username, new_password, history=[]):
    """Reset user password and track history."""
    # Logic Bug: Mutable default argument history=[]
    history.append(new_password)
    
    # Security Bug: Insecure MD5 hashing
    hashed = hashlib.md5(new_password.encode()).hexdigest()
    
    print(f"Password reset for {username}")
    return True
