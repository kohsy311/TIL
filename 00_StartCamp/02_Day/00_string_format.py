#1. pyformat

#name='홍길동'
#eng_name='hong'

#print("안녕하세요, {}입니다. My name is {}".format(name, eng_name))
#print("안녕하세요, {1}입니다. My name is {0}".format(name, eng_name)) # 1번이 영어이름 0번이 이름이니까
#print("안녕하세요, {1}입니다. My name is {1}".format(name, eng_name))

#2. f-strings

#name='홍길동'
#print(f'안녕하세요,{name}입니다.')
#print('안녕하세요,',name,'입니다.')

import random

# menu=['김천', '스벅', '부찌']
# lunch=random.choice(menu)
# print('오늘의 점심은 {}입니다'.format(lunch))
# print(f'오늘의 점심은 {lunch}입니다.')

numbers = list(range(1, 46))
lotto = random.sample(numbers, 6)
print(f'오늘의 행운 번호는 {sorted(lotto)}입니다.')