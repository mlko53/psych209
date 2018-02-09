import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from rand_mdots import rand_mdots

def viz_rand_mdots(mdots, radius):
	fig = plt.figure()
	ax = plt.axes(xlim=(-radius / 2, radius*2.5), ylim=(-radius/2, radius*2.5))
	ax.set_axis_bgcolor("black")
	ax.set_aspect('equal')
	ax.xaxis.set_visible(False)
	ax.yaxis.set_visible(False)
	particles, = ax.plot([], [], 'wo', ms=1)

	def init():
		particles.set_data([], [])
		return particles,

	def animate(i, mdots=mdots):
		coord = mdots[:,:,i-1]
		x = []
		y = []
		for i in range(0, coord.shape[0]):
			for j in range(0, coord.shape[1]):
				if coord[i, j] == 1:
					x.append(i)
					y.append(j)
		particles.set_data(x, y)
		return particles,

	anim = animation.FuncAnimation(fig, animate, init_func=init,
							   frames=1000, interval=1/100, blit=True, repeat=False)

	fig.tight_layout()
	plt.show()

if __name__ == "__main__":
	radius = 128
	mdots = rand_mdots(np.pi, coherence = 0.2, radius=radius)
	viz_rand_mdots(mdots, radius)