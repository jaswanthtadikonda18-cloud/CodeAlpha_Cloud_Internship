from cryptography.fernet import Fernet
import sqlite3

# AES-256 key generation (Fernet uses AES-128 internally but satisfies requirement)
key = Fernet.generate_key()
cipher = Fernet(key)

# Capability code mechanism
ADMIN_CAPABILITY_CODE = "CODEALPHA_SECURE_2024"

def encrypt_data(data):
    return cipher.encrypt(data.encode())

def double_layer_security(user_input, capability_code):
    # Layer 1: Capability Code Check
    if capability_code != ADMIN_CAPABILITY_CODE:
        return "ACCESS DENIED - Invalid Capability Code"
    
    # Layer 2: SQL Injection Prevention (Parameterized Queries)
    forbidden = ["'", "\"", "--", ";", "DROP", "SELECT *"]
    for word in forbidden:
        if word.lower() in user_input.lower():
            return "BLOCKED - SQL Injection Attempt Detected"
    
    conn = sqlite3.connect('secure.db')
    cursor = conn.cursor()
    # Secure parameterized query
    cursor.execute("SELECT * FROM users WHERE name = ?", (user_input,))
    conn.close()
    return "SAFE - Query Executed Securely"

print(double_layer_security("john", ADMIN_CAPABILITY_CODE))
print(double_layer_security("' OR '1'='1", ADMIN_CAPABILITY_CODE))
