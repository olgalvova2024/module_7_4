team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
print('В команде Мастера кода участников: %s !' % team1_num)

print('Итого сегодня в командах участников: %s и %s !' %(team1_num,team2_num))

print('Команда Волшебники данных решила задач: {} !'.format(score2))

print('Волшебники данных решили задачи за {} с !'.format(team2_time))

tasks_total = score1 + score2
print(f'Команды решили {score1} и {score2} задач')

if score1 > score2 or score1 == score2 and team1_time > team2_time:
    challenge_result = 'Мастера кода'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = 'Волшебники Данных'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: победа команды {challenge_result}!')

time_avg = round((team1_time+team2_time)/tasks_total,2)
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')