# Video to Image Converter

This script converts a video file into individual images, saving frames at specified intervals. It utilizes the OpenCV library for video processing and image handling.

## Features

- Extract frames from a video at a specified interval.
- Save extracted frames as image files in a specified output folder.
- Create the output folder if it does not exist.

## Requirements

- Python 3.10
- OpenCV library (`cv2`)

## Installation

1. Ensure you have Python 3 installed. If not, download and install it from [python.org](https://www.python.org/).
2. Install the OpenCV library using pip:
    ```bash
    pip install opencv-python
    ```

## Usage

1. Place your video file in the desired directory or provide the full path to the video file.
2. Modify the script or call the `video_to_images` function with appropriate arguments:
    ```python
    video_to_images('path_to_video_file', 'path_to_output_folder', frame_interval)
    ```
   - `path_to_video_file`: The path to the video file you want to process.
   - `path_to_output_folder`: The directory where extracted frames will be saved.
   - `frame_interval`: The interval between frames to be saved. For example, a value of 30 will save every 30th frame.

### Example

To extract frames from `input_video.mp4` and save every 30th frame to the `output_images` directory:

```python
video_to_images('input_video.mp4', 'output_images', 30)
