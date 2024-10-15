import os

def Test():
    for root, dirs, files in os.walk(folder):
        print(root, dirs, files)
        if name in files:
            file_path = os.path.join(root, name)
            print(f"찾았습니다 : {name}")
            print(f"{file_path}")
            return
    else:
        print("파일을 찾을 수 없습니다")


root = "C:\\"
folder = input("탐색을 원하시는 경로를 입력해 주세요")
print(folder)

file_list = os.listdir(folder)
print(file_list)
name = input("찾으시고자 하는 파일의 이름을 입력해 주세요")
Test()