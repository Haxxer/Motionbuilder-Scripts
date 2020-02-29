import pyfbsdk as mbPy
import math
import ProgressOps
import time

loops = 10000

ProgressBar = ProgressOps.ExternalProgressBar()

with ProgressBar:
    start_time = time.time()
    for i in range(loops):
        perc = int(math.floor((float(i+1)/float(loops))*100))
        ProgressBar.set_percentage(perc)

end_time = time.time()
progress_time = end_time-start_time
print('Execution time is {0}s'.format(progress_time))
