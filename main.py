import random

def generate_number():
    return random.randint(1, 10)

def play_game():
    secret = generate_number()
    attempts = 0
    print("Я загадал число от 1 до 10. Попробуй угадать!")
    while True:
        try:
            guess = int(input("Твой вариант: "))
            attempts += 1
            if guess < secret:
                print("Больше")
            elif guess > secret:
                print("Меньше!")
            else:
                print(f"Поздравляю! Ты угадал за {attempts} попыток.")
                break
        except ValueError:
            print("Ошибка: введи целое число.")

    again = input("Хочешь сыграть ещё? (y/n): ").lower()
    if again == 'y':
        play_game()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    play_game()