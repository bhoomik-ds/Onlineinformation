#!/usr/bin/env python3
"""
Django Secret Key Generator
Run this script to generate a new secret key for your Django project.
Usage: python generate_secret_key.py
"""

from django.core.management.utils import get_random_secret_key

def generate_secret_key():
    """Generate a new Django secret key."""
    secret_key = get_random_secret_key()
    print("=" * 80)
    print("Django Secret Key Generator")
    print("=" * 80)
    print(f"\nYour new secret key is:\n{secret_key}")
    print("\n" + "=" * 80)
    print("IMPORTANT:")
    print("- Keep this secret key safe and secure")
    print("- Never share it publicly or commit it to version control")
    print("- Use this as the value for SECRET_KEY environment variable")
    print("- For Vercel: Add this to your project's environment variables")
    print("=" * 80)
    
    return secret_key

if __name__ == "__main__":
    generate_secret_key()
