"Домашнее задание: БД без классов"

import sqlite3
connect=sqlite3.connect("notes.db")
cursor=connect.cursor()


cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            created_at DATE
    )
""")

def add_note():
    title=input('Введите заголовок заметки:')
    content=input('Введите содержание заметки(описание):')
    created_at=input('Введите дату заметки:')
    


    cursor.execute("""INSERT INTO notes(title, content, created_at) VALUES(?, ?, ?)""", (title, content, created_at))
    connect.commit()
    print('Заметка успешно добавлена')

def get_notes():
    cursor.execute("SELECT * FROM notes")
    notes = cursor.fetchall()
    for note in notes:
        print(f'Заголовок заметки: {note[1]}, дата создания: {note[3]}')

def update_note():
    notes_id=int(input('Введите id заметки, которую хотите изменить:'))
    new_title=input('Введите новый заголовок заметки:')
    new_content=input('Введите новое содержание(описание) заметки:')
    cursor.execute("""
        UPDATE notes 
        SET title = ?, content=?
        WHERE id = ?
    """, (new_title, new_content, notes_id))
    connect.commit()
    print('Заметка успешно обновлена')


def delete_note():
    notes_id=input('Введите id заметки для удаления:')
    cursor.execute("DELETE FROM notes WHERE id=?", (notes_id,))
    connect.commit()
    print('Заметка была удалена')


def menu():
    while True:
        print("""
1. Добавить заметку
2. Посмотреть все заметки
3. Редактировать заметку
4. Удалить заметку
5. Выйти
""")
        choice=input('Выберите действие:')
        if choice=='1':
            add_note()
        elif choice=='2':
            get_notes()
        elif choice=='3':
            update_note()
        elif choice=='4':
            delete_note()
        elif choice=='5':
            break
        else:
            print('Некорректный выбор. Попробуйте ещё раз')

# menu()