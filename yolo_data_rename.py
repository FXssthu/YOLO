"""重命名指定文件夹内的所有图片。
参数列表:
    directory (str): 文件夹路径
    new_name (str):  新文件名的基础部分
    extension (str): 目标图片文件的扩展名(例如 '.jpg','.png')
"""
import os
def rename_images(directory, new_name, extension):
    
    try:
        # 遍历文件夹内的所有文件
        for i, filename in enumerate(os.listdir(directory)):
            # 检查文件是否是目标图片类型
            if filename.endswith(extension):
                old_file_path = os.path.join(directory, filename)
                new_file_name = f"{new_name}_{i + 1}{extension}"  # 新的文件名
                new_file_path = os.path.join(directory, new_file_name)
                
                # 重命名文件
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: '{filename}' to '{new_file_name}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 修改为您的图片文件夹路径
    folder_path = "E:\\YOLOv5\\data\\images\\train"  # 例如："C:/Users/YourUsername/Pictures"
    
    # 指定新的文件名基础部分和图片扩展名
    base_name = "train"       # 修改为您希望的基础文件名
    image_extension = ".png"  # 可修改为 ".png" 或其他类型

    rename_images(folder_path, base_name, image_extension)
