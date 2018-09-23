#!/usr/bin/env python

import cairocffi as cairo
import random
from numpy import pi
import imageio

# with imageio.get_writer('/path/to/movie.gif', mode='I') as writer:
#     for filename in filenames:
#         image = imageio.imread(filename)
#         writer.append_data(image)

class Walker:

	def __init__(self, width, height):
		self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
		self.context = cairo.Context(self.surface)
		self.context.set_source_rgb(1, 1, 1)
		self.context.paint()

		self.writer = imageio.get_writer('animated.gif', mode='I')

		self.radius = 5
		self.x = 10
		self.y = 10
		self.num = 1;

	def circle(self,x,y,r,fill=False):
		self.context.set_source_rgb(0, 0, 0)
		self.context.arc(x,y,r,0,(pi*2))
		if fill:
		  self.context.fill()
		else:
		  self.context.stroke()


	def draw(self):
		self.circle(self.x, self.y, self.radius, fill=True)
		print('img_{}.png'.format(self.num))
		self.surface.write_to_png('img_{}.png'.format(self.num))
		image = imageio.imread('img_{}.png'.format(self.num))
		self.writer.append_data(image)
		self.num += 1


	def step(self):
		random_num = random.random()

		if random_num < 0.4 :
			#high probability it moves down
			#take a step down
			self.y += self.radius * 2
		elif random_num < 0.6 :
			#take a step right
			self.x += self.radius * 2
		elif random_num < 0.8 :
			#take a step left
			self.x -= self.radius * 2
		elif random_num <= 1 :
			#take a step up
			self.y -= self.radius * 2

		self.draw()


walker = Walker(200, 200)
for i in range(0, 10):
	walker.step()

# size = (500,500)
# white = (255,255,255)
# black = (0,0,0)
#
# class Walker(object):
# 	"""
# 	"""
#
# 	def __init__(self, width, height):
# 		self.x = width/2.0
# 		self.y = height/2.0
# 		self.width = 2
# 		self.height = 2
# 		self.num = 1;
#
# 		self.first_img = Image.new("RGB", size, white)
# 		self.prev_img = self.first_img
# 		self.first_img = self.draw()
# 		self.imgs = [self.first_img]
#
# 	def draw(self):
# 		img = self.prev_img.copy()
# 		draw = ImageDraw.Draw(img)
# 		position = [(self.x - self.width), (self.y - self.height), (self.x + self.width), (self.y + self.height)]
# 		draw.ellipse(position, black, black)
# 		#img.save("walk" + str(self.num) + ".jpg", "JPEG")
# 		return img
#
# 	def step(self):
# 		#random_num = random.randrange(4)
# 		random_num = random.random()
# 		print("random number", random_num)
# 		self.num += 1
# 		if random_num < 0.4 :
# 			#high probability it moves down
# 			#take a step down
# 			self.y += self.height * 2
# 			img = self.draw()
# 			self.imgs.append(img)
# 			self.prev_img = img
# 		elif random_num < 0.6 :
# 			#take a step right
# 			self.x += self.width * 2
# 			img = self.draw()
# 			self.imgs.append(img)
# 			self.prev_img = img
# 		elif random_num < 0.8 :
# 			#take a step left
# 			self.x -= self.width * 2
# 			img = self.draw()
# 			self.imgs.append(img)
# 			self.prev_img = img
# 		elif random_num <= 1 :
# 			#take a step up
# 			self.y -= self.height * 2
# 			img = self.draw()
# 			self.imgs.append(img)
# 			self.prev_img = img
#
# #initial position = [(self.x - self.width), (self.y - self.height), (self.x + self.width), (self.y + self.height)]
#
# walker = Walker(500, 500)
# for i in range(0, 100):
# 	walker.step()
# print("number of images", len(walker.imgs))
#
# im = walker.imgs[0]
# im.save("walker.gif", save_all=True, append_images=walker.imgs, duration=300)
