import random
print('hello world')
print(1 + 1)
print(True)
students = ['markus', 'alex', 'tom', 'peter']
print(students)
print(random.choice(students))
good = "bye"
print(good)
print(list(good))
변수 = "한글도 되나요?"
print(변수)
print(list(변수))
print("신기하네요")
print(random.choice(list(변수)))
print('hallo\ng     uten\ntag')

my_name = 'My name is %s' % 'seokbum hong'
print(my_name)

myname2 = 'My name is {}'.format('Markus')
print(myname2)

print('{} x {} = {}'.format(7, 8, 7*8))
print('{1} x {0} = {2}'.format(7, 8, 7*8))

print('{3}, {2}, {0}, {1}'.format('a','b','c','d'))