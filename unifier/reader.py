import csv
from datetime import datetime
import os
from decimal import Decimal

from unifier import settings
from entities.transaction import Transaction


class BankDataReader:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def read_transactions(self):
        transactions = self._collect_transactions()
        return sorted(transactions, key=lambda t: t.created_date)

    def _collect_transactions(self):
        all_transactions = []
        for data_file_name in os.listdir(self.data_dir):
            file_path = os.path.join(self.data_dir, data_file_name)

            with open(file_path) as csv_file:
                config_name = self._get_config_name_by_file_name(data_file_name)
                config = self._load_config(config_name)
                if config:
                    transactions = self._process_data_file(csv_file, config)
                    all_transactions.extend(transactions)
        return all_transactions

    def _process_data_file(self, csv_file, config: dict):
        reader = csv.reader(csv_file)
        header_skipped = not config.get("has_header", True)
        transactions = []
        for row in reader:
            if not header_skipped:
                header_skipped = True
                continue
            transaction = self._parse_transaction_row(row, config)
            transactions.append(transaction)
        return transactions

    def _parse_transaction_row(self, values, config):
        columns = config["columns_order"]
        date_format = config["date_format"]
        transaction = Transaction()
        for index, name in enumerate(columns):
            value = values[index]
            if name == "created_date":
                transaction.created_date = datetime.strptime(value, date_format).date()
            if name == "type":
                transaction.type = value
            if name == "amount":
                transaction.amount = Decimal(value)
            if name == "amount_hundredth":
                transaction.amount += Decimal(value) / Decimal(100.0)
            if name == "source":
                transaction.source = int(value)
            if name == "destination":
                transaction.destination = int(value)
        return transaction

    def _get_config_name_by_file_name(self, data_file_name):
        file_name_parts = os.path.splitext(data_file_name)
        file_name = file_name_parts[0]
        return file_name

    def _load_config(self, config_name):
        if config_name in settings.BANK_CSV_CONFIGS:
            return settings.BANK_CSV_CONFIGS[config_name]
        return None
