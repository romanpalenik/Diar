import datetime
import pickle
one_digit_number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


class CalendarEvents:
    """Class to take care of calendar events"""

    def change_format_to_database_index(self, date):
        """change format to year, day, month"""
        year = date[0:4] + ','
        month = date[4:6]
        day = date[6:8]
        if month[0] == '0':
            month = month[1]

        if day[0] == '0':
            day = day[1]

        day = ' ' + day + ','
        month = ' ' + month

        return year + day + month

    def check_and_repair_right_format(self, digit):
        """Check if if number has one digit, if yes add zero to start"""
        if digit in one_digit_number:
            digit = '0' + digit
        return digit


    def get_today(self):
        """function return today in format yearMonthDay"""
        # using now() to get current time
        current_time = datetime.datetime.now()
        day = str(current_time.day)
        month = str(current_time.month)

        day = self.check_and_repair_right_format(day)
        month = self.check_and_repair_right_format(month)

        return str(current_time.year) + month + day


    def date_to_operate_format(self, date):
        """change date to format yearMonthDay, that can be doing mathematical operation with"""
        date = date.replace(" ", "")
        date = date.split(',')
        day = date[1]
        month = date[2]

        day = self.check_and_repair_right_format(day)
        month = self.check_and_repair_right_format(month)

        right_format = date[0] + month + day
        return right_format

    def __init__(self):
        self.events = {}
        self.load_list()



    def load_list(self):
        """Load information events from output.dat"""
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/output.dat', 'rb') as f:
            self.events = pickle.load(f)

    def locate_nearest_event(self):
        """find what event is nearest to today"""
        nearest_event_date = ''
        min = 1000000
        today = self.get_today()
        event_array = self.events.keys()
        for event_date in event_array:
            event_date = self.date_to_operate_format(event_date)
            if int(event_date) - int(today) > 0:
                if int(event_date) - int(today) < min:
                    min = int(event_date) - int(today)
                    nearest_event_date = event_date

        nearest_event = '0'
        if len(event_array) > 0:
            nearest_event = self.change_format_to_database_index(nearest_event_date)

        return nearest_event

    def save_new_event(self, event, date, type, time):

        whole_event = [event, type, time]
        if len(event) == 0:
            del self.events[date]
        else:
            self.events[date] = whole_event
        with open('/home/roman/Skola/ProjektyMimo/ApkaNaSkolu/output.dat', 'wb') as f:
            pickle.dump(self.events, f)

