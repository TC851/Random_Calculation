# The program generates random calculation tasks
import random


class ExampleQuiz:
    def __init__(self):
        self.__a = 0
        self.__b = 0

    # Generate a random between 1 and 50
    def getExercise(self):
        self.__a = int(random.randint(1, 50))
        self.__b = int(random.randint(1, 50))

        return str(self.__a) + " + " + str(self.__b) + " " + " = ?"

    def getResult(self):
        return self.__a + self.__b


# main -------------------------------------------------------------------------------------
quiz = ExampleQuiz()
print(quiz.getExercise())
print("Result is" + " " + str(quiz.getResult()))
print()
print(quiz.getExercise())
print("Result is" + " " + str(quiz.getResult()))


