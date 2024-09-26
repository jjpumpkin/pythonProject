# _*_ coding: utf-8 *
# w rite, a ppend, r ead
f= open('diary.txt', 'a',encoding='utf8')
f.write('오늘의 일기...\n')
while True:
    n= input('내용입력:(종료q)')
    if 'q' ==n:
        break
        f.write(n)
        f.writelines('\n')
    f.close()