import json

# Path to the JSON file where responses are stored
RESPONSES_FILE = "responses.json"


# Load responses from the JSON file
def load_responses():
    try:
        with open(RESPONSES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Return default responses if the file doesn't exist
        return {
            "hi": "Hello! How can I help you today?",
            "hello": "Hi there! What can I do for you?",
            "how are you": "I'm just a bot, but I'm here to help you!",
            "what is your name": "I am a chatbot created to assist you.",
            "bye": "Goodbye! Have a great day!"
        }


# Save responses to the JSON file
def save_responses(responses):
    with open(RESPONSES_FILE, "w") as file:
        json.dump(responses, file, indent=4)


# Get a response from the chatbot or ask the user to teach it
def get_response(user_input, responses):
    for key in responses:
        if key in user_input.lower():
            return responses[key]
    return None  # Return None if no response is found
