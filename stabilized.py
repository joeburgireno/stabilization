
'''
    cut the video
    break up video into separate frames
    find the dy/dx from frame to frame
    move the video by the associated dy/dx
    compile video from frames
    '''

from subprocess import Popen
import argparse
from time import sleep
import sys


parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, help='video filename minus .mp4.')
args = parser.parse_args()

def stabilize(video): #no file extension, assumes mp4
    print("> Starting Crop Process.")
    process1 = Popen(['python', 'crop_video.py', '--filename', video])
    while process1.poll() is None:
        pass
        sys.stdout.flush()
    print("> Grabbing frames from video.")
    process2 = Popen(['python', 'images_from_video.py', '--filename', video])
    while process2.poll() is None: 
        pass
        sys.stdout.flush()
    print("> Finding dy and dx.")
    process3 = Popen(['python', 'shift.py', '--filename', video])
    while process3.poll() is None: 
        pass
        sys.stdout.flush()
    print("> Shifting image.")
    process4 = Popen(['python', 'translations.py', '--filename', video])
    while process4.poll() is None: 
        pass
        sys.stdout.flush()
    print("> Creating stabilized video.")
    process5 = Popen(['python', 'video_from_images.py', '--filename', video])
    while process5.poll() is None: 
        pass
        sys.stdout.flush()

if __name__ == '__main__':
    video = args.filename    
    stabilize(video)
 
