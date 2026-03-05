import sqlite3

# Журнал с пустыми белыми листами
connect = sqlite3.connect("users.db")
# рука с ручкой
cursor = connect.cursor()



cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()

# CRUD Create - Read - Update - Delete

def create_user(name, age, hobby):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        'INSERT INTO users(age, name, hobby) VALUES (?,?,?)',
        (age, name, hobby)
    )
    connect.commit()
    print(f"{name} Создан!!")

# create_user("John", 25, "Наваливать боком!!")

def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)

# get_users()

def update_user(name, rowid):
    cursor.execute(
        'UPDATE users SET name = ? WHERE rowid = ?',
        (name, rowid)
    )
    connect.commit()
    print('Обновлен!!')

update_user("Arzy", 3)

get_users()

def delete_user(rowid):
    cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print('Удалено!!')

delete_user(2)