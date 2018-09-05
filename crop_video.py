from subprocess import Popen
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, help='video filename minus .mp4.')
args = parser.parse_args()

video = args.filename

def crop_video(video):
    process = Popen(['ffmpeg', '-i', video+'.mp4', '-filter:v',
               'crop=in_w/3:in_h:0:0', video+'_L3'+'.mp4'])
    while process.poll() is None: 
        pass
 
if __name__ == '__main__':
    video = args.filename 
    crop_video(video)
    
