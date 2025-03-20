import os
import shutil

basedir = os.path.dirname(__file__)

"""
    The function `copy_to_folder` copies all files from the `origin_folder` to the `target_folder`,
    excluding files with the extension ".jpg".

    :param origin_folder: The origin_folder parameter is the path to the folder from which you want to
    copy files. It should be a string representing the directory path
    :param target_folder: The target_folder parameter is the destination folder where the files will be
    copied to
"""
def copy_to_folder(origin_folder, target_folder):
    for filename in os.listdir(origin_folder):
        file = os.path.join(origin_folder, filename)
        
        # checking if it is a file
        if os.path.isfile(file):
            if filename.endswith(".jpg"):
                 continue
            else:
                shutil.copy(os.path.join(origin_folder, filename), os.path.join(target_folder, filename))

"""
    The function `change_extension` renames all files in a given folder by removing the dot in the
    filename and adding the extension ".jpg".
    
    :param target_folder: The target_folder parameter is the path to the folder where the files are
    located
"""
def change_extension(target_folder):
    for filename in os.listdir(target_folder):
        file = filename.replace(".", "")       
        dst = f"{file}"
        dst = dst[1:]
        src = os.path.join(target_folder, filename)
        dst = os.path.join(target_folder, dst)
        try:
            os.rename(src, dst + '.jpg')
        except:
            pass