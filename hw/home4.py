# Magic methods ONLY

# 1) Class Movie

class Movie:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f"{self.title} ({self.duration} min)"

    def __add__(self, other):
        if type(self) == type(other):
            return self.duration + other.duration
        else:
            return NotImplemented

    def __eq__(self, other):
        return self.title == other.title and self.duration == other.duration

m1 = Movie("Matrix", 136)
m2 = Movie("Inception", 148)
m3 = Movie("Interstellar", 169)

print(m1 + m2)   # 237
print(m1 == m2)  # False
print(m1)
print(m2)
print(m3)

# 2) Class Library

class Library:
    def __init__(self, movies):
        self.movies = movies

    def __getitem__(self, item):
        return self.movies[item]

    def __len__(self):
        return len(self.movies)

    def __str__(self):
        result = ""
        i = 1
        for movie in self.movies:
            result += f"{i}. {movie}\n"
            i += 1
        return result.rstrip()

library = Library([m1, m2, m3])

print(library[1])
print(len(library))
print(library)


# 3) Class User

class User:
    def __init__(self, name, library):
        self.name = name
        self.library = library

    def __call__(self):
        print(f"User {self.name} is watching movies")

    def __str__(self):
        return f"User {self.name} | Movies: {len(self.library)}"

user = User("Alex", library)

print(user)
user()