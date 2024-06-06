import cv2
import os
import sys
from glob import glob


def log_progress(process, total, current):
    progress = int(50 * current / total)
    sys.stdout.write(f'\r{process}: [{"#" * progress}{"." * (50 - progress)}] {current}/{total} frames processed')
    sys.stdout.flush()


def convert(video_path, output_dir):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    video_output_dir = os.path.join(output_dir, video_name)
    
    if not os.path.exists(video_output_dir):
        os.makedirs(video_output_dir)
    
    video = cv2.VideoCapture(video_path)
    
    if not video.isOpened():
        print(f"Error: Could not open video {video_name}.")
        return
    
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    
    for current_frame in range(frame_count):
        ret, frame = video.read()
        if not ret:
            break
        
        frame_filename = os.path.join(video_output_dir, f"{video_name}_frame_{current_frame}.png")
        cv2.imwrite(frame_filename, frame)
        
        if current_frame % 20 == 0 or current_frame == frame_count - 1:
            log_progress(video_name, frame_count, current_frame + 1)
    
    video.release()
    print(f"\nCompleted: {video_name} has been processed with {frame_count} frames.")


def search_and_convert(input_dir=None):
    default_path = r"C:\Projects"
    if not input_dir:
        print(f"No input path provided. Using default path: {default_path}")
        input_dir = default_path
    
    if not os.path.exists(input_dir):
        print(f"The specified directory does not exist: {input_dir}")
        return
    
    video_files = glob(os.path.join(input_dir, "*.mp4")) + glob(os.path.join(input_dir, "*.ts"))
    
    if not video_files:
        print("No video files found.")
        return
    
    print(f"Found {len(video_files)} video file(s) to process.")
    for video_file in video_files:
        video = cv2.VideoCapture(video_file)
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video_name = os.path.basename(video_file)
        print(f"Video: {video_name} with {frame_count} frames to convert.")
        video.release()
    
    input("Press Enter to start converting all videos...")
    
    for video_file in video_files:
        print(f"\nProcessing {video_file}...")
        convert(video_file, input_dir)


user_input = input("Enter the path to search for video files or press enter to use the default: ").strip()
search_and_convert(user_input if user_input else None)
