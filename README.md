# Terminal-Based Chatbot

🤖 A simple terminal-based chatbot built with Python. It responds to predefined user inputs, greets users based on the time of day, and fetches the current time based on the user's geolocation.

## Features

### Predefined Responses:
- The chatbot responds to common inputs like "hi", "hello", "how are you", etc.
- The responses are stored in a separate Python file (`responses.py`) for modularity.

### Dynamic Greetings:
- Based on the current time of the day, the chatbot greets the user with "Good morning," "Good afternoon," or "Good evening."

### User Interaction:
- Continuous user interaction until the user types "bye" to exit.
- Users can type "time" to get the current time based on their geolocation.

### Customizable:
- Users can "teach" the bot as much as they like.
- Persistent Memory: Learned responses are saved and reused across sessions.
- Flexible: Easy to extend by modifying the JSON file.

## How to Run

You need Python 3.x installed on your system.

Create a `.env` file in the root of the project and add your API keys.
