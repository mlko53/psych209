import numpy as np
import random
import math

def rand_mdots(true, coherence, num=300, speed = 5, time=1000, radius = 128):
	'''
	args: 
		num: number of moving dots
		coherence: percentage of nonrandom motion
		true: true direction
		directions: (array) possible directions of moving dot
	output:
		mdots: array of directions of moving dots'
	'''

	directions = true * np.ones(shape=(num, ))
	for i in range(0,  round(num * (1 - coherence))):
 		directions[i] = 2 * np.pi * random.random()

	r = [radius * random.random() for i in range(0, num)]
	theta = [2 * np.pi * random.random() for i in range(0, num)]
	x = [i * np.cos(j) for i, j in zip(r, theta)] ### ranges between -r and r
	y = [i * np.sin(j) for i, j in zip(r, theta)] ### ranges between -r and r

	mdots = np.zeros(shape=(2*radius, 2*radius, time))
	for i in range(0, time):
		x += speed * np.cos(directions)
		y += speed * np.sin(directions)
		for j in range(0, num):
	 		if x[j]**2 + y[j]**2 > radius**2:
	 			if x[j] - .5 * speed * np.cos(directions[j]) < 0:
	 				my = y[j] - .5 * speed * np.sin(directions[j])
	 				mx = -(x[j] - .5 * speed * np.cos(directions[j]))
	 				alpha = np.pi - np.arctan(my/mx)
	 			else:
	 				my = y[j] - .5 * speed * np.sin(directions[j])
	 				mx = x[j] - .5 * speed * np.cos(directions[j])
	 				alpha = np.arctan(my/mx)
	 			dx = x[j] - radius * np.cos(alpha)
	 			dy = y[j] - radius * np.sin(alpha)
	 			x[j] = - radius * np.cos(alpha) + dx
	 			y[j] = - radius * np.sin(alpha) + dy
		mdots[[min(math.floor(xi+ radius), radius*2 - 1) for xi in x], [min(math.floor(yi + radius), radius*2 - 1) for yi in y], i] = 1
	return mdots

if __name__ == "__main__":
	print("Testing rand_mdots")
	print("-----------------------------")
	mdots = rand_mdots(np.pi, 0.2)
	print('Number of dots in each time')
	print(np.sum(mdots, axis = (0,1)))
	print("testing qualitative visualization")