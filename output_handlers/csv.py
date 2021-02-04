from typing import Iterable
import csv

from entities.transaction import Transaction
from output_handlers.base import BaseOutputHandler


class CsvStandardOutputHandler(BaseOutputHandler):
    def process(self, transactions: Iterable[Transaction], output_file_path):
        with open(output_file_path, "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow(['created_date', 'type', 'amount', 'source', 'destination'])

            for transaction in transactions:
                csv_writer.writerow([
                    transaction.created_date.strftime(self.output_date_format),
                    transaction.type,
                    "{:.2f}".format(transaction.amount),
                    transaction.source,
                    transaction.destination
                ])
