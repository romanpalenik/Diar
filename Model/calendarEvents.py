class CalendarEvents:
    """Class to take care of calendar events"""

    def __init__(self):
        self.events = {}
        self.load_list()

    def load_list(self):
        """Load information do list from events.txt"""
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/events.txt', "r") as file:
            for line in file:
                line = line.split(';')
                self.events[line[0]] = line[1]

