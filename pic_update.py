# import required module
import os
from datetime import datetime, timedelta
from helpers.copy import copy_to_folder, change_extension
from helpers.delete_folder_files import delete_folder_files

basedir = os.path.dirname(__file__)

# assign directory
origin_folder = os.path.abspath("../" + 'PICTURES')
target_folder = os.path.abspath("../" + "PICTURES_JPEG_FORMAT")
#Change timedelta to chaange the number of days.
yesterday_date = datetime.today() - timedelta(days=1)
origin_folder_files = os.listdir(origin_folder)

file_modified_on_desired_date = False

for filename in origin_folder_files:
    file = os.path.join(origin_folder, filename)
    modify_date = datetime.fromtimestamp(os.path.getmtime(file))
    if modify_date >= yesterday_date:
        delete_folder_files(target_folder)
        copy_to_folder(origin_folder, target_folder)
        change_extension(target_folder)
        break