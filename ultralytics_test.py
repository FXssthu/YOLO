from ultralytics import YOLO

# 指定你的模型权重路径
model_path = 'E:\\YOLOv11\\runs\\detect\\onlyme6\\weights\\best.pt'  # 替换为你的模型权重路径

# 加载训练好的 YOLOv8 模型
model = YOLO(model_path)

# 指定测试图片路径
img_path = 'C:\\Users\\Administrator\\Desktop\\test2.png'  # 替换为你的图片路径

# 执行推理
results = model(img_path)

# 获取并打印检测结果
for result in results:
    # 获取检测框
    boxes = result.boxes  # 获取检测框对象

    # 如果有检测结果
    if boxes is not None and len(boxes) > 0:
        # 遍历每一个检测框
        for box in boxes.xyxy:  # 每个框包含 [x1, y1, x2, y2, confidence, class]
            # 先检查 box 的长度
            if len(box) == 6:  # 确保有 6 个值
                x1, y1, x2, y2, conf, cls = box.tolist()  # 转换为列表并解压
                class_name = result.names[int(cls)]  # 获取类别名称
                print(f"Detected {class_name} with confidence {conf:.2f} at [{x1:.2f}, {y1:.2f}, {x2:.2f}, {y2:.2f}]")
            else:
                print(f"Unexpected box format: {box}")

    else:
        print("No objects detected.")

    # 可视化结果
    result.show()  # 显示结果图像
    # result.save()  # 保存带有检测框的图像
