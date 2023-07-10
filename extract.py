import cv2
import os
import tkinter as tk
from tkinter import filedialog

# Set the default output directory
base_output_dir = "C:\\SD\\ALL_LORA_TRAINED\\00inprogress\\face_recognition\\input"

# Create a Tkinter root widget
root = tk.Tk()
root.withdraw()  # Hide the root widget

# Open a file dialog for the user to choose the video files
video_files = filedialog.askopenfilenames(title="Choose video files", filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])

# Check if the user canceled the file dialog
if not video_files:
    print("No video files chosen, exiting.")
    exit()

# Loop over the video files
for video_file in video_files:
    # Load the video
    cap = cv2.VideoCapture(video_file)

    # Get the frames per second (fps) of the video
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the frame extraction rate (every 30 frames)
    frame_rate = 30

    # Get the base name of the video file without the extension
    base_name = os.path.splitext(os.path.basename(video_file))[0]

    # Create a directory for the current video file
    output_dir = os.path.join(base_output_dir, base_name)
    os.makedirs(output_dir, exist_ok=True)

    # Initialize a counter for the current frame
    current_frame = 0

    # Get total number of frames
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Loop over all frames in the video
    while True:
        # Read the current frame
        is_read, frame = cap.read()

        # Check if the frame was read correctly
        if not is_read:
            break

        # Check if the current frame number is divisible by the frame rate
        if current_frame % frame_rate == 0:
            # Save the current frame as a .png image
            frame_file = os.path.join(output_dir, f"{base_name}_{current_frame // frame_rate}.png")
            cv2.imwrite(frame_file, frame)

        # Increment the current frame number
        current_frame += 1

        # Calculate the progress percentage
        progress_percentage = (current_frame / total_frames) * 100

        # Print the progress status
        print(f"Progress for {base_name}: {progress_percentage:.2f}%")

    # Release the video file
    cap.release()

    print(f"Frames for {base_name} have been extracted to the directory: {output_dir}")

print("All video files processed.")
