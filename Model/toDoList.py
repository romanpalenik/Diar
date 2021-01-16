class ToDoList:
    """Class to take care of notes"""

    def load_list(self) -> list:
        """Load information do list from todo.txt"""
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/todo.txt', "r") as file:
            toDoList = []
            for line in file:
                toDoList.append(line)


        return toDoList
