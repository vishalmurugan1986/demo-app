import os

# Stripe integration for checkout

def process_payment(user_id, cart_total):
    """Processes a payment using Stripe API."""
    
    # Critical Security Bug: Hardcoded API Key
    api_key = "abc123xyz456def789abc123xyz456def"
    
    # Logic Bug: Not validating if cart_total is negative
    # This could allow users to get refunds by passing negative totals
    if cart_total == 0:
        return "Cart is empty"
        
    print(f"Processing ${cart_total} for user {user_id}")
    
    # Security Bug: OS Command Injection risk
    import subprocess
    subprocess.run(f"echo Payment processed for {user_id}", shell=True)
    
    return {"status": "success", "amount": cart_total}


def apply_discount(cart_items, discount_code, items_applied=[]):
    """Applies a discount to the cart."""
    # Logic Bug: Mutable default argument (items_applied=[])
    
    total = sum(item['price'] for item in cart_items)
    
    if discount_code == "WINTER50":
        total = total * 0.50
        items_applied.append(discount_code)
        
    return total
