from moviepy.editor import VideoFileClip

def create_gif_from_video(video_path, gif_path, start_time, duration):
    # Load the video
    clip = VideoFileClip(video_path)
    
    # Trim the video to the specified time frame
    gif_clip = clip.subclip(start_time, start_time + duration)
    
    # Save the clip as a GIF
    gif_clip.write_gif(gif_path)

# Example usage:
video_path = r".\loom-video.mp4"
gif_path = r"output\output"
start_time = [56,63,66,71,74,78,87]
duration = 1

for i in start_time:
    create_gif_from_video(video_path, gif_path+str(i)+".gif", i, duration)