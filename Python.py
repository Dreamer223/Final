# Функция для сохранения заметок в файл
def save_notes(notes):
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")

# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open("notes.txt", "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        return []

# Функция для добавления новой заметки
def add_note():
    note = input("Введите новую заметку: ")
    notes.append(note)
    print("Заметка добавлена.")

# Функция для просмотра заметок
def view_notes():
    if not notes:
        print("У вас нет заметок.")
    else:
        print("Ваши заметки:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")

# Функция для удаления заметки
def delete_note():
    view_notes()
    try:
        note_index = int(input("Введите номер заметки для удаления: ")) - 1
        if 0 <= note_index < len(notes):
            deleted_note = notes.pop(note_index)
            print(f"Заметка '{deleted_note}' удалена.")
        else:
            print("Неправильный номер заметки.")
    except ValueError:
        print("Неправильный ввод. Введите номер заметки для удаления.")

def edit_note():
    view_notes()
    try:
        note_index = int(input("Введите номер заметки для редактирования: ")) - 1
        if 0 <= note_index < len(notes):
            new_note = input("Введите новое содержание заметки: ")
            notes[note_index] = new_note
            print(f"Заметка отредактирована.")
            save_notes(notes)
        else:
            print("Неправильный номер заметки.")
    except ValueError:
        print("Неправильный ввод. Введите номер заметки для редактирования.")

# Основной код программы
notes = load_notes()

while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Просмотреть заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == "1":
        add_note()
        save_notes(notes)
    elif choice == "2":
        view_notes()
    elif choice == "3":
        edit_note()
    elif choice == "4":
        delete_note()
        save_notes(notes)
    elif choice == "5":
        print("Выход из программы.")
        save_notes(notes)  # Сохраняем заметки перед выходом
        break
    else:
        print("Неправильный выбор. Пожалуйста, выберите снова.")