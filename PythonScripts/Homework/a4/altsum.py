# (a4, Task_1)

def altsum(lst: list[int]) -> int:
    output = []
    next_neg = False
    first = False
    for i in lst:
        # this is just here to keep the first digit unchange, bc if first is postivie it could 1-2+2-6, when what we want is 1+2-2+6
        if first == False:
            output.append(i)
            first = True
        else:
            if next_neg == False:
                next_neg = True #the is to flag the text as 'change negetive'
                output.append(i)
            else:
                next_neg = False
                output.append(-i) # This is to 'negitify' the number lol
    print(output) # for error check
    return sum(output)

def ask_for_input():
    lst = [] # create a empty list for input stroage
    while True:
        i = input("Type a number (or 'Done' to stop): ")
        if i.lower() == "done":
            break
        try:
            lst.append(int(i))
        except ValueError:
            print("Please enter a valid number or 'Done' to stop.")
    return lst

lst = ask_for_input()
print(altsum(lst))

# output = 1 + 2 - 3 + 4 - 5 + 6 - ... so on