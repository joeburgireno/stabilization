
#Movie to images
#ffmpeg -i (in file name) -r (fps) (output file name)
#•	ffmpeg -y -i "N_3_top_left.mp4" -qscale 0 -r 25 "eye images/N_3_top_left_%03d.jpg"

from subprocess import Popen
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, help='video filename minus .mp4.')
args = parser.parse_args()

#input_file = input('File name (no extension - assuming mp4): ')

def images_to_folders(video):
    os.makedirs(video)
    os.makedirs(video+'_L3')#was just (video)
    create_cropped_images = Popen(['ffmpeg', '-y', '-i', video+'_L3.mp4', '-q:v', 
               '0', '-r', '25', video+'_L3'+'/'+video+'_L3_%03d.png'])
    create_full_images = Popen(['ffmpeg', '-i', video+'.mp4', '-vsync',
               '0', video+'/'+video+'_%03d.png'])
    while create_cropped_images.poll() or create_full_images.poll() is None: 
        pass
 
if __name__ == '__main__':
    video = args.filename
    images_to_folders(video)
