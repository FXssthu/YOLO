"""将图像调整为正方形，使用补白的方式。
参数列表:
        image_path (str): 输入图像的路径
        output_path (str): 输出图像的路径
注意:
1.不会删除原图像，只会生成一个新的图像。
"""
import os
from PIL import Image

def resize_to_square(image_path, output_path):
    
    with Image.open(image_path) as img:
        # 获取图像尺寸
        width, height = img.size
        max_side = max(width, height)

        # 创建一个正方形的白色背景图像
        new_image = Image.new("RGB", (max_side, max_side), (255, 255, 255))
        
        # 计算放置原图像的位置
        left = (max_side - width) // 2
        top = (max_side - height) // 2

        # 将原图像粘贴到正方形背景上
        new_image.paste(img, (left, top))
        
        # 保存新图像
        new_image.save(output_path)

def process_images_in_folder(folder_path):
    """
    遍历文件夹内的所有图片，并将其调整为正方形。

    参数:
        folder_path (str): 待处理的图像文件夹路径
    """
    # 遍历文件夹内所有文件
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # 支持的图片格式
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"square_{filename}")  # 在文件名前加上 "square_"

            resize_to_square(input_path, output_path)
            print(f"Processed: '{input_path}' to '{output_path}'")

if __name__ == "__main__":
    # 修改为您的图像文件夹路径
    images_folder = "E:\\YOLOv5\\data\\images\\train"  # 例如："C:/Users/YourUsername/Pictures"
    
    process_images_in_folder(images_folder)
