from functions import in_game_playing, nickname
import time

is_gaming = in_game_playing()
cnt = 0

if is_gaming:
    print("{0}님은 지금 게임중입니다.".format(nickname))
    for i in range(100):
        if is_gaming:
            if cnt != 0:
                print("{0}님의 게임이 시작되었습니다.".format(nickname))
            cnt += 1
        else:
            print("{0}님의 게임이 끝났습니다.".format(nickname))
        time.sleep(180)
else:
    print("{0}님은 지금 게임중이 아닙니다.".format(nickname))