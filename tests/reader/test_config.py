from unittest import TestCase

from unifier.reader import BankDataReader


class BankDataReaderConfigTestCase(TestCase):
    def test_config_name_gains_correctly(self):
        reader = BankDataReader("tests/test_data")

        self.assertEqual(reader._get_config_name_by_file_name("bank1.csv"), "bank1")
        self.assertEqual(reader._get_config_name_by_file_name("bank2.csv"), "bank2")
        self.assertEqual(reader._get_config_name_by_file_name("state_bank.csv"), "state_bank")
