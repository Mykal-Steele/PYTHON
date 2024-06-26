def allMultiplesOfK(k: int, lst: list[int]) -> bool:
    # Check if all elements in the list are multiples of k
    return all(i % k == 0 for i in lst)

lsts = []  # Initialize an empty list to store user input numbers
w = True  # Initialize a flag to control the outer loop

while True:  # Start an infinite loop
    
    if w == True:  # Check if it's the first iteration
        while True:  # Start an inner infinite 
            print("This will check if ALL the number you typed are the multiples of k")
            k = input("Type in the integer k: $")  # Prompt user to input k
            try:
                k = int(k)  # Try to convert k to an integer
                break  # If successful, exit the inner loop
            except ValueError:  # Handle non-integer input
                print("Please enter a valid number or 'Done' to stop.")
        i = input("You could type multiple numbers. \nType your first number for list 'lst' (or 'Done' to stop): $")  # Prompt user for the first list element
        w = False  # Set flag to False after first iteration
    else:
        i = input("Type your Next numbers (or 'Done' to stop): $")  # Prompt user for additional list elements

    if i.lower() == "done" or str(k).lower() == "done":  # Check if user wants to stop
        break  # Exit the outer loop
    try:
        lsts.append(int(i))  # Try to convert input to integer and add to list
    except ValueError:  # Handle non-integer input
        print("Please enter a valid number or 'Done' to stop.")

print(allMultiplesOfK(k, lsts))  # Check and print if all list elements are multiples of k
