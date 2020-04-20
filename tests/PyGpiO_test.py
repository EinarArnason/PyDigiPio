import unittest
import PyGpiO


class TestGpio(unittest.TestCase):

    def test_write(self):
        PyGpiO.configure_pin(21, "out")
        PyGpiO.write_to_pin(21, True)
        self.assertTrue(PyGpiO.read_from_pin(21), True)
        PyGpiO.write_to_pin(21, False)


if __name__ == '__main__':
    unittest.main()
