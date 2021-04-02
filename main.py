import pandas as pd
import numpy as numpy
import os

excel_files_folder = 'excel_files'

archivos = os.listdir(excel_files_folder)
results = pd.DataFrame()

for archivo in archivos:
    excel_file = excel_files_folder + '\\' + archivo
    df = pd.read_excel(excel_file)
    results = pd.concat([results,df],ignore_index = True)

results.to_excel(excel_files_folder + '\\merge.xlsx', sheet_name='Merged', index = False)

print(results)


