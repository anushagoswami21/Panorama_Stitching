from Stitcher import Stitcher
import cv2
from os import listdir
from os.path import isfile,join

#This code will take the 36 images from the images folder and combine 9 frames each to create 4 panoramas

mypath = 'images'

files = [join(mypath,f) for f in listdir(mypath) if isfile(join(mypath,f))]
files = sorted(files)

stitcher = Stitcher()



i=0
files_1 =[]

while(i<len(files)):
	files_1.append(files[i:i+9])
	i = i+9
# print(files_1)
z=1
files_2 = []
for j in files_1:
	l= j[-1]
	# print(j)
	im1 = cv2.imread(l)
	
	for i in reversed(xrange(len(j)-1)):
		print i
		im2 = cv2.imread(j[i])


		result = stitcher.stitch(im1,im2)

		im1 = result
	
	filename = 'final'
	files_2.append(im1)
	filename=filename+str(z)+".png"
	cv2.imwrite(filename,im1)
	filename = 'final'
	z=z+1
