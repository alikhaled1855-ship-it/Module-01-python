class Plant:
    def __init__(self, name :str, height :float, age :int) -> None:
        if height < 0:
            self._height = 0.0
        else:
            self._height = height
        if age < 0:
            self._age = 0
        else:
            self._age = age
        self._name = name
    def get_height(self) -> float:
        return self._height
    def get_age(self) -> int:
        return self._age
    def set_height(self, value :float) -> None:
        if value < 0:
            print(self._name + ": Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print("Height updated: " + str(value) + "cm")
    def set_age(self, value :int) -> None:
        if value < 0:
            print(self._name + ": Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print("Age updated: " + str(value) + " days")

    def show(self) -> None:
        print(self._name + ": " + str(self._height) + "cm, " + str(self._age) + " days old")
    def grow_plant(self) -> None:
        self._height = round(self._height + 0.8, 1)
    def age_plant(self) -> None:
        self._age += 1

if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    rose.set_height(25.0)
    rose.set_age(30)
    rose.set_height(-1)
    rose.set_age(-1)
    print("Current state: ", end="")
    rose.show()
