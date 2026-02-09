class AnimeCharacter:
    def __init__(self, name, mood, body):
        self.name = name
        self.mood = mood
        self.body = body

    def describe_body(self):
        return f"{self.name}'s body is {self.body}"

    def cry(self):
        if self.mood == "sad":
            self.mood = "calm"
            return f"{self.name} cried and is now {self.mood}"
        else:
            return f"{self.name} is not sad, no need to cry"


tomura = AnimeCharacter("Tomura", "sad", "skinny")
naruto = AnimeCharacter("Naruto", "angry", "strong")

print(tomura.describe_body())
print(tomura.cry())

print(naruto.describe_body())
print(naruto.cry())
