class PostOffice:
    def __init__(self, received_letter, dispatched_letter):
        self.received_letter = received_letter
        self.dispatched_letter = dispatched_letter

    def receive_letter(self, received_letter):
        if received_letter is False:
            received_letter = True
            print("The letter has been received at the post office.")
            return received_letter

    def dispatch_letter(self, dispatched_letter):
        if dispatched_letter is False:
            dispatched_letter = True
            print("The letter has been dispatched from the post office.")