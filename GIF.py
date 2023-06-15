from moviepy.editor import VideoFileClip
from tkinter.filedialog import *
video=askopenfilename()
clip=VideoFileClip(video)
clip.write_gif("timer.gif",fps=10)
