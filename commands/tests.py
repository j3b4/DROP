# DROP/commands/tests.py

import unittest


class TestString(unittest.TestCase):

    """Unittest for strings (just a basic example.)"""

    def test_upper(self):
        """Test the upper() str method."""
        self.assertEqual('foo'.upper(), 'FOO')


# Let's try more. This is the tutorial unit test to test in game commands
"""
    We are testing CmdAbilities first. We also need to import the 
    Character typeclass in order to test the command as used by an actual 
    character in the game.
"""

from evennia.commands.default.tests import CommandTest

from commands.command import CmdAbilities
from typeclasses.characters import Character

class TestAbilities(CommandTest):

    character_typeclass = Character

    def test_simple(self):
        self.call(CmdAbilities(), "", "STR: 0, INT: 0, WIS: 0, DEX: 0, CON: 0, CHA: 0")

