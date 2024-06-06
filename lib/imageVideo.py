import cv2
import os
import sys
import glob


def log_progress(process, total, current):
    progress = int(50 * current / total)
    sys.stdout.write(f'\r{process}: [{"#" * progress}{"." * (50 - progress)}] {current}/{total} frames processed')
    sys.stdout.flush()


def convert_images_to_video(image_folder, output_path, fps=30, cleanup=False):
    images = sorted(
        glob.glob(os.path.join(image_folder, '*.jpg')) + glob.glob(os.path.join(image_folder, '*.png')),
        key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[-1])
    )

    if not images:
        print("No images found in the directory.")
        return

    frame = cv2.imread(images[0])
    height, width, layers = frame.shape

    video_name = os.path.basename(image_folder) + '.mp4'
    video_path = os.path.join(output_path, video_name)
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'avc1'), fps, (width, height))
    #video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))
    #video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'MP4V'), fps, (width, height))



    total_frames = len(images)
    for i, image in enumerate(images):
        video.write(cv2.imread(image))
        log_progress(f"Converting {video_name}", total_frames, i + 1)

    #cv2.destroyAllWindows()
    video.release()
    print(f"\nVideo saved: {video_path}")

    if cleanup:
        for image in images:
            os.remove(image)
        os.rmdir(image_folder)
        print(f"Cleaned up folder: {image_folder}")


def process_image_directories(root_path, cleanup=False):
    directories = [d for d in os.listdir(root_path) if os.path.isdir(os.path.join(root_path, d))]
    
    for directory in directories:
        image_folder = os.path.join(root_path, directory)
        print(f"\nProcessing directory: {image_folder}")
        convert_images_to_video(image_folder, root_path, cleanup=cleanup)


def main():
    default_path = r"C:\Projects"
    input_path = input(f"Enter the path to search for image directories or press enter to use the default ({default_path}): ").strip()
    input_path = input_path if input_path else default_path

    cleanup_response = input("Do you want to remove the image directories after conversion? (yes/no): ").strip().lower()
    cleanup = cleanup_response == 'yes'

    process_image_directories(input_path, cleanup)

if __name__ == "__main__":
    main()
