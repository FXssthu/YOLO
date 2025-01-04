from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("runs/detect/onlyou3/weights/best.pt")
    img_path = "data/images/train/train_2.png"
    results = model(img_path)

    results[0].show()
