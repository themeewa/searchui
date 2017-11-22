from imagefun.rgbhistogram import RGBHistogram
import argparse
import cPickle
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
args = vars(ap.parse_args())


index = {}

# initialize our image descriptor --  3D RGB histogram with
# 8 bins per channel
desc = RGBHistogram([8, 8, 8])

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
	# extract our unique image ID (i.e. the filename)
	k = imagePath[imagePath.rfind("/") + 1:]

	# load the image, RGB histogram descriptor
	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features

f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()

print "done...indexed %d images" % (len(index))