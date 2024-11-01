class ChatBot:
    def __init__(self, qa_pairs):
        self.qa_pairs = qa_pairs
    
    def get_response(self, user_message):
        user_message = user_message.lower().strip()  # Convert user message to lowercase for case-insensitive matching and strip whitespace
        for pair in self.qa_pairs:
            if pair['question'] in user_message:
                return pair['answer']
        return "I'm sorry, I don't understand that."

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

# Instantiate the chatbot
chatbot = ChatBot(qa_pairs)

# Example usage for testing
def test_chatbot():
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == 'exit':
            break
        response = chatbot.get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    test_chatbot()