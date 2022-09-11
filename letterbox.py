class Letterbox:
    def __init__(self, flag_up):
        self.flag_up = flag_up

    def receive_letter(self, flag_up):
        if flag_up is False:
            flag_up = True
            print("The letterbox flag has been raised.")
            return flag_up
