import os
#Delete all files in the directory
def delete_folder_files(target_folder):
    for filename in os.listdir(target_folder):
        os.remove(os.path.join(target_folder, filename))