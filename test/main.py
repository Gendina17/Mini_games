import sys


def open_file(file_name, mode):
    """ Открывает файл"""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Невозможно открыть файл", file_name, ". Работа программы будет завершена.\n", e)
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """ Читает и возвращает очередную строку из файла"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """ Возвращает очередной блик вопроса ( у каждого вопроса 7 строк: категоря, сам вопрос, 4 варианта ответа,
    правиный ответ и пояснение) """
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation


def welcome(title):
    """ Функция приветствует игрока и сообщает тему игры"""
    print("\t\t Добро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")


def main():
    file = open_file("game.txt", "r")
    title = next_line(file)
    welcome(title)
    score = 0  # счет в игре
    category, question, answers, correct, explanation = next_block(file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        answer = input("Ваш ответ: ")
        if answer == correct:
            print("\nДа!", end=" ")
            score += 1
        else:
            print("\nНет.", end=" ")
        print(explanation)
        print("Счет: ", score, "\n\n")
        category, question, answers, correct, explanation = next_block(file)
    file.close()
    print("Это был последний вопрос!")
    print("На вашем счету", score)


# запуск игры
main()
