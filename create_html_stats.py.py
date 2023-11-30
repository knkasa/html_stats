#======================================================
# Run as follow:
# python create_html.py -d <csv file> -c <txt file>
# python create_html.py --csv_data=<csv file> 
#======================================================

import pandas as pd
import numpy as np
import os
import pdb
import sys
from dotenv import load_dotenv
from typing import List
import sweetviz as sv

# sweetviz==2.2.1 is confirmed to be working.

class html_class:
    def __init__(self, csv_file:str, col_list:List[str]=None):
        self.csv_file = csv_file
        self.col_list = col_list

    def get_html(self) -> None:
        '''Run sweetviz to create html file. '''

        try:
            try:
		df = pd.read_csv(self.csv_file, encoding='Shift-Jis')
	    except UnicodeDecodeError:
		df = pd.read_csv(self.csv_file, encoding='UTF-8')

	    sv.config_parser.read_string("[General]\nuse_cjk_font=1")
	    if self.col_list is not None:
		report = sv.analyze(df[self.col_list])
	    else:
		report = sv.analyze(df)
	    report.show_html("stats.html")
	except Exception as e:
	    raise Exception(e)

def main():

    options, _ = getopt.getopt(sys.argv[1:], 'd:c:', ['csv_data=', 'column_txt='])

    col_list = None
    for n, opt in enumerate(options):
	if opt[0]=='--csv_data' or opt[0]=='-d':
	    csv_file = opt[1]
	elif opt[0]=='--column_txt' or opt[0]=='-c':
	    with open(opt[1], 'r') as file:
		for line in file:
		    col_list.append(line.strip())

    try:
	print(f"csv file = {csv_file}")
    except NameError as e:
	raise Exception("No csv file found. Exiting...")

    if col_list is not None:
	col_list = [item for item in col_list if item] # Remove empty strings.

    html_creator = html_class(csv_file, col_list)
    html_creator.get_html()

if __name__=="__main__":
    main()

