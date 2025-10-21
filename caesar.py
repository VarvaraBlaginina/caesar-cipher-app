def generate_alphabet():
    return ''.join(chr(i) for i in range(33, 127))+''.join(chr(i) for i in range(ord('А'), ord('Я') + 1)) + \
               ''.join(chr(i) for i in range(ord('а'), ord('я') + 1))

# Определяем функцию шифра Цезаря
def caesar_cipher(text, shift, alphabet):
    # Создаем пустой список для хранения результата
    result = []
    # Перебираем каждый символ в исходном тексте
    for char in text:
        # Проверяем, есть ли символ в нашем алфавите
        if char in alphabet:
            # Вычисляем новый индекс с учетом сдвига (с циклическим перебором)
            index = (alphabet.index(char) + shift) % len(alphabet)
            # Добавляем зашифрованный символ в результат
            result.append(alphabet[index])
        else:
            # Если символа нет в алфавите, добавляем его без изменений
            result.append(char)
    # Объединяем символы в строку и возвращаем результат
    return ''.join(result)

def main():
    alphabet = generate_alphabet()
    choice = input("Выберите способ ввода (1 - клавиатура, 2 - файл): ")
    if choice == '1':
        text = input("Введите строку для шифрования: ")
    elif choice == '2':
        filename = input("Введите имя файла: ")
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
        except FileNotFoundError:
            print("Файл не найден.")
            return
    else:
        print("Неверный выбор.")
        return

    shift = int(input("Введите коэффициент сдвига: "))

    # Шифруем текст
    encrypted_text = caesar_cipher(text, shift, alphabet)
    print("Зашифрованная строка:", encrypted_text)
    
    # Спрашиваем, нужно ли расшифровать текст
    decrypt_choice = input("Хотите расшифровать строку? (1 - да / 2 - нет): ").lower()
    if decrypt_choice == '1':
        # Дешифруем текст (используя отрицательный сдвиг)
        decrypted_text = caesar_cipher(encrypted_text, -shift, alphabet)
        print("Расшифрованная строка:", decrypted_text)
    else:
        print("Расшифровка не выполнена.")

if __name__ == "__main__":
    main()