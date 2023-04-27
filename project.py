import random
from dictionary import dictionary

print("Welcome to the Serbian Language Learning Game!")

# Start the Serbian language learning game
def start_learning(difficulty, get_input=input) :
    # Initialize score and number of questions
    score = 0
    num_questions = 0
    # Determine the number of options based on the difficulty level
    if difficulty == '1' :
        num_options = 2
    elif difficulty == '2' :
        num_options = 3
    elif difficulty == '3' :
        num_options = 4
    else :
        num_options = 2

 # Ask questions until the user has answered 10
    while True :
        if num_questions == 10 :
            break
        # Choose a random word from the dictionary and get its translation
        word = random.choice(list(dictionary.keys()))
        translation = dictionary[word]
        # Generate a list of options, including the correct answer
        options = [translation]
        while len(options) < num_options :
            option = random.choice(list(dictionary.values()))
            if option not in options :
                options.append(option)
        # Shuffle the options and ask the user to select one
        random.shuffle(options)
        print(f"What is the translation of '{word}'?")
        for i, option in enumerate(options) :
            print(f"{i + 1}. {option}")
        guess = get_input("Enter the number of your answer: ")
        # Check if the user's input is valid and update the score and number of questions
        if guess.isdigit() and int(guess) in range(1, num_options + 1) :
            guess_index = int(guess) - 1
            if options[guess_index] == translation :
                print("Correct!")
                score += 1
            else :
                print(f"Incorrect. The correct translation is '{translation}'.")
            num_questions += 1
        else :
            print(f"Invalid input. Please enter a number between 1 and {num_options}.")

    # Display the final score and a message based on the user's performance
    print(f"You got {score} out of {num_questions} correct.")
    if score == 10 :
        print("Congratulations, you are fluent in Serbian!")
    else :
        print("Keep practicing to improve your skills.")


# Generate a random word from the dictionary
def generate_random_word() :
    return random.choice(list(dictionary.keys()))

# Get the translation of a word from the dictionary
def get_translation(word) :
    return dictionary[word]

# Get a list of options, including the correct answer, for a given translation
def get_options(translation, num_options) :
    options = [translation]
    while len(options) < num_options :
        option = random.choice(list(dictionary.values()))
        if option not in options :
            options.append(option)
    random.shuffle(options)
    return options

# Main function that runs the game
def main() :
    # Initialize score and number of questions
    score = 0
    num_questions = 0
    difficulty = input("Choose a difficulty level (1, 2, or 3): ")
    if difficulty == '1' :
        num_options = 2
    elif difficulty == '2' :
        num_options = 3
    elif difficulty == '3' :
        num_options = 4
    else :
        num_options = 2

    # Ask questions until the user has answered 10
    while num_questions < 10 :
        # Choose a random word from the dictionary and get its translation
        word = generate_random_word()
        translation = get_translation(word)
        options = get_options(translation, num_options)
        print(f"What is the translation of '{word}'?")
        for i, option in enumerate(options) :
            print(f"{i + 1}. {option}")
        guess = input("Enter the number of your answer: ")
        if guess.isdigit() and int(guess) in range(1, num_options + 1) :
            guess_index = int(guess) - 1
            if options[guess_index] == translation :
                print("Correct!")
                score += 1
            else :
                print(f"Incorrect. The correct translation is '{translation}'.")
            num_questions += 1
        else :
            print(f"Invalid input. Please enter a number between 1 and {num_options}.")

    print(f"You got {score} out of {num_questions} correct.")
    if score == 10 :
        print("Congratulations, you are fluent in Serbian!")
    else :
        print("Keep practicing to improve your skills.")


if __name__ == "__main__" :
    main()