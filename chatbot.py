import datetime
from responses import get_response  # Importing the response logic from responses.py


def greet_user():
    """
    Provides a greeting based on the time of day.
    """
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


def chatbot():
    """
    Main chatbot function to handle user interactions.
    """
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
