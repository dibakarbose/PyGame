import pygame,sys,time,os,tkinter
import newButton

os.environ['SDL_VIDEO_CENTERED'] = '1'			#To start PyGame window at the center of the screen

pygame.init()
pygame.font.init()
#myfont = pygame.font.SysFont('Lucida Handwriting', 30)
#textsurface1 = myfont.render('Player 1=', False, (0, 0, 0))
#textsurface2 = myfont.render('Player 2=', False, (0, 0, 0))

LEFT=1
r=0
RED=(255,0,0)
windowSize=width,height=(800,600)
screen=pygame.display.set_mode(windowSize)
pygame.display.set_caption("Tic Tac Toe")
running =1
board=pygame.image.load("Board.jpg")
round_Shape=pygame.image.load("Round.png")
cross_Shape=pygame.image.load("Cross.png")
board_rect=board.get_rect()
#round_rect=round_Shape.get_rect()
#cross_rect=cross_Shape.get_rect()
screen.blit(board,board_rect)
#screen.blit(textsurface1,(10,10))
#screen.blit(textsurface2,(540,10))


Box1 = [(130,65),"empty"]
Box2 = [(325,65),"empty"]
Box3 = [(520,65),"empty"]
Box4 = [(130,225),"empty"]
Box5 = [(325,225),"empty"]
Box6 = [(520,225),"empty"]
Box7 = [(130,385),"empty"]
Box8 = [(325,385),"empty"]
Box9 = [(520,385),"empty"]

press_count=0


def load_Screen():
	loadScreen=pygame.image.load("board.jpg")
	loadScreen_rect=loadScreen.get_rect()
	screen.blit(loadScreen,loadScreen_rect)
	Box1[1]='empty'
	Box2[1]='empty'
	Box3[1]='empty'
	Box4[1]='empty'
	Box5[1]='empty'
	Box6[1]='empty'
	Box7[1]='empty'
	Box8[1]='empty'
	Box9[1]='empty'

def draw_Round(x,y,press_count):
	if(x<=305 and y<=220 and Box1[1]=="empty"):
		screen.blit(round_Shape,Box1[0])
		Box1[1]="round"
		press_count=press_count+1
	elif(x<=495 and y<=220 and x>=307 and Box2[1]=="empty"):
		screen.blit(round_Shape,Box2[0])
		Box2[1]="round"
		press_count=press_count+1
	elif(x<=700and y<=220 and x>=497 and Box3[1]=="empty"):
		screen.blit(round_Shape,Box3[0])
		Box3[1]="round"
		press_count=press_count+1
	elif(x<=305 and y<=380 and y>=222 and Box4[1]=="empty"):
		screen.blit(round_Shape,Box4[0])
		Box4[1]="round"
		press_count=press_count+1
	elif(x<=495 and y<=380 and x>=307 and y>=222 and Box5[1]=="empty"):
		screen.blit(round_Shape,Box5[0])
		Box5[1]="round"
		press_count=press_count+1
	elif(x<=700 and y<=380 and x>=497 and y>=222 and Box6[1]=="empty"):
		screen.blit(round_Shape,Box6[0])
		Box6[1]="round"
		press_count=press_count+1
	elif(x<=305 and y<=535 and y>=382 and Box7[1]=="empty"):
		screen.blit(round_Shape,Box7[0])
		Box7[1]="round"
		press_count=press_count+1
	elif(x<=495 and y<=535 and x>=307 and y>=382 and Box8[1]=="empty"):
		screen.blit(round_Shape,Box8[0])
		Box8[1]="round"
		press_count=press_count+1
	elif(x<=700 and y<=535 and x>=497 and y>=382 and Box9[1]=="empty"):
		screen.blit(round_Shape,Box9[0])
		Box9[1]="round"
		press_count=press_count+1
	return press_count


def draw_Cross(x,y,press_count):
	if(x<=305 and y<=220 and Box1[1]=="empty"):
		screen.blit(cross_Shape,Box1[0])
		Box1[1]="cross"
		press_count=press_count+1
	elif(x<=495 and y<=220 and x>=307 and Box2[1]=="empty"):
		screen.blit(cross_Shape,Box2[0])
		Box2[1]="cross"
		press_count=press_count+1
	elif(x<=700and y<=220 and x>=497 and Box3[1]=="empty"):
		screen.blit(cross_Shape,Box3[0])
		Box3[1]="cross"
		press_count=press_count+1
	elif(x<=305 and y<=380 and y>=222 and Box4[1]=="empty"):
		screen.blit(cross_Shape,Box4[0])
		Box4[1]="cross"
		press_count=press_count+1
	elif(x<=495 and y<=380 and x>=307 and y>=222 and Box5[1]=="empty"):
		screen.blit(cross_Shape,Box5[0])
		Box5[1]="cross"
		press_count=press_count+1
	elif(x<=700 and y<=380 and x>=497 and y>=222 and Box6[1]=="empty"):
		screen.blit(cross_Shape,Box6[0])
		Box6[1]="cross"
		press_count=press_count+1
	elif(x<=305 and y<=535 and y>=382 and Box7[1]=="empty"):
		screen.blit(cross_Shape,Box7[0])
		Box7[1]="cross"
		press_count=press_count+1
	elif(x<=495 and y<=535 and x>=307 and y>=382 and Box8[1]=="empty"):
		screen.blit(cross_Shape,Box8[0])
		Box8[1]="cross"
		press_count=press_count+1
	elif(x<=700 and y<=535 and x>=497 and y>=382 and Box9[1]=="empty"):
		screen.blit(cross_Shape,Box9[0])
		Box9[1]="cross"
		press_count=press_count+1

	return press_count


def check_win():
	print("Started CheckWinner Loop")
	if Box1[1]==Box2[1]==Box3[1]=="cross" or Box1[1]==Box2[1]==Box3[1]=="round":
		pygame.draw.line(screen, RED, (105,135), (695,135), 4)
		return 1
	elif Box4[1]==Box5[1]==Box6[1]=="cross" or Box4[1]==Box5[1]== Box6[1]=="round":
		pygame.draw.line(screen, RED, (105,300), (695,300), 4)
		return 1
	elif Box7[1]==Box8[1]==Box9[1]=="cross" or Box7[1]==Box8[1]==Box9[1]=="round":
		pygame.draw.line(screen, RED, (105,460), (695,460), 4)
		return 1
	elif Box1[1]==Box4[1]==Box7[1]=="cross" or Box1[1]==Box4[1]==Box7[1]=="round":
		pygame.draw.line(screen, RED, (200,50), (200,540), 4)
		return 1
	elif Box2[1]==Box5[1]==Box8[1]=="cross" or Box2[1]==Box5[1]==Box8[1]=="round":
		pygame.draw.line(screen, RED, (400,50), (400,540), 4)
		return 1
	elif Box3[1]==Box6[1]==Box9[1]=="cross" or Box3[1]==Box6[1]==Box9[1]=="round":
		pygame.draw.line(screen, RED, (590,50), (590,540), 4)
		return 1
	elif Box1[1]==Box5[1]==Box9[1]=="cross" or Box1[1]==Box5[1]==Box9[1]=="round":
		pygame.draw.line(screen, RED,(105,65), (675,530), 4)
		return 1
	elif Box3[1]==Box5[1]==Box7[1]=="cross" or Box3[1]==Box5[1]==Box7[1]=="round":
		pygame.draw.line(screen, RED, (675,70), (120,530), 4)
		return 1
	return 0


#btn = newButton.Button('New Game', 675, 550, 100, 50)
while running:
	event=pygame.event.poll()
	if event.type==pygame.QUIT:
		running=0
	elif event.type==pygame.MOUSEBUTTONDOWN and event.button==LEFT:
		x,y=event.pos
	elif event.type==pygame.MOUSEMOTION:
		a,b=event.pos
		print("Mouse at x=%d y=%d"%(a,b))
	elif event.type==pygame.MOUSEBUTTONUP and event.button==LEFT:
		if press_count%2==0:
			press_count=draw_Round(x,y,press_count)
			pass
		else:
			press_count=draw_Cross(x,y,press_count)
		
		
		if press_count==9:
			pygame.display.flip()
			press_count=0
			time.sleep(3)
			load_Screen()
			r=0
		x,y=0,0

	if press_count>=5:
		r=check_win()
		pygame.display.flip()
		if r==1:
			print("In Sleep Loop")
			time.sleep(3)
			load_Screen()
			r=0
			press_count=0

	#if(r==1):
	#	btn.handle_event(event)
	#	r=0

	

	pygame.display.flip()