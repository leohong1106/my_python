animals = ['코알라', '하이에나', '다람쥐', '표범']
print(animals)
animals.append('스컹크')
animals.append('아나콘다')
print(animals)
print(animals[3])
del animals[1]
print(animals)
#추가/삭제 및 slicing도 가능
print(animals[2:4])

#가나다 순으로 정렬하기
animals.sort()
print(animals)

#animals.count로 셀 수도 있음.
