import numpy as np
import cv2
import imutils

class Stitcher:
    def stitch(self,im1,im2 , ratio = 0.75 ,thresh=4.0):
        (kp1,f1) = self.detectanddescribe(im1)
        (kp2,f2) = self.detectanddescribe(im2)

        M = self.matchKP(kp1,kp2,f1,f2,ratio,thresh)
        if M is None :
            return None

        (matches , H , status ) = M
        res = cv2.warpPerspective(im1, H,(im1.shape[1]+ im2.shape[1]/2, im1.shape[0]))

        res[0:im2.shape[0], 0:im2.shape[1]] = im2
        return res

    def detectanddescribe(self,im):
        descriptor = cv2.xfeatures2d.SIFT_create()
        (kps,features) = descriptor.detectAndCompute(im, None)
        kps = np.float32([kp.pt for kp in kps])
        return (kps,features)

    def matchKP(self, kp1,kp2, f1, f2 , ratio , thresh):
        matcher = cv2.DescriptorMatcher_create("BruteForce")
        rawMatches = matcher.knnMatch(f1, f2, 2)
        matches = []

        for i in rawMatches:
            if (len(i)==2 and i[0].distance<i[1].distance*ratio):
                matches.append((i[0].trainIdx,i[0].queryIdx))

        if len(matches)>4 :
            pt1 = np.float32([kp1[i] for (_, i) in matches])
            pt2 = np.float32([kp2[i] for(i,_) in matches])

            (H, status) = cv2.findHomography(pt1, pt2, cv2.RANSAC,
				thresh)

            return (matches,H , status)
        return None