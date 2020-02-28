import pyfbsdk as mbPy
import math
import ProgressOps

ProgressBar = ProgressOps.ExternalProgressBar()
with ProgressBar:
    for i in range(amount):
        for obj in selectedModels:
            perc = int(math.floor((float(i+1)/float(amount))*100))
            percentage = b"{0}".format(perc)
            ProgressBar.set_percentage(percentage)