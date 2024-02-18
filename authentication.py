from flask import session
import secrets 

def generate_secret_key():
    return secrets.token_urlsafe(16)

def generate_random_token():
    return secrets.token_urlsafe()

