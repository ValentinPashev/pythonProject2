from project import BaseFish


class DeepSeaFish(BaseFish):

    TIME_TO_CATCH = 180

    def __init__(self, name, points):
        super().__init__(name, points, self.TIME_TO_CATCH)

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} " \
               f"[Points: {self.points}, Time to Catch: " \
               f"{self.time_to_catch} seconds]"