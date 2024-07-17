import os

if __name__ == '__main__':
    # 指定要遍历的目录路径
    choose_dir = input('输入目录: ')  # 星穹铁道
    use_append = input("输入待删除后缀(默认:'删我'): ") or '删我'
    current_dir = os.getcwd()
    use_dir = os.path.join(current_dir,choose_dir)

    file_list = os.walk(use_dir)
    for root, dirs, files in file_list:
        for file in files:
            # 输出文件路径
            if file.endswith(use_append):
                new_file = file.rstrip(use_append)
                ori_path = os.path.join(root, file)
                new_path = os.path.join(root, new_file)
                print("rename {} >to> {}".format(ori_path, new_path))
                os.rename(ori_path, new_path)

