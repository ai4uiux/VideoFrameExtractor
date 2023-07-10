Video Frame Extractor
This Python script allows you to extract frames from video files and save them as individual images using the OpenCV library. It provides a user-friendly interface for selecting video files using a file dialog, and you can specify the frame rate for extraction. The script also displays the progress of the frame extraction process for each video file.

Getting Started
Clone the repository or download the video_frame_extractor.py script.

Install the necessary dependencies:

bash
Copy code
pip install opencv-python tkinter
Run the script:

bash
Copy code
python video_frame_extractor.py
Choose the video files using the file dialog. Supported formats are .mp4, .avi, and .mkv.

The frames will be extracted based on the specified frame rate and saved as .png images in the output directory.

Progress status will be displayed for each video file being processed.

Once all video files have been processed, the script will indicate completion.

Configuration
Output Directory: By default, the extracted frames will be saved in "C:\SD\ALL_LORA_TRAINED\00inprogress\face_recognition\input". You can modify the base_output_dir variable in the script to specify a different output directory.

Frame Extraction Rate: The default extraction rate is set to every 30 frames. Adjust the frame_rate variable in the script to change it.

License
This project is licensed under the MIT License. See the LICENSE file for details.
