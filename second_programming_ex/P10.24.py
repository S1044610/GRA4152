import re

class Appointment:
    "Superclass for different types of appointments."
    def __init__(self, description, year, month, day):
        self._description = description
        self._date = (year, month, day)
    
    def occursOn(self, year, month, day):
        return self._date == (year, month, day)

    def save(self, file):
        "This save method will be overridden in subclasses."
        raise NotImplementedError
        
    @staticmethod
    def load(file):
        "Load the appointments"
        appointments = []
        for line in file:
            # Split the line into description and date parts
            if 'One time' in line:
                appointment_class = Onetime
            elif 'Daily time' in line:
                appointment_class = Daily
            elif 'Monthly time' in line:
                appointment_class = Monthly
            else:
                raise ValueError(f"Unknown appointment type in line: {line}")
 
            # Use regex to find the date pattern and extract the description
            date_pattern = re.compile(r'(\d{1,2}) (\d{1,2}) (\d{4})')
            date_match = date_pattern.search(line)
            if date_match:
                year, month, day = map(int, date_match.groups())
                # The description is the part of the line before the date pattern
                description = line[:date_match.start()].split(' ', 4)[-1].strip()
                appointments.append(appointment_class(day, month,year, description))
            else:
                raise ValueError(f"Date format not found in line: {line}")

        return appointments


# For Onetime, Daily, and Monthly, use overriding
# The 'Onetime' class overrides the 'occursOn' method from the 'Appointment' 
# superclass and calls the superclass method to check for an exact date match.
#class Onetime(Appointment):
#    def occursOn(self, year, month, day):
#        # Call the superclass method to maintain the original behavior
#        return super().occursOn(year, month, day)
    
class Onetime(Appointment):
    "one time inherits from Appointment and requires a specific date."
    def __repr__(self):
        return "One time appointment {} {} {} {}".format(self._date[2], self._date[1], self._date[0], self._description)

    "The save method serialize a one time appointment details for saving to a file."
    def save(self, file):
        file.write(self.__repr__() + "\n")

# The 'Daily' class overrides the 'occursOn' method and always returns True, 
# indicating the appointment occurs every day, thus not needing to call the 
# superclass method.
#class Daily(Appointment):
#    def occursOn(self, year, month, day):
#        # Daily appointments occur every day, so we do not call the superclass method
#        return True
    
class Daily(Appointment):
    def occursOn(self, year, month, day):
        "a daily appointment inherits from Appointment and occurs every day."
        return True

    def __repr__(self):
        return "Daily time appointment starting {} {} {} {}".format(self._date[2], self._date[1], self._date[0], self._description)

    
    def save(self, file):
        "The save method serialize a daily appointment details for saving to a file."
        file.write(self.__repr__() + "\n")

# The 'Monthly' class overrides the 'occursOn' method to check if the day of the month matches
#class Monthly(Appointment):
#    def occursOn(self, year, month, day):
#        # Monthly appointments occur if the day of the month matches
#        return self._date[2] == day
    
class Monthly(Appointment):
    def occursOn(self, year, month, day):
        "Represents a monthly recurring appointment inherits from Appointment and occurs on the same day each month."
        return self._date[2] == day

    def __repr__(self):
        return "Monthly time appointment starting {} {} {} {}".format(self._date[2], self._date[1], self._date[0], self._description)

    def save(self, file):
        "The save method serialize a monthly appointment details for saving to a file."
        file.write(self.__repr__() + "\n")


def save_appointments(appointments, file_path):
    "Save all appointments to a file"
    with open(file_path, 'w') as file:
        for appointment in appointments:
            appointment.save(file)


def load_appointments(file_path):
    "# To load appointments from the file"
    with open(file_path, 'r') as file:
        return Appointment.load(file)

# Create a list of appointments with a different types
appointments = [
    Onetime("See the dentist", 2023, 11, 9),
    Daily("Daily appointment", 2023, 11, 10),
    Monthly("Monthly appointment", 2023, 11, 11)
]

# Save the appointments to a file
save_file_path = 'appointments.txt'
save_appointments(appointments, save_file_path)

# To load the appointments from the file
loaded_appointments = load_appointments(save_file_path)

print(loaded_appointments)

