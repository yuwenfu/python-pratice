#P38 3-4
attenders = []
attenders.append('TOM')
attenders.append('Jack')
attenders.append('Jimmy')
for attender in attenders:
    print("Hi "+attender+","+"would you like to attend my party?")
#P38 3-5
print("Jimmy"+" can not attend the party .")
attenders.remove('Jimmy')
attenders.append("BOM")
for attender in attenders:
    print("Hi "+attender+","+"would you like to attend my party?")
print('\n')
#P38 3-6
message = "I can find a bigger table !"
print (message)
attenders.insert(0,'Lucy')
attenders.insert(2,'Uber')
attenders.insert(5,'Python')
for attender in attenders:
    print("Hi "+attender+","+"would you like to attend my party?")
print('\n')
#P39 3-7
print("Because the place is limited. I can invite two pesrson only.\n")
attender = attenders.pop()
print("sorry "+attender+",I could not invite you to enjoy the party.Because the party is very limit .")
attender = attenders.pop()
print("sorry "+attender+",I could not invite you to enjoy the party.Because the party is very limit .")
attender = attenders.pop()
print("sorry "+attender+",I could not invite you to enjoy the party.Because the party is very limit .")
attender = attenders.pop()
print("sorry "+attender+",I could not invite you to enjoy the party.Because the party is very limit .")
for attender in attenders:
    print("Hi "+attender+","+"would you like to attend my party?")
del attenders[1]
del attenders[0]
print(attenders)
print(attenders)
