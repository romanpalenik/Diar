class CalendarEvents:
    """Class to take care of calendar events"""

    def __init__(self):
        self.load_list()

    def load_list(self) -> list:
        """Load information do list from events.txt"""
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/events.txt', "r") as file:
            toDoList = []
            for line in file:
                toDoList.append(line)

        return toDoList
