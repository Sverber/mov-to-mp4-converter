import os
import shutil
from moviepy.editor import VideoFileClip

# Define input, output, and failed directories
input_directory = 'input'
output_directory = 'output'
failed_directory = 'failed'

# Create the output and failed directories if they don't exist
os.makedirs(output_directory, exist_ok=True)
os.makedirs(failed_directory, exist_ok=True)

# Convert each MOV file to MP4
for input_filename in os.listdir(input_directory):
    if input_filename.endswith('.mov') or input_filename.endswith('.MOV'):
        input_path = os.path.join(input_directory, input_filename)
        try:
            # Load the video file
            video = VideoFileClip(input_path)
            output_filename = os.path.splitext(input_filename)[0] + '.mp4'
            output_path = os.path.join(output_directory, output_filename)

            # Ensure compatibility with Windows by specifying codecs
            video.write_videofile(
                output_path,
                codec='libx264',  # Widely supported video codec
                audio_codec='aac',  # Widely supported audio codec
                ffmpeg_params=['-preset', 'slow', '-crf', '22']  # Adjust compression settings for compatibility
            )

            print(f'Converted {input_filename} to {output_path}')
        except Exception as e:
            print(f'Conversion of {input_filename} failed: {str(e)}')
            # Copy the failed video to the "failed" directory
            failed_path = os.path.join(failed_directory, input_filename)
            shutil.copy(input_path, failed_path)
            print(f'Copied {input_filename} to {failed_path}')
