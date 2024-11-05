"Базы данных на классах"

import sqlite3

class DataBase:
    def __init__(self, db_name="notes.db"):
        self.connection=sqlite3.connect(db_name)
        self.cursor=self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
                        CREATE TABLE IF NOT EXISTS notes(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT,
                        content TEXT,
                        created_at DATE
    )
""")
        self.connection.commit()



    def add_note(self, note):
        self.cursor.execute("""
                            INSERT INTO notes
                            (title, content, created_at) 
                            VALUES(?, ?, ?)""", (note.title, note.content, note.created_at))
        self.connection.commit()
        print('Заметка успешно добавлена')

    def get_notes(self):
        self.cursor.execute("SELECT * FROM notes")
        notes = self.cursor.fetchall()
        for note in notes:
            print(f'Заголовок заметки: {note[1]}, дата создания: {note[3]}')
            
    
    def update_note(self, new_title, new_content, notes_id):
        self.cursor.execute("""
                        UPDATE notes  
                        SET title = ?, content=?
                        WHERE id = ?""", (new_title, new_content, notes_id))
        
        self.connection.commit()
        print('Заметка успешно обновлена')


    def delete_note(self, notes_id):
        self.cursor.execute("DELETE FROM notes WHERE id=?", (notes_id,))

        self.connection.commit()
        print(f'Заметка с id {notes_id} была удалена')