import csv
with open('camion.csv', 'rt') as f:
    rows = csv.reader(f)
    print('\nRows: \n', rows)

    headers = next(rows)
    print('\nHeaders: \n', headers)

    print('\nRows:')
    for row in rows:
        print(row)
