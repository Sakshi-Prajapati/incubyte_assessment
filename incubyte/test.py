import unittest
import Input

class TestClass(unittest.TestCase):

    def types(self):
        # self.a = Input.Inputs.x
        # self.b = Input.Inputs.y
        # self.c = Input.Inputs.Z
        #
        # self.assertEqual(type(self.a), int)
        # self.assertEqual(type(self.b), int)
        # self.assertEqual(type(self.c), int)
        f_x = Input.Inputs.types(Input.Inputs.x)
        self.assertEquals(type(f_x),int)


