class Letter:
    def __init__(self, is_written, is_sent, is_read, is_encrypted):
        self.is_written = is_written
        self.is_sent = is_sent
        self.is_read = is_read
        self.is_encrypted = is_encrypted

    def mark_as_read(self, is_read):
        if is_read is False:
            is_read = True
            print("Letter is read.")
            return is_read
