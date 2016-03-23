import csv, os
from glob import glob
from xlsxwriter.workbook import Workbook

for csvfile in glob('csvFiles/*.csv'):

    name = os.path.basename(csvfile).split('.')[-2]
    workbook = Workbook('xlsxFiles/' + str(name) + '.xlsx', {'strings_to_numbers': True, 'constant_memory': True})
    worksheet = workbook.add_worksheet()

    with open(csvfile, 'r') as f:
        r = csv.reader(f)
        for row_index, row in enumerate(r):
            for col_index, data in enumerate(row):
                worksheet.write(row_index, col_index, data)
    workbook.close()

print("-------------------------------------------")
print("   .CSV to .XLSX Conversion Successful")
print("-------------------------------------------")
