#import webbrowser

#webbrowser.open('http://www.msbsound.com/about/')
#webbrowser.open_new('https://www.google.com/')
#webbrowser.open_new_tab('https://www.daum.net/')

import webbrowser
#webbrowser.open('https://search.naver.com/search.naver?query=')

love=["치즈","레드벨벳","오마이걸","러블리즈"]

for idol in love:
    print(type(idol))
    webbrowser.open('https://search.naver.com/search.naver?query='+idol)