from PIL import Image, ImageDraw
import random

size = (500,500)
white = (255,255,255)
black = (0,0,0)

class Walker(object):
	"""
	"""
	
	def __init__(self, width, height):
		self.x = width/2.0
		self.y = height/2.0
		self.width = 2
		self.height = 2
		self.num = 1;
		
		self.first_img = Image.new("RGB", size, white)
		self.prev_img = self.first_img
		self.first_img = self.draw()
		self.imgs = [self.first_img]
		
	def draw(self):
		img = self.prev_img.copy()
		draw = ImageDraw.Draw(img)
		position = [(self.x - self.width), (self.y - self.height), (self.x + self.width), (self.y + self.height)]
		draw.ellipse(position, black, black)
		#img.save("walk" + str(self.num) + ".jpg", "JPEG")
		return img 
		
	def step(self):
		#random_num = random.randrange(4)
		random_num = random.random()
		print("random number", random_num)
		self.num += 1
		if random_num < 0.4 :
			#high probability it moves down
			#take a step down
			self.y += self.height * 2
			img = self.draw()
			self.imgs.append(img)
			self.prev_img = img
		elif random_num < 0.6 :
			#take a step right
			self.x += self.width * 2
			img = self.draw()
			self.imgs.append(img)
			self.prev_img = img
		elif random_num < 0.8 :
			#take a step left
			self.x -= self.width * 2
			img = self.draw()
			self.imgs.append(img)
			self.prev_img = img
		elif random_num <= 1 :
			#take a step up
			self.y -= self.height * 2
			img = self.draw()
			self.imgs.append(img)
			self.prev_img = img

#initial position = [(self.x - self.width), (self.y - self.height), (self.x + self.width), (self.y + self.height)]

walker = Walker(500, 500) 
for i in range(0, 100):
	walker.step()
print("number of images", len(walker.imgs))

im = walker.imgs[0]
im.save("walker.gif", save_all=True, append_images=walker.imgs, duration=300)
