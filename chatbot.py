import random
from datetime import datetime


greetings = [ 
    "Hey there! I'm Jas_Bot.",
    "Hello! Jas_Bot at your service.",
    "Hi! I'm your friendly chatbot Jas_Bot.",
    "Greetings! Jas_Bot is online."
]


responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! How can I assist you?",
    "how are you": "I'm running smoothly—thanks for asking. How about you?",
    "bye": "Goodbye! Have a great day.",
    "thanks": "You're welcome!",
    "who are you": "I'm Jas_Bot—your simple rule‑based chatbot assistant.",
    "good morning": "Good morning! Hope your day starts great.",
    "good evening": "Good evening! How was your day?",
    "good night": "Good night! Sleep well and take care.",
    "i am fine": "Good to hear that!",
    "i'm fine": "Good to hear that!",
    "fine": "Good to hear that!",
    "good": "Good to hear that!", 
    "what is your name" :"Myself Jas_Bot your chatbot ",
    "what is the weather today": "it is good you can go for any work",
    "what are you upto these days":"Nothing great just answering your queries",
    "nice to talk to you":"I am glad to have a conversation with you ",
    "see you soon":"sure anytime at your service"
}


personal_questions = [
    "what is your favourite color",
    "what do you have any hobbies",
    "do you have feelings",
    "what do you know about the world",
    "do you have emotions"
]

def get_response(user_input: str) -> str:
    user_input = user_input.lower()

    
    for keyword in personal_questions:
        if keyword in user_input:
            return "I'm just a chatbot, I don't possess personal traits or emotions."

    
    for key in responses:
        if key in user_input:
            return responses[key]

    return "Sorry, I didn't understand that. Could you rephrase?"

def log_conversation(user_msg: str, bot_reply: str) -> None:
    """Append the conversation to chat_log.txt with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("chat_log.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] You: {user_msg}\n")
        file.write(f"[{timestamp}] Jas_Bot: {bot_reply}\n\n")

def jas_bot() -> None:
    print(random.choice(greetings))
    print("Type 'bye' at any time to exit.\n")

    while True:
        user_input = input("You: ")
        bot_reply = get_response(user_input)
        print("Jas_Bot:", bot_reply)
        log_conversation(user_input, bot_reply)

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    jas_bot()
