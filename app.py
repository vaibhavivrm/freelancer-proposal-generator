from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)

openai.api_key = "YOUR_REAL_API_KEY"


@app.route("/")
def home():
    return "Backend is running 🚀"


@app.route("/generate", methods=["POST"])
def generate():
    data = request.json

    prompt = f"""
    Write a professional freelance proposal:

    Project: {data.get('title')}
    Client: {data.get('client')}
    Description: {data.get('description')}
    Role: {data.get('role')}
    Budget: {data.get('budget')}
    Tone: {data.get('tone')}
    Length: {data.get('length')}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "proposal": response.choices[0].message.content
    })


if __name__ == "__main__":
    app.run(debug=True)