def list_benifits(): # storing the info in a func
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(info): # printing the stored info 'x' from the list one by one
    for list in info:
            print(list, " is a benefit of functions!")

x = list_benifits() # take the data return from the list_benifits func
build_sentence(x) # use the data x and put it as info into the func build_sentence