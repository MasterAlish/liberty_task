from typing import Iterable

from entities.transaction import Transaction
from unifier import settings


class BaseOutputHandler:
    output_date_format = settings.OUTPUT_DATE_FORMAT

    def process(self, transactions: Iterable[Transaction], output_file_path):
        pass
