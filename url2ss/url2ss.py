# coding:utf-8
import csv
import os
import subprocess
import sys

from datetime import datetime, date
from selenium import webdriver
from time import sleep

csv_file_name = ''

args = sys.argv
if (len(args) == 1):
  print('urs2element.py <csv file name>')
  quit()

if (len(args) == 2):
  csv_file_name = args[1]

if (os.path.isfile(csv_file_name) == False):
  print('CSV ファイルが存在しません')
  quit()

save_folder     = os.getcwd() + '\\' + datetime.now().strftime("%Y%m%d%H%M%S")
save_folder_pc  = save_folder + '\\pc'
save_folder_sp  = save_folder + '\\sp'

os.mkdir(save_folder)
os.mkdir(save_folder_pc)
os.mkdir(save_folder_sp)

def cap(pId, pURL):
    # URL を開く
    driver.get(pURL)
    # キャプチャー実行
    cap_pc(pId, pURL)
    cap_sp(pId, pURL)
    # 1秒待機
    sleep(1)

def cap_pc(pId, pURL):
    driver.set_window_size(1024,1000)
    iw = driver.execute_script("return document.body.clientWidth;")
    ih = driver.execute_script("return document.body.clientHeight;")
    cmd = '"c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --headless --disable-gpu --hide-scrollbars --screenshot=' + save_folder_pc + '\\' + pId + '.png --window-size=' + str(iw) + ',' + str(ih) + ' ' + pURL
    subprocess.Popen(cmd, shell=True)

def cap_sp(pId, pURL):
    driver.set_window_size(600,1000)
    iw = driver.execute_script("return document.body.clientWidth;")
    ih = driver.execute_script("return document.body.clientHeight;")
    cmd = '"c:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" --headless --disable-gpu --hide-scrollbars --screenshot=' + save_folder_sp + '\\' + pId + '.png --window-size=' + str(iw) + ',' + str(ih) + ' ' + pURL
    subprocess.Popen(cmd, shell=True)

driver = webdriver.Chrome()

with open(csv_file_name, 'r') as f:
    reader = csv.reader(f)
    # header = next(reader)
    if (reader != ''):
        for row in reader:
            print(row[0] + ' : ' + row[1])
            cap(row[0], row[1])

driver.quit()
quit()
