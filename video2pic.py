"""跳步法截取视频的指定帧并保存到指定文件夹 
参数列表:  
video_path: 视频文件路径  
output_folder: 保存帧的文件夹路径  
step: 步长，每隔多少帧截取一帧  
n_frames: 总共截取多少帧  
"""
import cv2      
import os  
# 获取视频的总帧数  
def get_video_frame_count(video_path):  
    # 打开视频文件  
    cap = cv2.VideoCapture(video_path)  
      
    # 检查视频是否成功打开  
    if not cap.isOpened():  
        print(f"Error: Cannot open video file {video_path}")  
        return None  
      
    # 获取视频的总帧数  
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  
      
    # 释放视频捕获对象  
    cap.release()  
      
    return frame_count  
# 截取视频的指定帧并保存到指定文件夹  
def extract_frames(video_path, output_folder, step, n_frames):  
    # 检查输出文件夹是否存在，不存在则创建  
    if not os.path.exists(output_folder):  
        os.makedirs(output_folder)  
  
    # 打开视频文件  
    cap = cv2.VideoCapture(video_path)  
    if not cap.isOpened():  
        print(f"Error: Cannot open video file {video_path}")  
        return  
  
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
  
    # 计算要截取的帧的索引  
    frame_indices = [i for i in range(0, frame_count, step)][:n_frames]  
    # 截取并保存帧  
    for idx, frame_id in enumerate(frame_indices):  
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)  
        ret, frame = cap.read()  
        if not ret:  
            print(f"Warning: Cannot read frame at index {frame_id}")  
            continue  
  
        # 保存帧到输出文件夹  
        output_path = os.path.join(output_folder, f"frame_{idx:04d}.jpg")  
        cv2.imwrite(output_path, frame)  
        print(f"Saved: {output_path}")  
  
    # 释放视频捕获对象  
    cap.release()  
    print("Frame extraction completed.")  
  
# 使用示例  
video_path = "04.mp4"                                              # 替换为你的视频文件路径  
output_folder = "C:/Users/Administrator/yolov5/data/mydata/image"  # 替换为你想要保存帧的文件夹路径  
frame_count = get_video_frame_count(video_path)  
n_frames = 99                                                      # 设置要截取的帧数  
step = int(frame_count/n_frames)  
# 打印信息 总共帧数，步长，已截取的帧数  
print(f"Total frames: {frame_count}, step: {step}, extract {n_frames} frames.")  
extract_frames(video_path, output_folder, step, n_frames)