from pathlib import Path
import tabula
import re


class Step7DataBlockPdfReportImport():
    def __init__(self, reports_directory):
        self.var_dict = dict()
        pathlist = Path(reports_directory).rglob('*.pdf')
        for path in pathlist:
            # because path is object not string
            path_in_str = str(path)
            self.tables = tabula.read_pdf(path_in_str, pages='all')

            if len(self.tables) >= 2:

                datablock_number = int(re.findall("(^DB)([0-9]+)", self.tables[0].columns[0])[0][1]) # First column name is datablock number

                self.tables.pop(0) # remove table with index 0, rest of tables are variables

                for i, df in enumerate(self.tables):
                    self.tables[i]['Name'] = self.tables[i]['Name'].str.replace('\r', '')  # Izbriše control characters iz "name"

                for i, df in enumerate(self.tables):
                    for index, row in df.iterrows():
                        entry = {row['Name'] : {'DB': datablock_number, 'var_name': row['Name'], 'var_type': row['Type'], 'Address': row['Address']}}
                        self.var_dict.update(entry)
            else:
                print('No table at {}'.format(path_in_str))