from output_handlers.csv import CsvStandardOutputHandler
from output_handlers.json import JsonStandardOutputHandler
from output_handlers.xml import XmlStandardOutputHandler


class BankDataWriter:
    def __init__(self, output_file_path):
        self.output_file_path = output_file_path

    def process_output(self, transactions, output_format):
        output_handler = self._get_output_handler(output_format)
        output_handler.process(transactions, self.output_file_path)

    def _get_output_handler(self, output_format):
        if output_format == "json":
            return JsonStandardOutputHandler()
        elif output_format == "xml":
            return XmlStandardOutputHandler()
        return CsvStandardOutputHandler()
