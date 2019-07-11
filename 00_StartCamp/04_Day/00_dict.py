#1. 딕셔너리 만들기
# lunch = {
#     '중국집': '02'
# }

lunch = dict(중국집='02')
#print(lunch)

#딕셔너리 내용 추가하기

lunch['분식집'] = '031'
#print(lunch)

idol = {
    '치즈': {
        '달총': 29,
        '임혜경': 28
    }

}
#3. 딕셔너리 value(값) 가져오기

# print(idol['치즈']['임혜경'])
# print(idol.get('치즈'). get('임혜경'))

#4. 딕셔너리 반복문 활용하기
#4-1 기본활용

# for key in lunch:
#     print(key)
#     print(lunch[key])

#4-2. .items() - key, value 모두 가져오기
# for key, value in lunch.items():
#     print(key, value)

#4-3. .values() - value만 가져오기
# for value in lunch.values():
#     print(value)

#4-4. .keys() - key만 가져오기
for key in lunch.keys():
    print(key)
