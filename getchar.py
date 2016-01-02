##########-----------------------------------DONKEY KONG----------------------------------------#############
#controls a = left ,s = down , d = right , w = up , l = left jump , r= right jump f=straight jump  q = quit 
from random import *
import os
import time
import math
def getchar():
            	"""Returns a single character from standard input""" """Function taken from Github : https://gist.github.com/jasonrdsouza/1901709"""
		import tty, termios, sys 
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
