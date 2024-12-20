"""删除指定文件夹中所有带有特定名称的图片。
参数列表:
folder_path: 图像文件夹路径
keyword: 要查找的特定字符串
注意:
1. 该脚本仅删除图片文件，不会删除文件夹。
2. 该脚本仅支持png、jpg、jpeg、bmp、gif格式的图片文件。
3. 删除是永久性的，不可恢复。请谨慎操作。
"""
import os
def delete_images_with_keyword(folder_path, keyword):
    # 遍历文件夹内所有文件
    for filename in os.listdir(folder_path):
        # 检查图片文件类型
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')) and keyword in filename:
            file_path = os.path.join(folder_path, filename)
            try:
                os.remove(file_path)  # 删除文件
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
if __name__ == "__main__":
    # 修改为您的图像文件夹路径
    images_folder = "E:\\YOLOv5\\data\\labels\\train"  # 例如："C:/Users/YourUsername/Pictures"
    
    # 修改为您要查找的特定字符串
    keyword = "txt"  # 例如："test"

    # 调用删除函数
    delete_images_with_keyword(images_folder, keyword)
