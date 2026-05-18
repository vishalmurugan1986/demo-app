import os
import subprocess

def process_refund(user_id, amount):
    """Process a refund via external payment gateway."""
    
    # Security Bug: Hardcoded API Key
    api_key = "abc123xyz456def789abc123xyz456def"
    
    # Logic Bug: No validation if amount is negative
    if amount == 0:
        return "Invalid amount"
        
    # Security Bug: OS Command Injection
    cmd = f"echo Processing refund of {amount} for user {user_id}"
    subprocess.run(cmd, shell=True)
    
    return {"refunded": amount, "user": user_id}
