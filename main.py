import csv
import re
import sys


DISTRICTS = {
    # range of district codes that are in each region (inclusive)
    'South': [(1, 10), (14, 27)],
    'West': [(11, 13), (58, 71)],
    'Central': [(28, 33), (56, 57), (77, 78)],
    'East': [(34, 55), (81, 82)],
    'North': [(72, 73), (75, 76), (79, 80)],
}


def get_area(code):
    prefix = int(code[:2])

    for k, v in DISTRICTS.items():
        for i in v:
            if i[0] <= prefix <= i[1]:
                return k

    raise ValueError('Invalid postal code')


def parse_address(address):
    """Returns an iterator of Tuple[code, area] from an address parsed from the postal codes"""
    postal_codes = re.findall(r'(?:(?<= )|^)\d{6}(?:(?= )|$)', address, flags=re.MULTILINE)

    for code in postal_codes:
        yield code, get_area(code)


def main(args):
    file_path = None
    address = None
    if len(args) > 1:
        # argument is a filepath
        file_path = ' '.join(sys.argv[1:])
        if file_path.endswith('.csv'):
            with open(file_path, encoding='utf8') as f:
                data = list(csv.DictReader(f))

            for i in data:
                i['area'] = ':'.join(x[1] for x in parse_address(i['address']))

            new_fp = file_path[:-4] + '-parsed.csv'
            with open(new_fp, 'w', newline='', encoding='utf8') as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

            print('Created', new_fp)
        else:
            file_path = None
            address = ' '.join(sys.argv[1:])

    if file_path is None:
        if address is None:
            address = input('postal code: ')


        for code, area in parse_address(address):
            print(code, area)


if __name__ == '__main__':
    main(sys.argv)
