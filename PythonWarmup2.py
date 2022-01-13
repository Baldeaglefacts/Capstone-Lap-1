print('How many classes are you taking this semester?')
class_amount = int(input())
class_list = []
for x in range(class_amount):
    print('Enter the name of class ' + str(x+1))
    class_list.append(input())

for c in class_list:
    print(c)
