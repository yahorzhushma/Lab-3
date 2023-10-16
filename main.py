while True:
    print("\nГлавное меню:")
    print("1. Копирование из F1 в F2")
    print("2. Студенты")
    print("3. Предметы")
    print("4. Завершение программы")

    choice = input("Введите номер действия: ")

    if choice == '1':

        with open('F1.txt', 'w') as f1:
            print("Введите данные в файл F1. Для завершения введите пустую строку.")
            while True:
                line = input()
                if not line:
                    break
                f1.write(line + '\n')
        with open('F1.txt', 'r') as f1:
            content = f1.read()

        while True:
            if len(content) == 0:
                print("Файл пуст.")
                break

            while True:
                try:
                    N = int(input("Введите N: "))
                    K = int(input("Введите K: "))

                    with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
                        lines = f1.readlines()
                        if N <= 0 or K <= 0:
                            print("N и K должны быть положительными числами.")
                        elif N > len(lines) or K > len(lines):
                            print("N и K не могут превышать количество строк в файле.")
                        elif N > K:
                            print("N не может быть больше K.")
                        else:
                            for i in range(N - 1, min(K, len(lines))):
                                f2.write(lines[i])
                            print("Копирование завершено.")
                            break

                except ValueError:
                    print("Ошибка: Введите корректное целое число для N и K.")

            def is_consonant(char):
                consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
                return char in consonants

            with open('F2.txt', 'r') as f2:
                text = f2.read()
                consonant_count = sum(1 for char in text if is_consonant(char))

            print(f"Количество согласных букв в файле F2: {consonant_count}")
            break

    elif choice == '2':
        with open('студенты.txt', 'r') as file:
            for line in file:
                data = line.split()
                name = data[0]
                scores = [int(x) for x in data[1:]]

                average_score = sum(scores) / len(scores)

                if average_score < 6:
                    print(f"{name}: {average_score}")

    elif choice == '3':
        subjects_dict = {}

        with open('предметы.txt', 'r') as file:
            for line in file:
                parts = line.split(":")
                subject = parts[0].strip()
                info = parts[1].strip()

                data = info.split()

                total_lessons = 0

                for item in data:
                    if item.endswith("(л)"):
                        total_lessons += int(item[:-3])
                    elif item.endswith("(пр)"):
                        total_lessons += int(item[:-4])
                    elif item.endswith("(лаб)"):
                        total_lessons += int(item[:-5])

                subjects_dict[subject] = total_lessons

        print("Словарь с общим количеством занятий по предметам:")
        print(subjects_dict)

    elif choice == '4':
        break

    else:
        print("Неверный выбор. Попробуйте снова.")
