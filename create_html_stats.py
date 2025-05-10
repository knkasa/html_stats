# -*- coding: utf-8 -*-

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
import yaml
import time
from loguru import logger
import getopt  # you could also use argparse library.
from typing import List
import sweetviz as sv
import functools
from diskcache import Cache

# sweetviz==2.2.1 is confirmed to be working.
cache = Cache('/tmp/expensive_cache')

class html_class:
    __slots__ = ['csv_file', 'col_list']
    def __init__(self, csv_file:str, col_list:List[str]=None):
        self.csv_file = csv_file
        self.col_list = col_list

    def __str__(self):
	return f"Attribute vars: {self.csv_file}, {self.col_list}

    @functools.lru_cache()
    @conditional_decorator(condition=True)
    def get_html(self) -> None:
        '''
	Run sweetviz to create html file. 
        Parameters:
	a(int): explanation.
        b(float): explanation.
	Returns:
        int: explanation.

        Example:
	>>> get_html(a,b)
        12
　　    '''

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
	    logger.exception(f"Error at get_html(): {e}")
	    raise Exception(e)

    @static_method
    def conditional_decorator(condition):
	def decorator(func):
	    if condition:
		return func
	    else:
		def wrapper(*args, **kwargs):
		    return func(*args, **kwargs)
		return wrapper if func else None
	return decorator

class loguru_class():
    def __init__(self,):
	if not os.path.exitsts('log'):
	    os.makedir('log')
	logger.add(
	    f"./log/monitoring_{datetime.now().strftime(%Y%m%d-%H%M%S')}.log",
	    rotaion="1000MB",
	    level="INFO", #"DEBUG"
	    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name} | {message}"  # {level: <8} means put 8 spaces after the level text.

def main():

    from pathlib import Path
    system_path = Path('__file__').resolve().parent
    
    loguru_engine = loguru_class()

    with open('setting.yaml', 'r') as yml:
	settings = yaml.save_load(yml)
	
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
	logger.info(f"csv file = {csv_file}")
    except NameError as e:
	raise Exception("No csv file found. Exiting...")

    if col_list is not None:
	col_list = [item for item in col_list if item] # Remove empty strings.

    encoding_options = ['Shift-JIS','UTF-8']
    for encoding in encoding_options:
	try:
	    load_dotenv(encoding=encoding, verbose=True)
	    logger.debug(f"The following encoding worked. {encoding}")
	    break
	except UnicodeDecodeError:
	    raise Exception("Loading .env failed.  Try different encoding.")

    time1 = time.perf_counter()
    html_creator = html_class(csv_file, col_list)
    html_creator.get_html()
    logger.info(f"Time elapsed: {(time.perf_counter()-time1):.1f}sec.")

if __name__=="__main__":
    main()

