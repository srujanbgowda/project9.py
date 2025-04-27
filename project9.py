import os
import shutil

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return
    
    file_types = {
        "Images": [".jpg", ".png", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar", ".7z"]
    }
    
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    folder_path_new = os.path.join(folder_path, folder)
                    os.makedirs(folder_path_new, exist_ok=True)
                    shutil.move(file_path, folder_path_new)
                    moved = True
                    break
            if not moved:
                others_path = os.path.join(folder_path, "Others")
                os.makedirs(others_path, exist_ok=True)
                shutil.move(file_path, others_path)

folder_input = input("Enter the path of the folder to organize: ")
organize_folder(folder_input)




