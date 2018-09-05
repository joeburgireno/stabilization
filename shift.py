import numpy as np
import os
from skimage.feature import (match_descriptors, corner_harris,
                             corner_peaks, ORB, plot_matches)
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from pdb import set_trace as db
from skimage import io
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, help='video filename minus .mp4.')
args = parser.parse_args()

def find_dxdy(video):
    
    directory = os.listdir(video+'_L3')
    numb_of_files = len(directory)

    horizontal_shift = []
    vertical_shift = []

    img1 = rgb2gray(io.imread(video+'_L3'+'/'+video+'_L3'+'_{0:0=3d}'.format(1)+'.png'))

    for i in tqdm(range(1,numb_of_files)):

        img2 = rgb2gray(io.imread(video+'_L3'+'/'+video+'_L3'+'_{0:0=3d}'.format(i+1)+'.png'))

        descriptor_extractor = ORB(n_keypoints=200)

        descriptor_extractor.detect_and_extract(img1)
        kp1 = descriptor_extractor.keypoints
        des1 = descriptor_extractor.descriptors

        descriptor_extractor.detect_and_extract(img2)
        kp2 = descriptor_extractor.keypoints
        des2 = descriptor_extractor.descriptors

        matches = match_descriptors(des1, des2, cross_check=True)

        dx = [kp1[idx[0]][0] - kp2[idx[1]][0] for idx in matches]
        dy = [kp1[idx[0]][1] - kp2[idx[1]][1] for idx in matches]

#        plt.hist(dx, 100)
#        plt.show()
        
#        plt.hist(dy, 100)
#        plt.show()        

        horizontal_shift.append(np.median(dx))
        vertical_shift.append(np.median(dy)) 

    dx_dy = np.column_stack((horizontal_shift, vertical_shift))
    
    np.savetxt(video+'_dxdy.csv', dx_dy, delimiter=",")

#k1 = np.array(list_kp1) - turns list_kp1 into an nx2 matrix
#dk = k1-k2
#hist(dk[:,0],100) then show() to see the histogram
#np.median(k1,0) - finds the median of a mxn matrix into an 1xn

if __name__ == '__main__':
    video = args.filename
    find_dxdy(video)

