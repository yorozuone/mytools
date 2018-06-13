# coding:utf-8
import csv
import os
import sys

from selenium import webdriver
from time import sleep

csv_file_name = ''

args = sys.argv
if (len(args) == 1):
  print('urs2ss.py <csv file name>')
  quit()

if (len(args) == 2):
  csv_file_name = args[1]

if (os.path.isfile(csv_file_name) == False):
  print('CSV ファイルが存在しません')
  quit()

driver = webdriver.Chrome()

with open(csv_file_name, 'r') as f:
    reader = csv.reader(f)
    # header = next(reader)
    if (reader != ''):
        for row in reader:
            if (len(row) == 0):
                print('<none>')
            else:
                csv_url = row[0]
                #
                driver.get(csv_url)
                ret_js = "return document.title;"
                # ret_js = "return document.getElementsByName ('description').item(0).content;"
                try:
                    ret_value = driver.execute_script(ret_js)
                except:
                    ret_value = '(none)'
                print(str(ret_value))
            sleep(1)

driver.quit()
quit()



