def chatbot():
    print("Chatbot: Hello! Type 'bye' to end the chat.")
    
    while True:
        user = input("You: ").lower()
        
        if "hello" in user:
            print("Chatbot: Hi there!")
        elif "how are you" in user:
            print("Chatbot: I'm fine, thanks!")
        elif "bye" in user:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
