# Simple function to return chatbot answers
def get_bot_response(user_input):
    user_input = user_input.lower()

    if user_input == "hello" or user_input == "hi":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what is your name":
        return "I am a basic rule-based chatbot."
    elif user_input == "bye" or user_input == "goodbye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."


# Main program loop
print("=== Basic Chatbot ===")
print("Type 'bye' to exit\n")

while True:
    user_message = input("You: ")
    reply = get_bot_response(user_message)
    print("Bot:", reply)

    if user_message.lower() == "bye" or user_message.lower() == "goodbye":
        break