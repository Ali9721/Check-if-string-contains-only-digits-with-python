# Define "text" as a variable & gets string.
text = input("Please enter a string: ")

# Use "if" & "else" & "isdigit" 
if text.isdigit():
    # Output the result in this condition.
    print(f"{text} contains only digits.")
else:
    # Output the result in this condition.
    print(f"{text} does not contain only digits.")