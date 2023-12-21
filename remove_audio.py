from moviepy.editor import VideoFileClip

def remove_audio(input_file, output_file):
    # Load the video clip
    video_clip = VideoFileClip(input_file, target_resolution=(1080, 1920))

    # Remove the audio
    video_clip = video_clip.set_audio(None)

    # Write the video without audio to a new file
    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # Close the video clip
    video_clip.close()

# Replace 'input.mp4' with the path to your input MP4 file
input_file = 'video\walking_through_store.mp4'

# Replace 'output_no_audio.mp4' with the desired output file name
output_file = 'video\walking_through_store_no_audio.mp4'

remove_audio(input_file, output_file)