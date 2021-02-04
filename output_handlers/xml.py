from typing import Iterable
import xml.etree.ElementTree as ET

from entities.transaction import Transaction
from output_handlers.base import BaseOutputHandler


class XmlStandardOutputHandler(BaseOutputHandler):
    def process(self, transactions: Iterable[Transaction], output_file_path):
        with open(output_file_path, "w") as xml_file:
            root = ET.Element('transactions')

            for transaction in transactions:
                item = ET.SubElement(root, 'item')
                item.set('created_date', transaction.created_date.strftime(self.output_date_format))
                item.set('type', transaction.type)
                item.set('amount', "{:.2f}".format(transaction.amount))
                item.set('source', str(transaction.source))
                item.set('destination', str(transaction.destination))

            xml_data = ET.tostring(root)
            xml_file.write(xml_data.decode("utf-8"))
