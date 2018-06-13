import os
import openpyxl as px
from openpyxl.drawing.image import Image
from datetime import datetime, date

def cap(src_folder, dst_folder, name, ext):
    wb = px.Workbook()
    ws = wb.active
    img = Image(src_folder + name + ext)
    ws['A1'].value = name
    ws.add_image(img, 'A2')
    wb.save(dst_folder + name + '.xlsx')

src_folder = os.getcwd() + '\\'
dst_folder = os.getcwd() + '\\' + datetime.now().strftime("%Y%m%d%H%M%S") + '\\'

os.mkdir(dst_folder)

src_files = os.listdir(src_folder)
for src_file in src_files:
    if os.path.isfile(src_folder + src_file):
        name, ext = os.path.splitext(os.path.basename(src_file))
        if ext in {'.jpg', '.png'}:
            cap(src_folder, dst_folder, name, ext)
