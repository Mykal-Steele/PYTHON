def list_benifits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

def build_sentence(info):
    for list in info:
            print(list, " is a benefit of functions!")

x = list_benifits()
build_sentence(x)