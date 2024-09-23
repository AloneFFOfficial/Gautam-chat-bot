# Function to process user input and provide predefined responses
def process_input(user_input):
    # Normalize the input to avoid case-sensitivity
    user_input = user_input.lower()
    
    # Predefined responses using if-else
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm a chatbot, I'm always good. How about you?"
    elif "what is your name" in user_input:
        return "I'm your assistant chatbot."
    elif "what can you do" in user_input:
        return "I can answer simple questions and assist you with predefined queries."
    elif "tell me a joke" in user_input:
        return "Why don’t scientists trust atoms? Because they make up everything!"
    elif "who created you" in user_input:
        return "I was created by a developer to assist with technical queries."
    elif "what is ai" in user_input:
        return "AI stands for Artificial Intelligence, the simulation of human intelligence in machines."
    elif "what is python" in user_input:
        return "Python is a popular programming language known for its simplicity and versatility."
    elif "what is your favorite color" in user_input:
        return "I don't have preferences, but I've heard blue is calming!"
    elif "what is the time" in user_input:
        return "Sorry, I can't tell time. You can check your device for that!"
    elif "goodbye" in user_input or "bye" in user_input:
        return "Goodbye! Have a great day ahead!"
    elif "exit" in user_input:
        return "exit"  # Return 'exit' to break the loop.
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop to interact with the user
def chatbot():
    print("Chatbot: Hello! Ask me anything or type 'exit' to quit.")
    
    while True:
        user_input = input("You: ")
        response = process_input(user_input)
        
        if response == "exit":
            print("Chatbot: Exiting... Goodbye!")
            break
        else:
            print("Chatbot:", response)

# Run the chatbot
chatbot()