
'''try:
    number = int(input('Enter a number: '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print('Invalid input')
    
    
#Reading from external files



employee_file = open('Kona.txt', 'r')
for employee in employee_file.readlines():
    print(employee)

employee_file.close()

'''
#w(over write) new file and apppend in existing files

employee_file = open('index.html', 'w')

employee_file.write('<p> this is html</p>')

employee_file.close()
