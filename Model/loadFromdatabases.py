import pickle


class Databases:
    """Class to take care of loading from database"""

    def load_list(self) -> list:
        """Load information to do list from to_do.dat"""
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/to_do.dat', "rb") as file:
            toDoList = pickle.load(file)

        return toDoList

    def save_to_do_list(self, to_do):
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/to_do.dat', 'wb') as f:
            pickle.dump(to_do, f)

    def delete_from_list(self, note_to_delete, to_do_list):
        for i in range(len(to_do_list)):
            if note_to_delete == to_do_list[i]:
                del to_do_list[i]
                return to_do_list



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