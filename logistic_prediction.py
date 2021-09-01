from functions import research, nickname
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers

html_code = research()

html = BeautifulSoup(html_code, 'html.parser')

kills, deaths, assists, game_results, KDAs, game_last_results = [], [], [], [], [], [[0 for col in range(4)] for row in range(20)]
j = 0

for i in range(0, 60, 3):
    kill = int(html.select('.GameItem>.Content>.KDA>.KDA>span')[i].get_text())
    death = int(html.select('.GameItem>.Content>.KDA>.KDA>span')[i+1].get_text())
    assist = int(html.select('.GameItem>.Content>.KDA>.KDA>span')[i+2].get_text())
    game_result = html.select('.GameResult')[j].get_text()

    game_result = ''.join(game_result.split())

    game_last_results[j][0] = kill
    game_last_results[j][1] = death
    game_last_results[j][2] = assist
    game_last_results[j][3] = game_result
    j += 1

index = [
    'Game 1',
    'Game 2',
    'Game 3',
    'Game 4',
    'Game 5',
    'Game 6',
    'Game 7',
    'Game 8',
    'Game 9',
    'Game 10',
    'Game 11',
    'Game 12',
    'Game 13',
    'Game 14',
    'Game 15',
    'Game 16',
    'Game 17',
    'Game 18',
    'Game 19',
    'Game 20'
]

df_record = pd.DataFrame(game_last_results, columns=['Kills', 'Deaths', 'Assists', 'GameResult'], index=index)

df_record['KDAs'] = round((df_record['Kills'] + df_record['Assists']) / df_record['Deaths'], 2)
for i in range(20):
    if df_record.iloc[i, 1] == 0:
        df_record.iloc[i, 4] = round(df_record.iloc[i, 0] + df_record.iloc[i, 2], 2)

#------------------------------------------------------------------------------- 데이터프레임화 완료

for i in range(20):
    if df_record.iloc[i, 3] == '승리':
        df_record.iloc[i, 3] = 1
    else:
        df_record.iloc[i, 3] = 0

x, y = [], []
for i in range(20):
    x.append(df_record.iloc[i, 4])
    y.append(df_record.iloc[i, 3])

model = Sequential()
model.add(Dense(1, input_dim=1, activation='sigmoid'))

sgd = optimizers.SGD(learning_rate=0.01)
model.compile(optimizer=sgd ,loss='binary_crossentropy', metrics=['binary_accuracy'])

model.fit(x, y, batch_size=1, epochs=1000, shuffle=False)

for i in range(20):
    if y[i] == 1:
        plt.scatter(x[i], y[i], color='blue')
    else:
        plt.scatter(x[i], y[i], color='red')

sns.regplot(x=x, y=y, data=df_record, logistic=True)
plt.show()

num = float(input("승률을 알고 싶은 kda를 입력하세요. : "))

print(model.predict([num]))
print("{0}님의 KDA {1}의 승률은 {2}%입니다.".format(nickname, num, model.predict([num])[0][0] * 100))