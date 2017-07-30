#贪吃蛇TIPS
Q：重新生成苹果
A：首先确定，本轮蛇的更新，蛇是否吃到苹果
   吃到的话为苹果重新生成位置
   可以使用使用随机数生成
   import random 
   random.randint()

Q: 蛇不能直接掉头
A：在按键回调函数中判断，如果当前蛇和回调函数需要设置的方向为同向或反向，则不必更新蛇运行的方向
   
Q：蛇吃到自己判断失败
A: 身体.count(蛇头)是否大于2，大于2的话说明蛇咬到了自己
   

#参考 example.py学习如何贴图，显示字符
#如何在pygame里面显示字符
font = pygame.font.Font(None, 100) #字体None=默认字体，字号 
text = font.render("XXXXXX", True, [255,0,0]) # render(text, antialias, color, background=None) 
screen.blit(text, [x, y]) #显示对象 位置

#如何在pygame里面显示图片
img = pygame.image.load("beach_ball.png") #图片路径，一般和python源文件放在一个目录下
screen.blit(img, [x, x])

