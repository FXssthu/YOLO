""" 作用:删除指定文件夹下所有指定后缀名的文件
参数列表:
folder_path: 文件夹路径
file_extension: 文件后缀名
注意: 
      1.该脚本仅删除文件，不会递归删除文件夹
      2.删除是永久性的，不可恢复，请谨慎操作
"""
import os
def delete_files_with_extension(folder_path, file_extension):
    # 确保文件夹路径是绝对路径
    folder_path = os.path.abspath(folder_path)
    # 遍历文件夹中的所有文件
    for filename in os.listdir(folder_path):
        # 检查文件是否以指定后缀名结尾
        if filename.endswith(file_extension):
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)  # 删除文件
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
if __name__ == "__main__":
    # 设置要删除文件的文件夹路径和后缀名
    folder_path = "E:\\YOLOv5\\data\\labels\\val"  # 替换为目标文件夹路径
    file_extension = ".xml"  # 替换为您希望删除的文件后缀名

    delete_files_with_extension(folder_path, file_extension)
