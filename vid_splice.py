import numpy as np
import skvideo.io

fp = "vid_data/prep_vid.mp4"
vid = skvideo.io.vread(fp)
T, M, N, C = vid.shape
print("Number of frames: %d" % (T,))
print("Number of rows: %d" % (M,))
print("Number of cols: %d" % (N,))
print("Number of channels: %d" % (C,))

print("Frame 0 mean value: ", np.mean(vid[0,:,:]))
print("Frame 0 max value: ", np.max(vid[0,:,:]))

print("Writing Frame 0 and last frame to PNG file...")

skvideo.io.vwrite("frame0.png", vid[0])
skvideo.io.vwrite("framelast.png", vid[-1])

print("Getting a chunk of the image...")

skvideo.io.vwrite("chunk.png", vid[-1: int(M/4):int(3*M/4), int(N/4):int(3*N/4), :])
