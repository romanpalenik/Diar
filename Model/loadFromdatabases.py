class Load_From_databases:
    """Class to take care of loading from database"""

    def load_list(self) -> list:
        """Load information do list from todo.txt"""
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/todo.txt', "r") as file:
            toDoList = []
            for line in file:
                toDoList.append(line)

        return toDoList

    def load_events_types(self) -> list:
        """load name of subject """
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/predmety.txt', "r") as file:
            events_types = []
            events_types.append('Škola')
            events_types.append('Iné')
            for line in file:
                line = line.replace('\n', "")
                events_types.append(line)

        return events_types