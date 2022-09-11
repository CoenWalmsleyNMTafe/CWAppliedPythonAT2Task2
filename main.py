from person import Person
from letter import Letter
from letterbox import Letterbox

bob_letterbox = Letterbox(False)
alice_letterbox = Letterbox(False)
alice = Person("Alice", False, False, False, False)
bob = Person("Bob", False, False, False, False)

bob.write_letter(bob.name, bob.writing)
bob.send_letter(bob.name, bob.sending)
Letterbox.receive_letter(alice_letterbox, False)
alice.check_letterbox(alice.name, True)
alice.retrieve_letter(alice.name, alice.retrieving)
alice.read_letter(alice.name, alice.reading)
Letter.mark_as_read(alice, False)
