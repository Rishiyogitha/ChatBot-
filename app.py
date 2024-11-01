from flask import Flask, request, jsonify, render_template
from Chatbot import ChatBot
from flask_ngrok import run_with_ngrok
app = Flask(__name__, template_folder='template')
run_with_ngrok(app)
# Example dataset
qa_pairs = [
    {"question": "hello", "answer": "Hi there! How can I help you today?"},
    {"question": "how are you", "answer": "I'm just a bot, but I'm doing great! How can I assist you?"},
    {"question": "what is your name", "answer": "I'm a universal chatbot. What's your name?"},
     {"question": "rishi", "answer": "Great Name. How can i assist you today?"},
    {"question": "tell me a joke", "answer": "Why don't scientists trust atoms?"},
    {"question": "why", "answer": "Because they make up everything"},
    {"question": "what can you do", "answer": "I can help answer your questions and provide information. What would you like to know?"},
    {"question": "who created you", "answer": "I was created by a team of developers. How can I assist you today?"},
    {"question": "goodbye", "answer": "Goodbye! Have a great day!"},
    {"question": "help", "answer": "Sure, I'm here to help! What do you need assistance with?"},
    {"question": "what is the weather today", "answer": "I'm not sure about the weather right now, but you can check a weather website for up-to-date information."}
]

chatbot = ChatBot(qa_pairs)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chatbot', methods=['POST'])
def chatbot_api():
    data = request.json
    message = data.get('message')
    response = chatbot.get_response(message)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run()


