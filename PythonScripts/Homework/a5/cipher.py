# This script defines a function 'enc' to encrypt a message using a key based on a specific algorithm,
# and prompts the user to input a message and a key to perform the encryption.

def enc(msg: str, key: int) -> str:
    
    encrypted = []
    encrypted.append(msg[0])
    n = 1
    x = 1

    while x-1 < key:
    
        n = x

        while n + key - 1 < len(msg): # Inner loop to append characters based on the key
            encrypted.append(msg[n + key - 1])  
            n += key
        
        encrypted.append(msg[x])
        x += 1  # Increment x to move through the message
  
    output = ''.join(encrypted[:-1])  # Join the encrypted characters into a single string, omitting the last character added unnecessarily
    return output  

def takeInput():

    msg = input("Enter message: ") 
    while True:
        key = int(input("Enter key: "))
        if key < len(msg):
            break
        else:
            print("Type a key smaller than the length of the message")

    return msg, key


msg, key = takeInput() 
result = enc(msg, key) 
print("Encrypted message:", result)  
