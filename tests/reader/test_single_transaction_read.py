from datetime import date
from decimal import Decimal
from unittest import TestCase

from unifier.reader import BankDataReader


class BankDataReaderTransactionTestCase(TestCase):
    def test_transaction_parsed_correctly_for_bank1(self):
        reader = BankDataReader("tests/test_data")
        bank1_config = {
            "has_header": True,
            "columns_order": ["created_date", "type", "amount", "source", "destination"],
            "date_format": "%b %d %Y"
        }
        transaction = reader._parse_transaction_row(["Oct 1 2019", "remove", "99.20", "198", "182"], bank1_config)
        self.assertEqual(transaction.created_date, date(2019, 10, 1))
        self.assertEqual(transaction.type, "remove")
        self.assertEqual(transaction.amount, Decimal("99.20"))
        self.assertEqual(transaction.source, 198)
        self.assertEqual(transaction.destination, 182)

    def test_transaction_parsed_correctly_for_bank3(self):
        reader = BankDataReader("tests/test_data")
        bank3_config = {
            "has_header": True,
            "columns_order": ["created_date", "type", "amount", "amount_hundredth", "destination", "source"],
            "date_format": "%d %b %Y"
        }
        transaction = reader._parse_transaction_row(["6 Oct 2019", "add", "1060", "8", "198", "188"], bank3_config)
        self.assertEqual(transaction.created_date, date(2019, 10, 6))
        self.assertEqual(transaction.type, "add")
        self.assertEqual(transaction.amount, Decimal("1060.08"))
        self.assertEqual(transaction.source, 188)
        self.assertEqual(transaction.destination, 198)

    def test_transaction_parsed_correctly_3(self):
        reader = BankDataReader("tests/test_data")
        config = {
            "has_header": True,
            "columns_order": ["type", "amount", "destination", "source", "created_date"],
            "date_format": "%d.%m.%Y"
        }
        transaction = reader._parse_transaction_row(["add", "999.99", "100", "101", "31.01.2021"], config)
        self.assertEqual(transaction.created_date, date(2021, 1, 31))
        self.assertEqual(transaction.type, "add")
        self.assertEqual(transaction.amount, Decimal("999.99"))
        self.assertEqual(transaction.source, 101)
        self.assertEqual(transaction.destination, 100)
