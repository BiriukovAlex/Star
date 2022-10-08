import random
import pygame
import sys

WINWIDTH = 640 # width of the program's window, in pixels
WINHEIGHT = 480 # height in pixels
FPS = 60

NumStar = 100		# Общее количество звезд
speed = 1.29 		# Скорость полета звезд
stars = []			# Список, содержащий звезды
					# каждая звезда состоит из X-координаты, Y-координаты,
					# расстояния по Z (дальность до звезды), цвет

BRIGHTBLUE = (  0, 170, 255)
RED = (  255, 0, 0)
GREEN =  (  0, 255, 0) 

LEFT = 'left'
RIGHT = 'right'
FIRE = 'fire'
  
def main():
	pygame.init()
	print (__name__)
	FPSCLOCK = pygame.time.Clock()
	print (FPSCLOCK)
	pygame.mixer.init()  # для звука
	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	print (DISPLAYSURF)
	pygame.display.set_caption('First')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 10)
	print (BASICFONT)

	r = pygame.Rect(0, 0, WINWIDTH, 20)
	pygame.draw.rect(DISPLAYSURF, BRIGHTBLUE, r, 0)

	text = BASICFONT.render(str('RUN'), True, RED)
	DISPLAYSURF.blit(text, (0, 0))

	pygame.draw.line(DISPLAYSURF,GREEN,[0,21],[WINWIDTH,21],3)
	pygame.draw.circle(DISPLAYSURF, GREEN, [580,11], 5, 3)
	
	for i in range(0, NumStar):		# Заполняем список новыми сгенерированными звездами.
		stars.append(new_star())

	while True:
		playerMoveTo = None
		keyPressed = False
				
		for event in pygame.event.get():
			print (event)
			if event.type == pygame.QUIT:
				terminate()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					playerMoveTo = LEFT	
				elif event.key == pygame.K_RIGHT:	
					playerMoveTo = RIGHT
				elif event.key == pygame.K_SPACE:	
					playerMoveTo = FIRE	
				elif event.key == pygame.K_ESCAPE:		
					terminate()	
				
		DISPLAYSURF.fill((0, 0, 0))		# Очищаем экран
		for i in range(0, NumStar):		# Цикл по всем звездам.
			s = stars[i]			    # Запоминаем характеристики звезды из списка
										# Вычисляем текущие координаты звезды
			x = s[0] * 256 / s[2]
			y = s[1] * 256 / s[2]
			s[2] -= speed        			# Изменяем ее координату по Z

			# Если координаты вышли за пределы экрана - генерируем новую звезду.
			if s[2] <= 0 or x <= -WINWIDTH // 2 or x >= WINWIDTH // 2 or y <= -WINHEIGHT // 2 or y >= WINHEIGHT // 2:
				s = new_star()

			if s[3] < 256:			# Если цвет не достиг максимума яркости, увеличиваем цвет.
				s[3] += speed

			if s[3] >= 256:			# Если вдруг цвет стал больше допустимого, то выставляем его как 255
				s[3] = 255

			stars[i] = s				# Помещаем звезду обратно в список звезд.

			# Отображаем звезду на экране.
			x = round(s[0] * 256 / s[2]) + WINWIDTH // 2
			y = round(s[1] * 256 / s[2]) + WINHEIGHT // 2
			pygame.draw.circle(DISPLAYSURF, (s[3], s[3], s[3]), (x, y), 3)
				
		pygame.display.update() # draw DISPLAYSURF to the screen.
		FPSCLOCK.tick(FPS)







# -----------------------------------------------------------------------------------
# Функция генерации новой звезды.
# -----------------------------------------------------------------------------------
def new_star():
    star = [random.randint(0, WINWIDTH) - WINWIDTH // 2, random.randint(0, WINHEIGHT) - WINHEIGHT // 2, 256, 0]
    return star
	
def terminate():
	print ("QUIT")
	pygame.quit()
	sys.exit()
    
if __name__ == '__main__':
    main()
