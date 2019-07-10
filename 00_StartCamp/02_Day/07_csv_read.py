#csv 파일 read의 2가지 방법

#1. split
# with open('lunch.csv', 'r', encoding='utf-8') as f:
#     lines = f.readlines() #lines는 리스트형식
#     for line in lines:
#         print(line.strip().split(',')) #,를 기준으로 잘라서 리스트로 만들어줄게!



#2. csv reader
import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:
    lines = csv.reader(f)

    for line in lines:
        print(line)