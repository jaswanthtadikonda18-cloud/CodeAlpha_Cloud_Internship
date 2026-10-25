# Retrieval-based AI Chatbot with predefined patterns

class CloudChatbot:
    def __init__(self):
        # Predefined input patterns for commercial use
        self.patterns = {
            "hello": "Hi! Welcome to CodeAlpha Cloud Support! How can I help?",
            "pricing": "Our cloud plans start from $9.99/month with scalability!",
            "booking": "You can book via our cloud portal - instant confirmation!",
            "help": "I can help with redundancy, SQL security, and cloud queries!",
            "bye": "Thanks for chatting! Visit again!"
        }
    
    def get_response(self, user_input):
        user_input = user_input.lower()
        for key in self.patterns:
            if key in user_input:
                return self.patterns[key]
        return "I am learning! Please ask about hello, pricing, booking, or help."

# For website integration (Flask)
from flask import Flask, request, jsonify
app = Flask(__name__)
bot = CloudChatbot()

@app.route('/chat', methods=['POST'])
def chat():
    msg = request.json.get('message')
    reply = bot.get_response(msg)
    return jsonify({"reply": reply}) # Instant response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000) # Accessible over internet
