from person import Person
from letter import Letter
from letterbox import Letterbox
from postoffice import PostOffice

bob_letterbox = Letterbox(False)
alice_letterbox = Letterbox(False)
postoffice = PostOffice(False, False)
alice = Person("Alice", False, False, False, False, False, False, False)
bob = Person("Bob", False, False, False, False, False, False, False)
charli = Person("Charli", False, False, False, False, False, False, False)

def main():
    bob.write_letter(bob.name, bob.writing)
    bob.encrypt_letter(bob.name, bob.encrypting)
    bob.send_letter(bob.name, bob.sending)
    PostOffice.receive_letter(postoffice, False)
    PostOffice.dispatch_letter(postoffice, False)
    charli.deliver_letter(charli.name, False)
    Letterbox.receive_letter(alice_letterbox, False)
    alice.check_letterbox(alice.name, True)
    alice.retrieve_letter(alice.name, alice.retrieving)
    alice.decrypt_letter(alice.name, alice.decrypting)
    alice.read_letter(alice.name, alice.reading)
    Letter.mark_as_read(alice, False)

if __name__ == '__main__':
    main()
