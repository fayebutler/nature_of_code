#!/usr/bin/env python

import cairocffi as cairo
import random
from numpy import pi
import imageio


class Walker:

	def __init__(self, width, height):
		self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
		self.context = cairo.Context(self.surface)
		self.context.set_source_rgb(1, 1, 1)
		self.context.paint()

		self.writer = imageio.get_writer('animated.gif', mode='I')

		self.radius = 5
		self.x = width/2.0
		self.y = height/2.0
		self.num = 1;
		self.positions = []

	def circle(self, x, y, r, fill=False):
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

		while (self.x, self.y) in self.positions:
			print(" ({}, {}) is in positions".format(self.x, self.y))
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

		self.positions.append((self.x, self.y))
		self.draw()


walker = Walker(200, 200)
for i in range(0, 30):
	walker.step()
