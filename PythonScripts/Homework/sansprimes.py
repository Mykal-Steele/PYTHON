def fuc_is_prime(unchecked: list[int]) -> tuple[list[int], list[bool]]:
    # Function to check prime numbers in a list and return the list of unchecked numbers and their prime status
    
    nextCheck = False  # Set initial flag for next check
    index = 0  # Initialize index
    bool_list = []  # Initialize list to store prime status
    print("\n------------------------------------------------")
    for i in unchecked.copy():
        # Iterate over unchecked numbers
        num = int(i)  # Convert to integer
        is_prime = True  # Assume prime initially
        if num <= 2:
            is_prime = False  # Numbers less than or equal to 2 are not prime
        else:
            for j in range(2, int(num**0.5) + 1):
                if num % j == 0:
                    is_prime = False  # If divisible, not prime
                    break
        if is_prime:
            print(f"{i} is a prime number! ✅")  # Print prime number
            i = True
            bool_list.append(i)  # Add prime status to list
            nextCheck = True  # Set flag for next check
            del unchecked[index]  # Remove from unchecked list
        else:
            if nextCheck:
                print(f"{i} is NOT a prime number. ❌")  # Print non-prime number
                del unchecked[index]  # Remove from unchecked list
                nextCheck = False  # Reset flag
            else:
                print(f"{i} is NOT a prime number. ❌")  # Print non-prime number
                index += 1  # Move to next index
            i = False
            bool_list.append(i)  # Add prime status to list
    print("------------------------------------------------")
    return unchecked, bool_list  # Return remaining unchecked numbers and prime status

def collect_Input():
    # Function to collect user input
    input_has_finished = False  # Set flag for input completion
    unchecked = []  # Initialize list for unchecked numbers
    while not input_has_finished:
        if not unchecked:
            isItPrime = input("- Type as many numbers as you want to check for prime\n\n**Type 'DONE' when you are finished**\nType... ")  # Prompt for input
        else:
            print("\n------------------------------------------------\nYou have chosen these numbers: ", unchecked)  # Show chosen numbers
            isItPrime = input("------------------------------------------------\n\n- Type your next number.\n\n- **Type 'DONE' when you are finished**\nType... ")  # Prompt for next number
        
        if isItPrime.lower() == 'done':
            input_has_finished = True  # Finish input
        else:
            try:
                unchecked.append(int(isItPrime))  # Add input to unchecked list if it can be converted to an integer
            except ValueError:
                print(f"\n❌ Error: '{isItPrime}' is not a valid number. Please enter a valid number or 'DONE' to finish.")  # Error message
    
    return unchecked  # Return unchecked numbers

unchecked = collect_Input()  # Collect user input
x, y = fuc_is_prime(unchecked)  # Check for prime numbers

print("\nSubtask I: ", x)
print("Subtask II:", y)
