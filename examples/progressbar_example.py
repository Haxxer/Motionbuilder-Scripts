import pyfbsdk as mbPy
import math
import ProgressOps

loops = 10000000

ProgressBar = ProgressOps.ExternalProgressBar()
with ProgressBar:
    for i in range(loops):
        perc = int(math.floor((float(i+1)/float(loops))*100))
        percentage = b"{0}".format(perc)
        ProgressBar.set_percentage(percentage)