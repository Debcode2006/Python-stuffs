def get_response(user_input):
    """
    Get chatbot response based on user input.
    Returns appropriate response from predefined rules.
    """
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Dictionary of predefined responses
    responses = {
        "hello": "Hi! Nice to meet you!",
        "hi": "Hello! How can I help you today?",
        "how are you": "I'm fine, thanks! How about you?",
        "how are you doing": "I'm doing great! Thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Bye! Take care!",
        "thanks": "You're welcome!",
        "thank you": "You're welcome! Is there anything else I can help you with?",
        "what is your name": "I'm ChatBot, nice to meet you!",
        "who are you": "I'm a simple rule-based chatbot created to help you!",
    }
    
    # Return response if input matches any key, otherwise return default message
    return responses.get(user_input, "I'm not sure how to respond to that. Try saying 'hello' or 'how are you'.")

def main():
    print("ChatBot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    print("ChatBot: What would you like to talk about?")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower().strip() in ['bye', 'goodbye']:
            print("ChatBot:", get_response(user_input))
            break
        
        # Get and print chatbot response
        response = get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
