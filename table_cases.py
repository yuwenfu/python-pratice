#P33 3-1
name = ['python','linux','arm','avr','stm32']
print(name[0].title())
print(name[1].upper())
print(name[2].lower())
print(name[3])
print(name[4])
#P33 3-2
message = "My best friend is "+name[0].title()+'.'
print(message)
message = "My best friend is "+name[1].title()+'.'
print(message)
message = "My best friend is "+name[2].title()+'.'
print(message)
message = "My best friend is "+name[3].title()+'.'
print(message)
message = "My best friend is "+name[4].title()+'.'
print(message)
#P33 3-3
transportations = ['car','truck','bus','train','plane','bicycle','motorbike']
for transportation in transportations:
    message = "I would like to own a "+transportation
    print(message)
print("all over")
