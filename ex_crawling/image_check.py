import os
img_dir ="./범고래"
for filename in os.listdir(img_dir):
    file_path =os.path.join(img_dir, filename)
    if os.path.isfile(file_path):
        file_size =os.path.getsize(file_path)
        print(file_size ,file_path)
        if file_size <1024:
            print('delete file:', file_size ,file_path)
            os.remove(file_path)
