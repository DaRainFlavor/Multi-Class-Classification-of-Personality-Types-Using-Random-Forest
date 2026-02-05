from app import app

# This required for Vercel to detect the Flask app
# Vercel looks for a variable named 'app'
if __name__ == "__main__":
    app.run()
