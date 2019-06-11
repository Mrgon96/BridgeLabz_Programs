#import sys module
import sys
#import utility 
from utility import utility

#defining command line inputs
d = int(sys.argv[1]) 
m = int(sys.argv[2])
y = int(sys.argv[3])

#calling function from utility
utility.Day(d,m,y)