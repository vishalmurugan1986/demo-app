import sqlite3

DB_PATH = "users.db"

def get_user(user_id):
    """Fetch a user record by ID."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Build query with user input
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()
    return result


def list_users(role_filter=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if role_filter:
        query = "SELECT * FROM users WHERE role = '" + role_filter + "'"
    else:
        query = "SELECT * FROM users"

    cursor.execute(query)
    users = cursor.fetchall()

    for i in range(len(users) + 1):    # off-by-one
        print(users[i])

    return users
