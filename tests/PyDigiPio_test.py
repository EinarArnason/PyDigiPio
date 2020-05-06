import unittest
import PyDigiPio


class TestGpio(unittest.TestCase):

    def test_write(self):
        PyDigiPio.configure_pin(21, "out")
        PyDigiPio.write_to_pin(21, True)
        self.assertTrue(PyDigiPio.read_from_pin(21), True)
        PyDigiPio.write_to_pin(21, False)


if __name__ == '__main__':
    unittest.main()
