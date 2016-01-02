import time
class Donkey():
	def __init__(self,x,y):
	    	self.__x=x
		self.__y=y
		self.__Flag=0
		self.__count=0
		self.__Var=0
		self.__Temp=0
		self.__var1=0

	def move(self,sc,g,p):
			sc.printg(self.__x,self.__y,' ',g,p)
			if(self.__y == 54):
				self.__count=1
			if(self.__y==1):
			    	self.__count=0
			if(self.__count==0 and sc.checko(self.__x,self.__y+1)):
			    		self.__y+=1
			if(self.__count==1 and sc.checko(self.__x,self.__y-1)):
			    		self.__y-=1
			time.sleep(0.2)
			sc.printg(self.__x,self.__y,'D',g,p)
	def getX(self):
	    	return self.__x
	def getY(self):
	    	return self.__y
	def getFlag(self):
	    	return self.__Flag
	def setFlag(self,a):
	    	self.__Flag=a
	def getVar(self):
	    	return self.__Var
	def setVar(self,a):
	    	self.__Var=a
	def getTemp(self):
	    	return self.__Temp
	def setTemp(self,a):
	    	self.__Temp=a
			    	
	def getVar1(self):
	    	return self.__var1
	def setVar1(self,a):
	    	self.__var1=a
	def getcount(self):
	    	return self.__count
