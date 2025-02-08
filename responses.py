responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "what is your name": "I am a chatbot created to assist you.",
    "bye": "Goodbye! Have a great day!"
}


def get_response(user_input):


    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return "I'm sorry, I don't understand that."
