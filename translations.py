import numpy as np
import cv2 as cv
import os
import pandas as pd
import argparse
from tqdm import tqdm
from pdb import set_trace as db

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, help='video filename minus .mp4.')
args = parser.parse_args()

def translations(images):
    directory = os.listdir(images)
    numb_of_files = len(directory)
    
    dxdy = pd.read_csv(images+'_dxdy.csv', header=None)
    
    for i in tqdm(range(1,numb_of_files)):
        img = cv.imread(images+'/'+images+'_'+'{0:0=3d}'.format(i+1)+'.png',0)
        rows,cols = img.shape #channels needed if image is color
        dx = dxdy.iloc[i-1,0]
#        if dx < np.abs(5):
#            dx = dx
#        else:
#            dx = 0
        dy = dxdy.iloc[i-1,1]
#        if dy < np.abs(5):
#            dy = dy
#        else:
#            dy = 0
        M = np.float32([[1,0,dy],[0,1,dx]])
        dst = cv.warpAffine(img,M,(cols,rows))
        cv.imwrite(images+'/'+'new_'+images+'_'+'{0:0=3d}'.format(i)+'.png',dst)
        
if __name__ == '__main__':
    images = args.filename
    translations(images)
