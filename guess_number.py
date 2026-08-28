import random


def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    print("Игра «Угадай число»")
    print("Я загадал число от 1 до 100.")
    print(f"У вас есть {max_attempts} попыток, чтобы его угадать.")

    while attempts < max_attempts:
        user_input = input(
            f"\nПопытка {attempts + 1}/{max_attempts}. "
            "Введите число: "
        )

        try:
            guess = int(user_input)
        except ValueError:
            print("Ошибка: необходимо ввести целое число.")
            continue

        if guess < 1 or guess > 100:
            print("Ошибка: число должно находиться от 1 до 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Слишком маленькое число.")
        elif guess > secret_number:
            print("Слишком большое число.")
        else:
            print(
                f"Поздравляю! Вы угадали число {secret_number} "
                f"за {attempts} попыток."
            )
            return

    print(f"\nПопытки закончились. Загаданное число было: {secret_number}")


def main():
    while True:
        play_game()

        answer = input("\nХотите сыграть еще раз? (да/нет): ").lower()

        if answer not in ("да", "д"):
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    main()
