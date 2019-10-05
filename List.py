print('안녕', end = '하세요'); print('한줄로 쓰기')
# immutable  값을 변경할 수 없음(문자열)
# mutable    값을 변경할 수 있음(List)
# like [val2, val2, ..]

my_list = []
print(my_list)
print(type(my_list))
#마이리스트는 리스트 타입 자료형이다.
my_list = [1, 2, 3]
print(my_list)
my_list.append(4)
print(my_list)