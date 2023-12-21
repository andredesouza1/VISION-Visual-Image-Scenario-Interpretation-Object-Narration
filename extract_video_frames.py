from moviepy.video.io.VideoFileClip import VideoFileClip
import os
import imageio

def extract_frames(input_path, output_path):
    """Extracts frames from a video clip every half second, preserving original dimensions."""
    # clears temp folder of images
    folder_path = output_path
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    # Load the video clip
    clip = VideoFileClip(input_path, target_resolution=(1920, 1080))

    # Get the original frame dimensions
    width, height = clip.size
    print(width, height)

    # Get video duration and frame rate
    duration = clip.duration
    fps = clip.fps

    # Calculate the number of frames to extract (2 frames per second)
    num_frames = int(duration * fps * 2)  # Multiply by 2 for half-second intervals

    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Extract frames every half second
    for i in range(num_frames):
        # Get the frame at the current half-second interval
        frame = clip.get_frame(i * 0.5)  # Access frame every 0.5 seconds

        # Save the frame as an image with original dimensions
        frame_path = os.path.join(output_path, f'frame_{i + 1:03d}.jpg')
        imageio.imwrite(frame_path, frame, format='jpg')
        print(i)
        if i >= duration*2:
            break

    # Close the video clip
    clip.close()
    
if __name__ == "__main__":
    input_video_path = "video\walking_through_store.mp4"
    output_frames_path = "./video_frames"

    extract_frames(input_video_path, output_frames_path)


