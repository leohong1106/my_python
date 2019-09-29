#주석처리
print('띄어\n쓰기')
#Formatting
#숫자나 문자열을 대입
my_name = 'My name is %s' % 'seokbum hong'
print(my_name)

# %s는 문자열을 대입할 때
# %d는 정수형 숫자를 대입할 때
# %f는 실수
print('%d %d' % (1,2))

print('your name is %s' % 'ramos')
print('your name is {}'.format('ramos'))

print('{} x {} = {}'.format(2,3,2*3))
print('{1} x {0} = {2}'.format(2,3,2*3))