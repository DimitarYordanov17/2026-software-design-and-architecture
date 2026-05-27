from abc import ABC, abstractmethod


class ArrivalStrategy(ABC):
    @abstractmethod
    def arrive(self):
        pass


class RunningWithJumps(ArrivalStrategy):
    def arrive(self):
        print("Arriving by running with jumps!")


class Teleportation(ArrivalStrategy):
    def arrive(self):
        print("Arriving by teleportation!")


class SleepingOnBus(ArrivalStrategy):
    def arrive(self):
        print("Arriving by sleeping on the bus!")


class Student:
    def __init__(self, name, student_type, strategy):
        self.name = name
        self.student_type = student_type
        self._strategy = strategy

    def arrive(self):
        self._strategy.arrive()

    def describe(self):
        return f"{self.name} ({self.student_type})"


class FunTask:
    def describe(self):
        return "Fun Task: solve a puzzle!"


class IncomprehensibleTask:
    def describe(self):
        return "Incomprehensible Task: decipher ancient runes!"


class EasyTask:
    def describe(self):
        return "Easy Task: write your name!"


class TaskFactory:
    @staticmethod
    def create(student_type):
        tasks = {
            "prodigy": FunTask,
            "fitness_maniac": IncomprehensibleTask,
            "lucky": EasyTask,
        }
        if student_type not in tasks:
            raise ValueError(f"Unknown student type: {student_type}")
        return tasks[student_type]()


class SuperpowerDecorator(ABC):
    def __init__(self, student):
        self._student = student

    @property
    def student_type(self):
        return self._student.student_type

    def arrive(self):
        self._student.arrive()

    def describe(self):
        return self._student.describe()


class SuperConcentration(SuperpowerDecorator):
    def describe(self):
        return self._student.describe() + " + Super Concentration"


class FastWriting(SuperpowerDecorator):
    def describe(self):
        return self._student.describe() + " + Fast Writing"


class Telepathy(SuperpowerDecorator):
    def describe(self):
        return self._student.describe() + " + Telepathy"


class University:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("University is open for exam day!")
        return cls._instance

    def process_student(self, student):
        student.arrive()
        task = TaskFactory.create(student.student_type)
        print(f"{student.describe()} → {task.describe()}\n")


if __name__ == "__main__":
    alice = Student("Alice", "prodigy", RunningWithJumps())
    bob = Student("Bob", "fitness_maniac", Teleportation())
    charlie = Student("Charlie", "lucky", SleepingOnBus())

    alice = SuperConcentration(alice)
    bob = FastWriting(bob)
    charlie = Telepathy(charlie)

    uni1 = University()
    uni2 = University()
    print(f"Same university instance: {uni1 is uni2}\n")

    uni1.process_student(alice)
    uni1.process_student(bob)
    uni1.process_student(charlie)
