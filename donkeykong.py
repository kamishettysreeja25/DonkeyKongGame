##########-----------------------------------DONKEY KONG----------------------------------------#############
#controls a = left ,s = down , d = right , w = up , l = left jump , r= right jump f=straight jump  q = quit 
from random import *
import os
import time
import math
from board  import *
from fireball import *
from donkkong import *
from getchar import *
from person import * 
def newlevel(sc):
  rand=randint(1,2)	
  screen=Board(rand)
  pm=Player(28,1)
  dk1=Donkey(6,1) 
  count=0
  i=0
  fb=[]
  if(count==0):
	fb.insert(i,Fireball(dk1.getX(),dk1.getY()+1))
	screen.printfi(dk1.getX(),dk1.getY()+2,'O',fb[i],pm)
	i+=1
  screen.printpm(28,1,'P',pm,dk1,fb[0])
  screen.printg(6,1,'D',dk1,pm)
  os.system("clear")
  screen.gencoins()
  screen.printScreen()
  return sc
    	
def play():
	ch=getchar()
	if(ch=='q'):
        	print "Your Score is :",
		print score	
    		exit()
	pm.move(ch,screen,pm,dk1,fb[0])
def main():
  lifes=3
  sco=0
  score=0
  rand=randint(1,2)
  screen=Board(rand)
  pm=Player(28,1)
  dk1=Donkey(6,1) 
  count=0
  i=0
  fb=[]
  st=0
  to=1
  if(count==0):
	fb.insert(i,Fireball(dk1.getX(),dk1.getY()+1))
	screen.printfi(dk1.getX(),dk1.getY()+2,'O',fb[i],pm)
	i+=1
  screen.printpm(28,1,'P',pm,dk1,fb[0])
  screen.printg(6,1,'D',dk1,pm)
  os.system("clear")
  screen.gencoins()
  while(lifes):
  	os.system("clear")
      	screen.printScreen()
    	che=''
	while(1):
	    	score=screen.getScore()
               	print "Your Score is  :",
	     	print score
	     	print "Your in level :",
		print to
		print "Enter move :",
		ch=getchar()
		if(ch=='q'):
		    	print "Game over : "
               		print "Your Score is :",
	        	print score	
    			exit()
		pm.move(ch,screen,pm,dk1,fb[0])
		dk1.move(screen,dk1,pm)
    		u=screen.checkqueen(pm)
    		if(u=='n'):
		    	pm.settemp1(0)
			to+=1
               		print "Your are in level  :",
	        	print to
    			print "lifes remaining : ",
			print lifes
			time.sleep(1)
			print st
			st=screen.getScore()
			st=st-50
  			rand=randint(1,2)	
  			screen=Board(rand)
  			pm=Player(28,1)
  			dk1=Donkey(6,1) 
  			count=0
 			i=0
 			fb=[]
 			if(count==0):
				fb.insert(i,Fireball(dk1.getX(),dk1.getY()+1))
				screen.printfi(dk1.getX(),dk1.getY()+2,'O',fb[i],pm)
				i+=1
  			screen.printpm(28,1,'P',pm,dk1,fb[0])
  			screen.printg(6,1,'D',dk1,pm)
 			os.system("clear")
  			screen.gencoins()
  			screen.printScreen()
			screen.setScore(st)
		    	break
    		t=screen.checkdonkey(pm,dk1)
    		if(t=='q'):
               		print "Your Score is :",
	        	print score
			#os.system("clear")
#			screen.printScreen()
			lifes-=1
    			print "lifes remaining : ",
			print lifes
			time.sleep(1)
			screen.printpm(pm.getX(),pm.getY(),' ',pm,dk1,fb[0])
			pm=Player(28,1)
			screen.printpm(28,1,'P',pm,dk1,fb[0])
			os.system("clear")
			screen.printScreen()
    			break
    		if(count%40==0 and count!=0):
			fb.insert(i,Fireball(dk1.getX(),dk1.getY()+1))
			screen.printfi(dk1.getX(),dk1.getY()+1,'O',fb[i],pm)
			i+=1
		j=0
		if(count>0):
			for j in range(len(fb)):
				rand=randint(1,2)
				if(j<len(fb)):
					che=screen.checkfireball(pm,fb[j])
					if(che=='q'):
               					print "Your Score is  :",
	        				print score
						lifes-=1
    						print "lifes remaining : ",
						print lifes
						time.sleep(1)
						screen.printpm(pm.getX(),pm.getY(),' ',pm,dk1,fb[0])
						pm=Player(28,1)
						screen.printpm(28,1,'P',pm,dk1,fb[0])
						os.system("clear")
						screen.printScreen()
    						break
					fb[j].move(screen,rand,fb[j],pm)
					#					if (fb[j].getX() ==28 ):
					#if(fb[j].getY()==78 or fb[j].getY()==1):
						#						screen.printfi(fb[j].getX(),fb[j].getY(),' ' ,fb[j])
#						fb.pop(j)
#					i-=1
   		if(che=='q'):
			break
		count+=1

    		os.system("clear")
		screen.printScreen()
	
  print "Game Over!!!"
  print "Your Score is :",
  print score
  time.sleep(1)
	
if __name__=="__main__":
     main()
