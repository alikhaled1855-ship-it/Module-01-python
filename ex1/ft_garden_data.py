class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def show(self):
        print(self.name + ": " + str(self.height) + "cm, " + str(self.age) + " days old")
if __name__ == "__main__":
    rose = Plant("Rose",25,30)
    rose.show()