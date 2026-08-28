import math


def calculate_factorial():
    while True:
        user_input = input("Введите положительное целое число: ")

        try:
            number = int(user_input)

            if number <= 0:
                print("Ошибка: число должно быть положительным.")
                continue

            result = math.factorial(number)

            print(f"Факториал числа {number} равен {result}")
            break

        except ValueError:
            print("Ошибка: необходимо ввести целое число.")


if __name__ == "__main__":
    calculate_factorial()
