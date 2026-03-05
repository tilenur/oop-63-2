import sqlite3

connect = sqlite3.connect('users.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        hobby TEXT
        )
""")

connect.commit()

def create_user(name, age, hobby):
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES(?,?,?)",
        (name, age, hobby)
    )
    connect.commit()
    print(f"user {name} created successfully")

create_user("Aibiike", 25, "sleeping ")

def get_users():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    for i in users:
        print(f"ID: {i[0]}, NAME: {i[1]}, AGE: {i[2]}, HOBBY: {i[3]}")

get_users()

def update_users(ids, name=None, age=None, hobby=None):
    for user_id in ids:
        if name is not None:
            cursor.execute(
                "UPDATE users SET name = ? WHERE id = ?",
                (name, user_id)
            )
        if age is not None:
            cursor.execute(
                "UPDATE users SET age = ? WHERE id = ?",
                (age, user_id)
            )
        if hobby is not None:
            cursor.execute(
                "UPDATE users SET hobby = ? WHERE id = ?",
                (hobby, user_id)
            )

    connect.commit()
    print("Updated!!")

update_users([1,2], hobby="gaming")
update_users([1], name="Alex")
update_users([2], age=30)

get_users()


def delete_users(ids):

    for user_id in ids:
        cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )

    connect.commit()
    print("Deleted!")


delete_users([1])

get_users()