import unittest
from Konfiguration.konfigurationsdatei import Initial

class MyTestCase(unittest.TestCase):
    def test_load_config_negativ(self):
        init = Initial()
        self.assertFalse(init.load(filename='dfr.ini'))
        del(init)

    def test_load_config_positiv(self):
        init2 = Initial()
        config_file = '/Users/marcomeo/PycharmProjects/schulungPython/Konfiguration/config.ini'
        print(config_file)
        self.assertIsNotNone(init2.load(filename=config_file))
        self.assertEqual(init2.loglevel, 'DEBUG')
        del(init2)


if __name__ == '__main__':
    unittest.main()
