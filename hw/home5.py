#  Часть 1 — Декоратор логирования

def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} вызвана с аргументами {args}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        print("Функция завершена")
        return result
    return wrapper


@log_execution
def add(a, b):
    return a + b


add(5, 3)

#  Часть 2 — Декоратор проверки доступа

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role


def require_admin(func):
    def wrapper(user):
        if user.role != "admin":
            print("Доступ запрещён")
            return
        return func(user)
    return wrapper


@require_admin
def delete_database(user):
    print("База данных удалена")


# ---- TEST ----
admin = User("Becky", "admin")
regular = User("Nurbek", "user")

delete_database(admin)     # allowed
delete_database(regular)  # denied