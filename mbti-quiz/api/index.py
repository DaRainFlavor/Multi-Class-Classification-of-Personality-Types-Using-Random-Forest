import os
import sys

# Add current directory to path so we can import app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

# This required for Vercel to detect the Flask app
# Vercel looks for a variable named 'app'
if __name__ == "__main__":
    app.run()
