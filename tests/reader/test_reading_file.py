from datetime import date
from decimal import Decimal
from unittest import TestCase

from unifier.reader import BankDataReader


class BankDataReaderFileConfigTestCase(TestCase):
    def test_transactions_file_read_correctly_for_bank1(self):
        reader = BankDataReader("tests/test_data")
        bank1_config = {
            "has_header": True,
            "columns_order": ["created_date", "type", "amount", "source", "destination"],
            "date_format": "%b %d %Y"
        }
        transactions = reader.read_transactions()

        self.assertEqual(len(transactions), 3)

        newer_transaction = transactions[-1]  # Sep 12 2019,add,122.10,170,198

        self.assertEqual(newer_transaction.created_date, date(2019, 9, 12))
        self.assertEqual(newer_transaction.type, "add")
        self.assertEqual(newer_transaction.amount, Decimal("122.10"))
        self.assertEqual(newer_transaction.source, 170)
        self.assertEqual(newer_transaction.destination, 198)
