def game():
    return 125

score = game()
with open('HISCORE.txt') as f:
    high_score = f.read()

if high_score == '':
    with open('HISCORE.txt', 'w') as f:
        f.write(str(score))

elif int(high_score) < score :
    with open('HISCORE.txt', 'w') as f:
        f.write(str(score))