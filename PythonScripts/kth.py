
# This is a better, doesn't follow the special rule
# def kthDigit(x, b, k):
#     if k == 0: 
#         return x % b
#     else:
#         for i in range(k):  #The will divide the x(always base 10) by the base we want it to change, becasue we need the remainder of each value after devision (this is how we turn base 10 to base of anything)
#             x //= b
#         return x % b

# # Example usage:
# print(kthDigit(x = int(input("x = ")),b = int(input("base = ")),k = int(input("k = "))))


# i only used if statements here, but the code sucks


def kthDigit(x,b,k):
    if k == 0:
        output = x % b
        return int(output)
    elif k == 1:
        x = x/b
        output = x % b

        return int(output)
    elif k == 2:
        x = x/b
        x = x/b
        output = x% b
        return int(output)
    

result = kthDigit(x = int(input("x = ")),b = int(input("base = ")),k = int(input("k = ")))
print(result)
