"""
Python dictionary 문제
"""

#1. 평균을 구하세요
score = {
    '수학':80,
    '국어':90,
    '음악':100
}

total_score = 0
for subject_score in score.values():
    total_score += subject_score
#print(total_score)
##avg_score = total_score / len(score)
##print(avg_score)

# a=score.get('수학')
# b=score.get('국어')
# c=score.get('음악')

# print(int((a+b+c)/3))

#print (score['수학'],['국어'],['음악'])
# for value in score.():s
#     print(key)

#2. 반 평균을 구하세요. -> 전체 평균
scores = {
    'a': {
        '수학':80,
        '국어':90,
        '음악':100
    },
    'b': {
        '수학':80,
        '국어':90,
        '음악':100
    } 
}

# print(idol['치즈']['임혜경'])

"""
total_score = 0
length = 0

for person_score in scores.values():
   for subject_score in person_score.values():
       total_score += subject_score
       length += 1

avg_score = total_score / length
"""


#print(avg_score)

#3. 도시별 최근 3일 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9]
}

#3-1. 도시별 최근 3일의 온도 평균은?
for name, temp in city.items():
    #name은 도시이름 temp에는 숫자

    average_temp = sum(temp) / len(temp)
    print(f'{name} : {average_temp}')

#3-2. 도시 중 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

#3-3. 서울은 영상 2도였던 적이 있나요?
print(2 in city['서울'])