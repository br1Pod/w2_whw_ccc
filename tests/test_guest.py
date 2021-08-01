import unittest

from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
            # sample rooms
        self.room1 = Room("Compton Crib", 20, 0, "Hip Hop")
        self.room2 = Room("Soul Shack", 20, 0, "Soul")
        self.room3 = Room("Nashville Nook", 20, 0, "Country")
        self.room4 = Room("Pop Pad", 20, 0, "Chart")
        self.room5 = Room("School of Rock", 20, 0, "Rock")

        # sample guests
        self.guest1 = Guest("Lil T", 23, 40, "Hip Hop")
        self.guest2 = Guest("Martha Vandell", 30, 25, "Soul")
        self.guest3 = Guest("Waylon Walton", 28, 30, "Country")
        self.guest4 = Guest("Ezra Sheerin", 18, 20, "Chart")
        self.guest5 = Guest("Dave Roadie", 27, 30, "Rock")
        self.guest6 = Guest("Suzi Quintro", 33, 35, "Rock")
        self.guest7 = Guest("Adele Clarkson ", 23, 30, "Chart")
        self.guest8 = Guest("Carla Jean", 21, 25, "Country")
        self.guest9 = Guest("Stan Cooke", 43, 40, "Soul")
        self.guest10 = Guest("Tanisha Ordell", 19, 35, "Hip Hop")

        #sample songs
        self.song1 = Song("Poundin 40s", "Crenshaw Cru", "Hip Hop")
        self.song2 = Song("Shawty Shake", "Doctah Dolla", "Hip Hop")
        self.song3 = Song("Cryin an Drinkin", "Marv N", "Soul")
        self.song4 = Song("Code Blue", "Shelly Lavelley", "Soul")
        self.song5 = Song("Your Cheatin Horse", "Harvest Hogs", "Country")
        self.song6 = Song("Trailer Hoedown", "The Hogfather", "Country")
        self.song7 = Song("Black Nails", "Jane's Jetts", "Rock")
        self.song8 = Song("Eye of the Python", "SnakeLake", "Rock")
        self.song9 = Song("Love Simp", "Nick Dastly", "Chart")
        self.song10 = Song("Girl don't hate me", "Hairgelled Hearthrobs", "Chart")


    # Tests

    def test_guest_has_name(self):
        self.assertEqual("Martha Vandell", self.guest2.name)