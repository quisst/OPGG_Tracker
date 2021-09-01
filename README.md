# OPGG_Tracker
- op.gg에 있는 정보들을 크롤링 해와서 정보를 제공합니다!

# 파일 설명
- functions.py : 다른 파일들 실행에 필요한 함수들을 모아놓은 곳입니다.
- game_log.py : 켜두고 있으면 3분마다 전적 갱신을 통해 경기결과를 모아 볼 수 있습니다.
- is_playing.py : 게임중이면 게임이 끝날때와 다시 시작할떄 알림을 출력하고 게임중이 아니라면 게임중이 아니라는 것을 출력합니다.
- logistic.prediction.py : Kill, Death, Assist, 경기 결과를 받아와서 데이터프레임을 만들고,
최근 20경기의 KDA((kill+assist)/death)의 값과 승패의 관계를 학습하여 logistic 회귀 그래프를 출력하고 유저에게 KDA값을 받아 예상 승률을 출력합니다.

# 필요 라이브러리
- bs4
- selenium
- time
- pandas
- matplotlib
- seaborn
- tensorflow
