import numpy as np
import skvideo.io

fp = "vid_data/yooh_vid.mp4"
vid = skvideo.io.vread(fp)
T, M, N, C = vid.shape
print("Number of frames: %d" % (T,))
print("Number of rows: %d" % (M,))
print("Number of cols: %d" % (N,))
print("Number of channels: %d" % (C,))

print("Frame 1 mean value: ", np.mean(vid[0,:,:]))
print("Frame 1 max value: ", np.max(vid[0,:,:]))

print("Writing Frame 1 to PNG file...")

skvideo.io.vwrite("frame1.png", vid[-1])
