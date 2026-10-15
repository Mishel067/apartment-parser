from random import choice
import time
import os

def show_field():
    global em
    global field
    for i in field:
        print(''.join([em[j] for j in i]))
def ask_for_game():
    start_phrase = ('Hello! Would you like to play?',
                    'Good day! Would you like to play?',
                    'Hi! How about a game?')
    phrase = ('Shall we play again?',
              'Do you want to play again?',
              'Would you like to play once more?')
    ans = ''
    while ans.lower() not in ('yes', 'no'):
        if games >= 1:
            print(choice(phrase))
        else:
            print(choice(start_phrase))
        ans = input()
        clear_console()
        if ans.lower() == 'no':
            print('OK. See you next time :)')
            time.sleep(1)
            clear_console()
            return False
        elif ans.lower() == 'yes':
            print('The game begins')
            time.sleep(1)
            clear_console()
            return True
        else:
            print('Invalid data. Please write “yes” or “no”.')
def who_goes_first():
    while True:
        order = input('Will you go first (X) or second (O)?(1 or 2)')
        if order in ('1', '2'):
            return int(order)
        print('Invalid data')

def rut(order):
    global cnt
    cnt += 1
    show_field()
    if cnt == 9:
        print('Its a draw')
        return True
    res = check_result(order)
    if res:
        return res
    elif cnt == 9:
        print('Its a draw')
        return True
def user_input(order):
    global field
    if order == 1:
        print("It's your turn, you're Xs")
    else:
        print("It's your turn, you're Os")
    move = [int(i) - 1 for i in input('Enter the row and column number').split()]
    try:
        if field[move[0]][move[1]] == 0:
            field[move[0]][move[1]] = order
            print('Great idea')
        else:
            print('Already occupied')
            user_input(order)
    except RecursionError:
        print('Too many attempts... Please replay')
    except:
        print('Invalid data')
        user_input(order)
def computer_move(order):
  global field
  lst = []
  for i in range(3):
      for j in range(3):
          if field[i][j] == 0:
               lst.append((i, j))
  pos = choice(lst)
  if order == 1:
      field[pos[0]][pos[1]] = 2
  else:
      field[pos[0]][pos[1]] = 1
def check_result(order):
    global field
    win_pos = (((0, 0), (0, 1), (0, 2)),
               ((1, 0), (1, 1), (1, 2)),
               ((2, 0), (2, 1), (2, 2)),
               ((0, 0), (1, 1), (2, 2)),
               ((2, 0), (1, 1), (0, 2)),
               ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (1, 2)),
               ((0, 2), (1, 2), (2, 2)))
    for i in win_pos:
        if field[i[0][0]][i[0][1]] == field[i[1][0]][i[1][1]] == field[i[2][0]][i[2][1]] and field[i[0][0]][i[0][1]] != 0:
            if field[i[0][0]][i[0][1]] == order:
                print('Wow, XD YOU WON')
            else:
                print('Ohh... YOU LOSE. See you next time')
            return True
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
em = {0: '⬜', 1: '❌', 2: '⭕'}
field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
cnt, games = (0, 0)
def main_game():
    global field
    global games
    while True:
        cnt = 0
        field = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        if not ask_for_game():
            return
        order = who_goes_first()
        while True:
            if order == 1:
                user_input(order)
                clear_console()
                if rut(order):
                    break
                computer_move(order)
                print()
                if rut(order):
                    break
            else:
                computer_move(order)
                print()
                if rut(order):
                    break
                user_input(order)
                clear_console()
                if rut(order):
                    break
        games += 1
main_game()



