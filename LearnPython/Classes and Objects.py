# define the Vehicle class
class Vehicle:
    def __init__(self, name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
        
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle("Fer", "convertible", "red", 60000.00)
car2 = Vehicle("Jump", "van", "blue", 10000.00)

# test code
print(car1.description())
print(car2.description())



#same code but shorter, the code dont use __init__
# #class Vehicle:
#   def final(self, name, type, color, value):
#
#        val = "car name is: %s, type is %s, color is %s, value is $%d" % (name, type, color, value)
#        return val

#car1 = Vehicle()
#car2 = Vehicle()
#print(car1.final("Fer", "convertible", "red", 60000.00))
#print(car2.final("Jump", "van", "blue", 10000.00))
