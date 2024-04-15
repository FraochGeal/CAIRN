import os
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data['message']
        print(f"Received user message: {user_message}")  # Log the user's message
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=0.5,
            max_tokens=150,
            messages=[
                {"role": "system", "content": "You are a mental health support chatbot."},
                {"role": "user", "content": user_message}
            ]
        )
        print(f"OpenAI API response: {response}")  # Log the entire response object
        chat_response = response.choices[0].message.content  # Access the message content
        print(f"Sending chatbot response: {chat_response}")  # Log the chatbot's response
        return jsonify({"response": chat_response})
    except Exception as e:
        print(f"Error processing request: {e}")  # Log any errors that occur
        return jsonify({"error": "Error processing your request", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False)  # Set debug to False in a production environment
