from database import DataBase
class Note:
    def __init__(self, title, content, created_at):
        self.title = title
        self.content = content
        self.created_at = created_at


class NoteService:
    def __init__(self, db_name="notes.db"):
        self.db = DataBase(db_name)

    def add_note1(self, note):
        self.db.add_note(note)
        
    

    def get_notes1(self):
        self.db.get_notes()
        
    
    def update_note1(self, new_title, new_content, notes_id):
        self.db.update_note(new_title, new_content, notes_id)

    
    def delete_note1(self, notes_id):
        self.db.delete_note(notes_id)

        
    def close(self):
        self.db.close()



note_service = NoteService()
def menu():
    while True:
        print("""
1. Добавить заметку
2. Посмотреть все заметки
3. Редактировать заметку
4. Удалить заметку
5. Выйти
""")

        choice = input("Выберите действие: ")
        if choice == '1':
            note = Note(title=input('Введите заголовок заметки:'), content=input("Введите содержание заметки(описание):"), created_at=input('Введите дату заметки:'))

            note_service.add_note1(note)
        
        elif choice == '2':
            note_service.get_notes1()
        
        elif choice == '3':
            notes_id=int(input('Введите id заметки, которую хотите изменить:'))
            new_title=input('Введите новый заголовок заметки:')
            new_content=input('Введите новое содержание(описание) заметки:')
            note_service.update_note1(new_title, new_content, notes_id)
        
        elif choice == '4':
            notes_id=input('Введите id заметки для удаления:')
            note_service.delete_note1(notes_id)
            
    
        elif choice == '5':
            print("Выход из программы.")
            break
        
        else:
            print("Некорректный выбор. Попробуйте снова.")


menu()