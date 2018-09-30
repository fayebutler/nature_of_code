#!/usr/bin/env python

import cairocffi as cairo
import random
from numpy import pi
import imageio

width = 200
height = 200

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
context = cairo.Context(surface)
context.set_source_rgb(1, 1, 1)
context.paint()

# writer = imageio.get_writer('animated.gif', mode='I')

# image = imageio.imread('img_{}.png'.format(self.num))
# writer.append_data(image)

def fractal_tree(starting_length, length_scaling):

    context.set_source_rgb(0, 0, 0)
    context.save()
    context.translate((200/2), 200)

    def branch(len):

        context.set_source_rgb(0, 0, (len*2)/100)
        context.set_line_width(len/12)

        context.move_to(0, 0)
        context.line_to(0, -len)
        context.stroke()
        context.translate(0, -len)

        len *= length_scaling;

        if len > 2:

            n = random.randint(1, 5)

            for i in range(0, n):
                context.save()
                rot = random.uniform(-pi/2, pi/2)
                context.rotate(rot)
                branch(len)
                context.restore()

    branch(starting_length)
    context.restore()


fractal_tree(50, 0.66)


num = 1
surface.write_to_png('img_{}.png'.format(num))
