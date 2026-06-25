print("Welcome to Vaishnavi's Smart Chatbot")
print("Type 'bye' to exit")

name = input("What is your name? ")

print("Hello", name)

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I am fine!")

    elif user == "what is your name":
        print("Bot: My name is SmartBot.")

    elif user == "who created you":
        print("Bot: Vaishnavi created me.")

    elif user == "what is python":
        print("Bot: Python is a programming language.")

    elif user == "ai":
        print("Bot: AI means Artificial Intelligence.")

    elif user == "bye":
        print("Bot: Goodbye", name)
        break

    else:
        print("Bot: Sorry, I don't understand.")
