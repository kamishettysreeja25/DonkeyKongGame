class Fireball:
    	def __init__(self,x,y):
	    	self.__x=x
		self.__y=y
		self.__Var=0
		self.__Flag=0
		self.__Temp=0
		self.__Temp1=0
		self.__Temp2=0
		self.__i=0
		self.__j=0
	def move(self,sc,rand,f,p):
	    	sc.printfi(self.__x,self.__y ,' ',f,p)
		if(rand==1):
		    	if(self.__y==1):
			    	self.__j=0
			elif(self.__y==78):
			    	self.__j=1
		    	if(sc.checkfloor(self.__x+1,self.__y+1) and self.__j==0 and sc.checko(self.__x,self.__y+1)and sc.checko(self.__x,self.__y+2) and sc.checko(self.__x+1,self.__y+1)):
#	if( self.__j==0 ):
						self.__y+=1
						self.__Temp=0
			elif(sc.checkfloor(self.__x+1,self.__y-1) and self.__j==1 and sc.checko(self.__x,self.__y-1) and sc.checko(self.__x,self.__y-2) and sc.checko(self.__x+1,self.__y-1)):
#if(self.__j==1):
						self.__y-=1
						self.__Temp=0
			elif(sc.checkfloor(self.__x+1,self.__y+1)== False):
			    		if(self.__Temp==0):
				    		self.__y+=1
						self.__Temp=1
			     		self.__x+=1
			elif(sc.checkfloor(self.__x+1,self.__y-1)== False):
			    		if(self.__Temp==0):
				    		self.__y-=1
						self.__Temp=1
			     		self.__x+=1
		elif(rand==2):
		    	if(self.__y==1):
			    	self.__i=0
			elif(self.__y==78):
			    	self.__i=1
		    	if(sc.checkdownladder(self.__x+1,self.__y) and sc.checko(self.__x+1,self.__y) and sc.checko(self.__x+2,self.__y) and sc.checko(self.__x+1,self.__y+1)):
			    	self.__x+=1
			elif(sc.checkdownladder(self.__x+1,self.__y)== False):
			    	if(sc.checkfloor(self.__x+1,self.__y)==False):
				    	self.__x+=1
				elif(sc.checkfloor(self.__x+1,self.__y)): 
					if( self.__i==0 ):
				    		self.__y+=1
					elif(self.__i==1):
						self.__y-=1
		sc.printfi(self.__x,self.__y,'O',f,p)

	# there to self floor for x+1 and y+1/ y-1
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
	    	return self.__Temp1
	def setTemp(self,a):
	    	self.__Temp1=a
	def getTemp1(self):
	    	return self.__Temp2
	def setTemp1(self,a):
	    	self.__Temp2=a
	def getj(self):
	    	self.__j
	def geti(self):
	    	self.__i
