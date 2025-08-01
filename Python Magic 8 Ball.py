import random  # This allows us to pick random items from a list

# Default list of Magic 8-Ball responses
responses = [
    "Yes", 
    "No", 
    "Maybe", 
    "Ask again later", 
    "Definitely", 
    "Absolutely not", 
    "It is certain", 
    "Very doubtful"
]

# Greet the user
print(" Welcome to the Magic 8-Ball!")
print("You can ask any YES or NO question.")
print("Type 'quit' to exit the program.")

# Ask the user if they want to add custom responses
add_custom = input("Would you like to add your own custom responses? (yes/no): ").strip().lower()

# If user wants to add responses
if add_custom == 'yes':
    while True:
        new_response = input("Enter your custom response (or type 'done' to finish): ").strip()
        if new_response.lower() == 'done':
            break
        # Add the custom response to the list
        responses.append(new_response)
        print(f"Added: '{new_response}'")

# Start the question loop
while True:
    question = input("\nAsk your yes/no question: ").strip()
    
    # Exit the program if user types 'quit'
    if question.lower() == 'quit':
        print("Goodbye! Thanks for using the Magic 8-Ball. ")
        break

    # Check if the user actually typed a question
    if question == "":
        print("Please ask a question!")
        continue

    # Choose a random response
    answer = random.choice(responses)
    print(" Magic 8-Ball says:", answer)
    