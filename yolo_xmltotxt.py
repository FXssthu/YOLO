'''作用: 将 XML 格式的标注文件转换为 YOLO 格式的标注文件
参数列表:
1. classes: 类别列表
2. xml_file: XML 格式的标注文件路径
3. txt_file: YOLO 格式的标注文件路径
'''
import os
import xml.etree.ElementTree as ET

def convert_xml_to_yolo_format(xml_file, classes):
    # 解析 XML 文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 获取图像的宽度和高度
    width = int(root.find('size/width').text)
    height = int(root.find('size/height').text)

    # 存储 YOLO 格式的标注
    yolo_labels = []

    # 遍历所有物体
    for obj in root.findall('object'):
        class_name = obj.find('name').text
        if class_name in classes:
            class_id = classes.index(class_name)

            # 获取边界框
            xmlbox = obj.find('bndbox')
            xmin = int(xmlbox.find('xmin').text)
            ymin = int(xmlbox.find('ymin').text)
            xmax = int(xmlbox.find('xmax').text)
            ymax = int(xmlbox.find('ymax').text)

            # 计算 YOLO 格式的标注
            x_center = (xmin + xmax) / 2.0 / width
            y_center = (ymin + ymax) / 2.0 / height
            obj_width = (xmax - xmin) / width
            obj_height = (ymax - ymin) / height

            yolo_labels.append(f"{class_id} {x_center} {y_center} {obj_width} {obj_height}")

    return yolo_labels

def save_labels_to_txt(yolo_labels, txt_file):
    with open(txt_file, 'w') as f:
        for label in yolo_labels:
            f.write(label + '\n')

def convert_folder_xml_to_yolo_txt(xml_folder, txt_folder, classes):
    os.makedirs(txt_folder, exist_ok=True)

    for xml_file in os.listdir(xml_folder):
        if xml_file.endswith('.xml'):
            # 获取 XML 文件路径和相应的 TXT 文件名
            xml_path = os.path.join(xml_folder, xml_file)
            txt_file_name = xml_file.replace('.xml', '.txt')
            txt_path = os.path.join(txt_folder, txt_file_name)

            # 转换并保存
            yolo_labels = convert_xml_to_yolo_format(xml_path, classes)
            save_labels_to_txt(yolo_labels, txt_path)
            print(f"Converted {xml_file} to {txt_file_name}")

if __name__ == "__main__":
    # 定义类别
    classes = ["dog", "cat"]  # 替换为您的类名

    # 输入和输出文件夹
    xml_folder = "E:\\YOLOv5\\data\\labels\\val"  # 替换为您的 XML 文件夹路径
    txt_folder = "E:\\YOLOv5\\data\\labels\\val"   # 替换为输出 TXT 文件夹路径

    convert_folder_xml_to_yolo_txt(xml_folder, txt_folder, classes)
