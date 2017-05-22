from Stitcher import Stitcher
import cv2
from os import listdir
from os.path import isfile,join



mypath = 'images'
# f = []
files = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f))]
files = sorted(files)
# print(files)
stitcher = Stitcher()

j= files[-1]

im1 = cv2.imread(j)
# cv2.imshow('i',im1)

for i in reversed(xrange(len(files)-1)):
	print i
	im2 = cv2.imread(files[i])
	# cv2.imshow('n',im2)

	result = stitcher.stitch(im1,im2)

	im1 = result

	# im1= result[~np.all(result == 0, axis=2)]
# result = stitcher.stitch(im1,im2)
# im1= result[~np.all(result == 0, axis=2)]



# result = stitcher.stitch(im1,im2)
# cv2.imshow('im1',im1)
cv2.namedWindow('m',cv2.WINDOW_NORMAL)
cv2.resizeWindow('m',5000,500)
cv2.imshow('m',im1)
cv2.waitKey(0)