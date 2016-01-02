##########-----------------------------------DONKEY KONG----------------------------------------#############
#controls a = left ,s = down , d = right , w = up , l = left jump , r= right jump f=straight jump  q = quit 
import os
import time
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
class Person:
    	def __init__(self,x=0,y=0):
	    	self.__x=x
		self.__y=y
class Player(Person):
    	def __init__(self,x,y):
	    	self.__x=x
		self.__y=y
		self.__flag=0
		self.__temp=0
		self.__Var=0
		self.__temp1=0
	def move(self,ch,sc,pm,g,f):
	    	if(ch=='a' or ch=='A'):
	   		sc.printpm(self.__x,self.__y,' ',pm,g,f)
			if(sc.checkwall(self.__x,self.__y-1) and sc.checkfloor(self.__x+1,self.__y-1) ):
				self.__y-=1
				
			sc.printpm(self.__x,self.__y,'P',pm,g,f)
		elif(ch=='d' or ch=='D'):
	   		sc.printpm(self.__x,self.__y,' ',pm,g,f)
			if(sc.checkwall(self.__x,self.__y+1) and sc.checkfloor(self.__x+1,self.__y+1) ):
		    		self.__y+=1
		
			sc.printpm(self.__x,self.__y,'P',pm,g,f)
		elif(ch=='w' or ch=='W'):
	   		sc.printpm(self.__x,self.__y,' ',pm,g,f)
		    	if(sc.checkwall(self.__x-1,self.__y) and sc.checkladder(self.__x-1,self.__y) ):
			    	self.__x-=1
			if(sc.checkwall(self.__x,self.__y-1)== False and sc.checkwall(self.__x,self.__y+1)== False ):
			    	self.__x-=1
		
			sc.printpm(self.__x,self.__y,'P',pm,g,f)

		elif(ch=='s' or ch=='S'):
	   		sc.printpm(self.__x,self.__y,' ',pm,g,f)
		    	if(sc.checkwall(self.__x+1,self.__y) and sc.checkladder(self.__x+1,self.__y)):
			    	self.__x+=1
			sc.printpm(self.__x,self.__y,'P',pm,g,f)
		
		elif(ch==' '):
		   	ch=getchar()
			if(ch=='d' or ch=='D'):
		      		if(self.__y<77):
		    	 		if(sc.checkwall(self.__x-2,self.__y+2) and sc.checkfloor(self.__x+1,self.__y+4) and sc.checkwall(self.__x,self.__y+4) and sc.checkwall(self.__x-1,self.__y+1) and sc.checkwall(self.__x-1,self.__y+3)):
	   	    				sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x-=1
					self.__y+=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)
					os.system("clear")
   					sc.printScreen()
					time.sleep(0.2)
					sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x-=1
					self.__y+=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)
					os.system("clear")
  					sc.printScreen()
					time.sleep(0.2)
					sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x+=1
					self.__y+=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)
					os.system("clear")
  					sc.printScreen()
					time.sleep(0.2)
	   				sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x+=1
					self.__y+=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)
			if(ch=='a' or ch=='A'):
		    		if(self.__y>3 ):

		    			if(sc.checkwall(self.__x-2,self.__y-2) and sc.checkfloor(self.__x+1,self.__y-4) and sc.checkwall(self.__x,self.__y-4) and sc.checkwall(self.__x-1,self.__y-1) and sc.checkwall(self.__x-1,self.__y-3)):
	   					sc.printpm(self.__x,self.__y,' ',pm,g,f)
						self.__x-=1
						self.__y-=1
						sc.printpm(self.__x,self.__y,'P',pm,g,f)
						os.system("clear")
   						sc.printScreen()
						time.sleep(0.1)
						sc.printpm(self.__x,self.__y,' ',pm,g,f)
						self.__x-=1
						self.__y-=1
						sc.printpm(self.__x,self.__y,'P',pm,g,f)
						os.system("clear")
   						sc.printScreen()
						time.sleep(0.1)

						sc.printpm(self.__x,self.__y,' ',pm,g,f)
						self.__x+=1
						self.__y-=1
						sc.printpm(self.__x,self.__y,'P',pm,g,f)
						os.system("clear")
   						sc.printScreen()
						time.sleep(0.1)
	   					sc.printpm(self.__x,self.__y,' ',pm,g,f)
						self.__x+=1
						self.__y-=1
						sc.printpm(self.__x,self.__y,'P',pm,g,f)

			elif(ch=='w' or ch=='W'):
		    		if(sc.checkfloor1(self.__x-1,self.__y) and sc.checkfloor1(self.__x-2,self.__y) ):
	   				sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x-=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)
					os.system("clear")
   					sc.printScreen()
					time.sleep(0.1)
					sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x-=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)
					os.system("clear")
					sc.printScreen()
					time.sleep(0.1)
	   				sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x+=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)
					os.system("clear")
   					sc.printScreen()
					time.sleep(0.1)
					sc.printpm(self.__x,self.__y,' ',pm,g,f)
					self.__x+=1
					sc.printpm(self.__x,self.__y,'P',pm,g,f)


	def getX(self):
	    	return self.__x

	def getY(self):
	    	return self.__y
	def getflag(self):
	    	return self.__flag
	def setflag(self,a):
	     	self.__flag=a
	def gettemp(self):
	    	return self.__temp
	def settemp(self,a):
	     	self.__temp=a
	def gettemp1(self):
	    	return self.__temp1
	def settemp1(self,a):
	     	self.__temp1=a

	def getVar(self):
	    	return self.__Var
	def setVar(self,a):
	    	self.__Var=a
