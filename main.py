Web VPython 3.2

box(color = vec(0,0,1), size = vec(20,30,1))
box(texture = textures.wood, pos = vec(-10,0,1), size = vec(1,31,1))
box(texture = textures.wood, pos = vec(0,15,1), size = vec(20,1,1))
box(texture = textures.wood, pos = vec(10,0,1), size = vec(1,31,1))
box(texture = textures.wood, pos = vec(0,-15,1), size = vec(20,1,1))
ball1=sphere(pos=vec(3,0,0),v=vec(2,0,0), color = color.orange)
ball2= sphere(pos=vec(-9,0,0), color = color.red)
ball3= sphere(pos=vec(-2,6,0), color = color.red)
import random

ball1.v=vec(random.uniform(-5,5),random.uniform(-5,5),0)
ball2.v=vec(random.uniform(-5,5),random.uniform(-5,5),0)
ball3.v=vec(random.uniform(-5,5),random.uniform(-5,5),0)
       
while True :
    rate(100)
    if ball1.pos.x >  10 :
        ball1.v.x = -ball1.v.x
    if ball1.pos.x <  -10 :
        ball1.v.x = -ball1.v.x
    if ball1.pos.y >  15 :
        ball1.v.y = -ball1.v.y
    if ball1.pos.y <  -15 :
        ball1.v.y = -ball1.v.y
    ball1.pos = ball1.pos + ball1.v * 0.01


    if ball2.pos.x >  10 :
        ball2.v.x = -ball2.v.x
    if ball2.pos.x <  -10 :
        ball2.v.x = -ball2.v.x
    if ball2.pos.y >  15 :
        ball2.v.y = -ball2.v.y
    if ball2.pos.y <  -15 :
        ball2.v.y = -ball2.v.y
    ball2.pos = ball2.pos + ball2.v * 0.01
