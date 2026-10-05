from flask import Flask, request, jsonify
from google import genai

app = Flask(__name__)
API_KEY = "AQ.Ab8RN6IMRECYROJzN5mUcNDd8jd8QOse3ocBlgf4eaIUQWW7UA"
client = genai.Client(api_key=API_KEY)

@app.route('/')
def home():
    return {"name": "Study AI", "status": "online"}

@app.route('/ask')
def ask():
    sawal = request.args.get('q', 'Hello')
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=sawal
        )
        jawab = response.text
    except Exception as e:
        jawab = f"Error: {e}"
    return jsonify({"sawal": sawal, "jawab": jawab})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
