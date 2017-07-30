from time import *
from random import *

date1 = (2008,1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1)
print '%d convert to %s'%(time1,asctime(localtime(time1)))
date2 = (2009,1,1,0,0,0,-1,-1,-1)
time2 = mktime(date2)
print '%d convert to %s'%(time2,asctime(localtime(time2)))
rand_time = uniform(time1,time2)
print '%d convert to %s'%(rand_time,asctime(localtime(rand_time)))

