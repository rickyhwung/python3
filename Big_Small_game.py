import random

def roll_dice(numbers=3, points=None):
    print('<<<< ROLL THE DICE! >>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers -1
    return points

def roll_result(total):
    isBig = 11 <= total <=18
    isSmall = 3<= total <=10
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small'

def start_game():
    moneys = 1000
    print('<<<< GAME STARTS! >>>>')
    choices = ['Big','Small']
    while moneys >= 0:
        your_choice = input('Big or Small :')
        your_betMoney = input('Hown much you wanna bet?')
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('The points are: {}+{}+{}={}'.format(points[0],points[1],points[2],total),'You Win!')
                moneys = moneys + int(your_betMoney)
                print('You gained {},you have {} now'.format(your_betMoney,moneys))
            else:
                print('The points are: {}+{}+{}={}'.format(points[0], points[1], points[2], total),'You lose!')
                moneys = moneys - int(your_betMoney)
                print('You lost {},you have {} now'.format(your_betMoney, moneys))
        else:
            print('Invalid Words')
            if your_choice == 0:
                break

start_game()