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
