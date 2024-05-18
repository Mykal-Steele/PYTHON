k = int(input("Your Secret Key is "))
M = str(((25*1502)**(257+123) + (98*34)**(981-813)))

b = M[k-1]
a = M[k-2]
output = int(a + b)
print("The secret code is", output)
