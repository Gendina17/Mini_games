# Игра Виселица

import random

MAN = ("""
____
|  |
|  |
|  
| 
|  
| 
""",
       """
____
|  |
|  |
|  O
| 
|  
| 
""",
       """
____
|  |
|  |
|  O
|  |
|  
| 
""",
       """
____
|  |
|  |
|  O
| /|
|  
| 
""",
       """
____
|  |
|  |
|  O
| /|\\
|  
|  
""",
       """
____
|  |
|  |
|  O
| /|\\
|  |
| 
""",
       """
____
|  |
|  |
|  O
| /|\\
|  |
| / 
""",
       """
____
|  |
|  |
|  O
| /|\\
|  |
| / \\ 
""")

MAX_WRONG = len(MAN)-1
WORDS = ("ПРОГРАММИРОВАНИЕ", "ИГРА", "ХОЛОДИЛЬНИК", "ИСКУССТВО", "РАДОСТЬ", "ПОЧТА", "ПИСЬМО", "КАЙФ")

word = random.choice(WORDS)
current = "_" * len(word)
wrong = 0
letters = []

print("Приветствую тебя, мой друг! Отгадай все слова, желаю удачи!!")

while wrong < MAX_WRONG and current != word:
    print(MAN[wrong])
    if letters:
        print("Уже названные буквы:\n", letters)
    print("Текущее слово:\n", current)
    current_letter = input("\n\nВведите букву: ").upper()
    while current_letter in letters:
        print("Вы уже вводили букву", current_letter)
        current_letter = input("\n\nВведите букву: ").upper()
    letters.append(current_letter)
    if current_letter in word:
        print("Вы правильно отгадали! Буква", current_letter.upper(), "есть в слове!")
        new = ""
        for i in range(len(word)):
            if current_letter == word[i]:
                new += current_letter
            else:
                new += current[i]
        current = new
    else:
        print("\nК сожалению, буквы", current_letter, "нет в слове")
        wrong += 1

if wrong == MAX_WRONG:
    print(MAN[wrong])
    print("\nВы проиграли и вас повесили!!! В следующий раз обязательно повезет!")
else:
    print("\nПоздравляю, вы отгадали слово!!!!")

print("\nБыло загадано:", word.upper())
input("\n\nНажмите Enter, чтобы выйти.")




