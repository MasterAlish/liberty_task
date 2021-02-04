import argparse

from unifier.reader import BankDataReader
from unifier.writer import BankDataWriter


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', default="data", metavar="/path/to/data", help='bank data directory')
    parser.add_argument('--format', default="csv", choices=["xml", "json", "csv"], help='output format')
    parser.add_argument('--output', default=None, help='output file')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    data_dir = args.data
    output_format = args.format
    output_file = args.output or "unified_bank_data." + output_format

    data_reader = BankDataReader(data_dir)
    transactions = data_reader.read_transactions()

    data_writer = BankDataWriter(output_file)
    data_writer.process_output(transactions, output_format)

