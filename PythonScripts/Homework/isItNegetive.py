a = int(input())
b = int(input())
negative= input().lower() == 'true'
x = (((a <0 or b < 0) and negative== False) or (negative and (a <0 and b <0))) # True if a or b is negetive (AND) Negetive is False, [OR] , True if Negetive is True and both A and b is negetive
x = x == True

print(x)

