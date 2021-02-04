import json
from typing import Iterable

from entities.transaction import Transaction
from output_handlers.base import BaseOutputHandler


class JsonStandardOutputHandler(BaseOutputHandler):
    def process(self, transactions: Iterable[Transaction], output_file_path):
        with open(output_file_path, "w") as json_file:
            data = [{
                "created_date": transaction.created_date.strftime(self.output_date_format),
                "type": transaction.type,
                "amount": "{:.2f}".format(transaction.amount),
                "source": transaction.source,
                "destination": transaction.destination
            } for transaction in transactions]

            json.dump(data, json_file)
