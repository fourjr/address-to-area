# Singapore Address to Area (NSEW)

Extracts postal codes from addresses and uses [district codes](https://www.ura.gov.sg/realEstateIIWeb/resources/misc/list_of_postal_districts.htm) to determine the approximate area of a postal code.

## Usage
- Call `python main.py` and follow prompts.
- Call `python main.py [address]`. The script will output an area.
- Call `python main.py [filepath.csv]` with a csv containing an `address` column. The script will parse the CSV and output a new CSV with a `area` column.

Addresses can have multiple postal codes. The script will then combine them with colons.
