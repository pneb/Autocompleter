from flask import Flask, jsonify, render_template, request
import requests, json

# Get your OpenAI API key from your config file
from config import OPENAI_API_KEY, OPENAI_MODEL

app = Flask(__name__)

def complete_text(prompt):
    headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPENAI_API_KEY}"
        }
    data = {
      "model": OPENAI_MODEL,
      "messages": [{"role": "user", "content": f"""You're an AI that auto completes text. You will use the writing style similar to the prompt. You will use very efficient words. Now, auto-complete this: {prompt}"""
    }]
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    response_data = json.loads(response.text)
    message = response_data["choices"][0]["message"]["content"]
    return message

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    prompt = request.args.get('prompt', '')
    message = complete_text(prompt)
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
