print(7%3)
# numbers = [1, 2, 3, 4, 5, 6, 7]
numbers = range(1,7)
for number in numbers:
    print(number)

if 1 % 2 == 1:
    print("홀수!")
if 2 % 2 == 0:
    print("짝수!")
print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
for number in numbers:
    if number % 2 == 1:
        print(number, " 홀수입니다.")
    else:
        print(number, " 짝수입니다.")