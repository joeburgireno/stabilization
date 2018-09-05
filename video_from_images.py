from subprocess import Popen
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, help='video filename minus .mp4.')
args = parser.parse_args()

def create_video(input_image):
    process = Popen(['ffmpeg', '-f', 'image2', '-r', '25', '-i', input_image+'/new_'+input_image+'_%03d.png',
               '-vb', '20M', '-vcodec', 'mpeg4', '-y', input_image+'_stabilized.mp4'])
    while process.poll() is None:
        pass
    print('done')

if __name__ == '__main__':
    imput_image = args.filename
    create_video(imput_image)
