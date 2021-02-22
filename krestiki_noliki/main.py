X = "X"
O = "0"
EMPTY = " "
TIE = "Ничья"
NUM_SQUARES = 9


def display_instruct():
    """ Выводит на экран инструкцию к игре"""
    print("""
    Приветствую тебя, мой друг, в лучшей игре тысячилетя!!
    Давай выясним с помощью игры "Крестики-нолики" кто же все таки круче, человеческий мозг или мой процессор!!!
    
    Чтобы сделать ход, введи число от 0 до 8, числа однозначно соответствуют полям доски:
    
                                        0 | 1 | 2
                                        ----------
                                        3 | 4 | 5
                                        ----------
                                        6 | 7 | 8
    
    Ну что, начнем!!! """)


def ask_yes_no(question):
    """ Задает вопрос с ответом да или нет (принимает вопрос, возвращает ответ)"""
    response = None
    while response not in ("да", "нет"):
        response = input(question).lower()
    return response


def pieces():
    """ Определяет кто ходит первым и возвращает значения фишек соответственно для каждого"""
    go_first = ask_yes_no("\nХочешь ходить первым? (да/нет): ")
    if go_first == "да":
        print("\nНу что ж, даю тебе фору, играй крестиками!")
        human = X
        computer = O
    else:
        print("\nХорошо, мой ход первый, ты играешь ноликами!")
        computer = X
        human = O
    return computer, human


def new_board():
    """ Функция создает новую игровую доску - список с пустыми полями, корые будут заполняться крестиками или
    ноликами, а затем красиво выводиться """
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """ Функция отображает, рисует текущую игровую доску на экране (выводит список красиво)"""
    print("\n\t\t\t", board[0], "|", board[1], "|", board[2])
    print("\t\t\t", "---------")
    print("\t\t\t", board[3], "|", board[4], "|", board[5])
    print("\t\t\t", "---------")
    print("\t\t\t", board[6], "|", board[7], "|", board[8], "\n")


def winner(board):
    """ Определяет победителя в игре, чтоб в мейне мы шли до тех пор пока победителя нет, возвращает нам победителя,
    ничью, или то что еще никто не выиграл"""
    WAYS_TO_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
    #  мы указали возмоные выигрышные расположения фишек, теперь мы проверим если три одинаковые фишки стоят
    #  на одной из таких комбинаций, то этот пользователь выиграл или если ни одной комбинации нет
    #  и при этом вся доска заполнена, то это ничья, если еще не вся, то игра продолжается
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            win = board[row[0]]
            return win
        if EMPTY not in board:
            return TIE
    return None


def legal_moves(board):
    """ Получая текущую доску, анализирует ее, вы возвращает список доступных ходов,
    то есть тех полей, в которых нет еще фишек"""
    moves = []
    for square_number in range(NUM_SQUARES):
        if board[square_number] == EMPTY:
            moves.append(square_number)
    return moves


def ask_number(question, low, high):
    """ Запрашивает число из указанного диапазона"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def human_move(board, human):
    """ Получает ход человека - позицию, куда он хочет поставить свою фишку и возвращает ее"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Твой ход, выбери позицию, куда хочешь поставить свою фишку (0-8): ", 0, NUM_SQUARES)
        if move not in legal:
            print("\nСиешной человек, это поле уже занято! Выбери другое!!\n")
    print("Ок, принято...")
    return move


def computer_move(board, computer, human):
    """ Вычисляет лучший ход компьютера и совершает его"""
    board = board[:]
    BEST_MOVES = (4, 9, 2, 6, 8, 1, 3, 5, 7)
    print("Я выберу поле номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:  # сначала проверяет, может ли победить, потом может
            print(move)  # ли предотвратить победу, потом просто лучший ход
            return move
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


def next_turn(turn):
    """ Осуществляет переход хода - возвращает измененное значенеи фишки"""
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    """ Функция осуществляет поздравление победителя или констатирует ничью"""
    if the_winner != TIE:
        print("Три", the_winner, "в ряд!\n")
    else:
        print("Ничья!\n")
    if the_winner == computer:
        print("Я же говорил, что выграю, так и случилось!!! \n")
    elif the_winner == human:
        print("Ладно, в этот раз ты перехитрил меня, но я еще отыграюсь!")
    elif the_winner == TIE:
        print("У нас ничья, сегодня тебе повезло, но радуйся недолго!")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X  # текущий ход, далее будем проверять чей ход и
    board = new_board()  # взависимости от этого вызывать нужную функцию
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)  # определяется ход человека и на тот номер,
            board[move] = human  # который он выбрал ан доске ставится его фишка
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# запуск программы
main()
