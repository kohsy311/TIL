lunch = {
    '양자강': '02-111-1111', #key: value
    '김밥카페': '02-222-2222',
    '순남시레기': '02-333-3333'
}

#1. 방법1
with open('lunch.csv', 'w', encoding='utf-8') as f:
    for item in lunch.items():
        f.write (f'{item[0]}, {item[1]}\n')