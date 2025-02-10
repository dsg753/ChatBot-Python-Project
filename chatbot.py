import datetime
import requests
import os
from dotenv import load_dotenv
from responses import load_responses, save_responses, get_response

load_dotenv()

ABSTRACT_API_KEY = os.getenv("ABSTRACT_API_KEY")
TIMEZONE_API_KEY = os.getenv("TIMEZONE_API_KEY")

def get_location(ip_address):
    
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key={ABSTRACT_API_KEY}&ip_address={ip_address}"
    response = requests.get(url)
    print(response.status_code)
    print(response.content)
    if response.status_code == 200:
        return response.json()['city'] + ", " + response.json()['country']
    else:
        return None

def get_current_time(location):
    
    url = f"https://timezone.abstractapi.com/v1/current_time/?api_key={TIMEZONE_API_KEY}&location={location}"
    response = requests.get(url)
    print(response.status_code)
    print(response.content)
    if response.status_code == 200:
        return response.json()['datetime']
    else:
        return None

def greet_user():
    
    ip_address = requests.get("https://api64.ipify.org").text
    location = get_location(ip_address)
    if location:
        current_time = get_current_time(location)
        if current_time:
            current_hour = int(current_time.split(' ')[1].split(':')[0])
            if current_hour < 12:
                return "Good morning!"
            elif 12 <= current_hour < 18:
                return "Good afternoon!"
            else:
                return "Good evening!"
        else:
            return "Hello!"
    else:
        return "Hello!"

def chatbot():
    
    
    responses = load_responses()

    print("🤖 Chatbot: " + greet_user())
    print("🤖 Chatbot: How can I assist you today? (Type 'bye' to exit)")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break

        if user_input.lower() == "time":
            ip_address = requests.get("https://api64.ipify.org").text
            location = get_location(ip_address)
            if location:
                current_time = get_current_time(location)
                if current_time:
                    print(f"🤖 Chatbot: The current time in {location} is {current_time}")
                else:
                    print("🤖 Chatbot: Sorry, I couldn't fetch the current time.")
            else:
                print("🤖 Chatbot: Sorry, I couldn't fetch the location.")
            continue

        
        bot_response = get_response(user_input, responses)
        if bot_response:
            print(f"🤖 Chatbot: {bot_response}")
        else:
            print("🤖 Chatbot: I don't know how to respond to that. Can you teach me?")
            new_response = input("You: Please provide a response: ")
            responses[user_input.lower()] = new_response
            save_responses(responses)  
            print("🤖 Chatbot: Thanks! I’ll remember that for next time.")

if __name__ == "__main__":
    chatbot()