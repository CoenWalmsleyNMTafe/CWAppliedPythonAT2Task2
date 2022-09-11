from letter import Letter


class Person:
    def __init__(self, name, writing, sending, reading, retrieving):
        self.name = name
        self.writing = writing
        self.sending = sending
        self.reading = reading
        self.retrieving = retrieving

    def read_letter(self, name, reading):
        if reading is False:
            reading = True
            print(f"{name} is reading letter.")
            return reading

        else:
            reading = False
            Letter.is_read = False
            return reading

    def write_letter(self, name, writing):
        if writing is False:
            writing = True
            print(f"{name} is writing letter.")
            Letter.is_written = True
            return writing
        else:
            writing = False
            Letter.is_written = False
            return writing

    def send_letter(self, name, sending):
        if sending is False:
            sending = True
            print(f"{name} is sending letter.")
            Letter.is_sent = True
            return sending
        else:
            sending = False
            Letter.is_sent = False
            return sending

    def retrieve_letter(self, name, retrieving):
        if retrieving is False:
            retrieving = True
            print(f"{name} is retrieving letter from letterbox.")
            return retrieving
        else:
            retrieving = False
            return retrieving

    def check_letterbox(self, name, flag_up):
        if flag_up is True:
            print(f"{name}, check your letterbox.")
