#list function
lucky_number = [4,8,15,16,23,42]
friends = ['sami','afrida', 'jim']

friends2 = friends.copy()

print(friends2)

#tuples

coordinates = (4,5)

print(coordinates[0])

#funtion

def greeting(name, age) :
    print("Hello "+ name + ", your age is "+ age)
    
greeting('mike', '35')

#return statement

def cube(num):
    return num*num*num
    
print(cube(3))