import datetime
from responses import load_responses, save_responses, get_response


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
    Chatbot with learning mode: remembers new responses provided by the user.
    """
    # Load existing responses
    responses = load_responses()

    print("🤖 Chatbot: " + greet_user())
    print("🤖 Chatbot: How can I assist you today? (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break

        # Get a response or enter learning mode if unknown
        bot_response = get_response(user_input, responses)
        if bot_response:
            print(f"🤖 Chatbot: {bot_response}")
        else:
            print("🤖 Chatbot: I don't know how to respond to that. Can you teach me?")
            new_response = input("You: Please provide a response: ")
            responses[user_input.lower()] = new_response
            save_responses(responses)  # Save the new response
            print("🤖 Chatbot: Thanks! I’ll remember that for next time.")


if __name__ == "__main__":
    chatbot()
