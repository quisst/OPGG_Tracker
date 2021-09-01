from functions import research, get_info
import time

name, minute, second, result = 0, 0, 0, 0

for i in range(100):
    print("{0}번째".format(i+1))
    name, minute1, second1, result1 = get_info(research())
    if minute1 != minute or second1 != second or result1 != result:
        minute, second, result = minute1, second1, result1
        print("{0}님이 {1}분{2}초의 경기 결과 {3}하셨습니다.".format(name, minute, second, result))
    time.sleep(180)