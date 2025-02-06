import random
import datetime


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


def greet_user():
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


def chatbot():
    print("🤖 Chatbot: " + greet_user())
    print("🤖 Chatbot: How can I assist you today? (Type 'bye' to exit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        print("🤖 Chatbot:", get_response(user_input))


if __name__ == "__main__":
    chatbot()
