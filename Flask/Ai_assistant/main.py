from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from openai import OpenAI


app = Flask(__name__)


load_dotenv()

api_key = os.getenv("GROQ_API_KEY")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    print("1. Request received")

    question = request.form.get("question")

    print("2. Question:", question)
    print("3. Sending request to API...")

    # question = request.form.get("question")

    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "system",
                "content": "Help like a personal assistant."
            },
            {
                "role": "user",
                "content": question
            }
        ],

        temperature=0.7,

        max_tokens=512
    )

    answer = response.choices[0].message.content.strip()

    return jsonify({
        'response': answer
    }), 200


@app.route('/summarize')
def summarize():

    return ""


if __name__ == '__main__':
    app.run(debug=True)