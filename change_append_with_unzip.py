import os
import zipfile
if __name__ == '__main__':
    # 指定要遍历的目录路径
    choose_dir = input('输入目录: ')  # 各种动漫角色在这里！！！
    use_append = input("输入待删除后缀(默认:'删我'): ") or '删我'
    current_dir = os.getcwd()
    use_dir = os.path.join(current_dir,choose_dir)

    # 第一遍改名
    for root, dirs, files in os.walk(use_dir):
        for file in files:
            # 输出文件路径
            if file.endswith(use_append):
                new_file = file.rstrip(use_append)
                ori_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                print("rename {}  to  {}".format(ori_path, new_path))
                os.rename(ori_path, new_path)

    # 第二遍解压并删除
    for root, dirs, files in os.walk(use_dir):
        # 首先检测三个文件能否解压(之后有004也不影响,这里表示至少有001,002,003)
        unzip_flag_1,unzip_flag_2,unzip_flag_3 = False,False,False
        for file in files:
            if file.endswith('.zip.001'):
                unzip_flag_1 = True
            if file.endswith('.zip.002'):
                unzip_flag_2 = True
            if file.endswith('.zip.003'):
                unzip_flag_3 = True
        unzip_flag = unzip_flag_1 and unzip_flag_2 and unzip_flag_3

        if unzip_flag: # 如果满足解压条件
            zip_files = [os.path.join(root, file) for file in files]
            print('Unzip step1:combine ',files)
            # 创建一个合并的zip文件
            with open('cache.zip', 'wb') as combined_zip:
                for zip_file in zip_files:
                    with open(zip_file, 'rb') as part:
                        combined_zip.write(part.read())
            # 解压合并后的zip文件
            print('Unzip step2: unzip')
            with zipfile.ZipFile('cache.zip', 'r') as zip_ref:
                for file_info in zip_ref.infolist():
                    try:
                        file_info.filename = file_info.filename.encode('cp437').decode('gbk')
                    except UnicodeDecodeError:
                        file_info.filename = file_info.filename.encode('cp437').decode('gbk', errors='replace')
                    zip_ref.extract(file_info,root)
            # 删除文件
            print('Unzip step2:remove cache zip files')
            os.remove('cache.zip')
            for zip_file in zip_files:
                os.remove(zip_file)






