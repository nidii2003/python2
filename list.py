def get_user_input_list():
    # Initialize an empty list to store user inputs
    values = []

    while True:
        # Prompt the user to enter a value
        user_input = input("Enter a value: ")

        # Check if the user pressed enter without typing anything
        if user_input == "":
            break

        # Add the input value to the list
        values.append(user_input)

    # Print the final list
    print("Here's the list:", values)

# Call the function to run the program
get_user_input_list()
