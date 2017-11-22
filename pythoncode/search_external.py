
# python search_external.py --dataset images --index index.cpickle --query queries/y.png

from imagefun.rgbhistogram import RGBHistogram
from imagefun.searcher import Searcher
import numpy as np
import argparse
import cPickle
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images we just indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where we stored our index")
ap.add_argument("-q", "--query", required = True,
	help = "Path to query image")
args = vars(ap.parse_args())

# load the query image and show it
queryImage = cv2.imread(args["query"])
cv2.imshow("Query", queryImage)
print "query: %s" % (args["query"])

# describe the query in the same way that we did in
# index.py -- a 3D RGB histogram with 8 bins per
# channel
desc = RGBHistogram([8, 8, 8])
queryFeatures = desc.describe(queryImage)

# load the index perform the search
index = cPickle.loads(open(args["index"]).read())
searcher = Searcher(index)
results = searcher.search(queryFeatures)

montageA = np.zeros((166 * 5, 400, 3), dtype = "uint8")
montageB = np.zeros((166 * 5, 400, 3), dtype = "uint8")

# loop over the top ten results
for j in xrange(0, 5):
	#  result e using row-major order
	# load the result image
	(score, imageName) = results[j]
	path = args["dataset"] + "/%s" % (imageName)
	result = cv2.imread(path)
	cv2.imshow("Results 1-5", result)
	cv2.waitKey(0)
	# cv2.waitKey(0)
	print "\t%d. %s : %.3f" % (j + 1, imageName, score)

	# if j < 5:
	# 	montageA[j * 166:(j + 1) * 166, :] = result

	# else:
	# 	montageB[(j - 5) * 166:((j - 5) + 1) * 166, :] = result

# show the results
# cv2.imshow("Results 1-5", montageA)
# cv2.imshow("Results 6-10", montageB)
# cv2.waitKey(0)