import os
import openpyxl as px
from openpyxl.drawing.image import Image
from datetime import datetime, date

def cap(src, dst):
    wb = px.Workbook()
    ws = wb.active
    img = Image(src)
    ws.add_image(img, 'A1')
    wb.save(dst)

src_folder = os.getcwd() + '\\'
dst_folder = os.getcwd() + '\\' + datetime.now().strftime("%Y%m%d%H%M%S") + '\\'

os.mkdir(dst_folder)

src_files = os.listdir(src_folder)
print(src_files)
for src_file in src_files:
    if os.path.isfile(src_folder + src_file):
        name, ext = os.path.splitext(os.path.basename(src_file))
        if ext in {'.jpg', '.png'}:
            cap(src_folder + name + ext, dst_folder + name + '.xlsx')
