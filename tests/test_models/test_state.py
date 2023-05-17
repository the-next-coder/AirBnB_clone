#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


<<<<<<< HEAD
class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
=======
class TestBaseModel(unittest.TestCase):


    def test_attr(self):
        state = State()
        self.assertEqual(state.name, "")


    def test_parent(self):
        state = State()
        self.assertTrue(isinstance(state, BaseModel))
>>>>>>> 73a076deabdb66313857081f333973f27192cb3f
