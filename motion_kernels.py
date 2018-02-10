import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math


def motion_kernel(direction, dim=(64,64), time_depth = 3, speed=5):
	'''
	time_depth has to be odd
	'''
	motion_kernel = np.zeros(shape=(dim[0], dim[1], time_depth))
	kernel = genGabor((dim[0] - (time_depth - 1)*speed - 1, dim[1] - (time_depth - 1)*speed - 1), 0.6, direction, func=np.cos)
	x_trans = round(np.cos(direction) * speed)
	y_trans = round(np.sin(direction) * speed)

	center_idx = int((time_depth-1)/2)

	left_pad = center_idx * speed - x_trans * center_idx
	down_pad = center_idx * speed - y_trans * center_idx

	print(kernel.shape)

	for t in range(0, time_depth):

		right_pad = dim[0] - kernel.shape[0] - left_pad
		up_pad = dim[1] - kernel.shape[1] - down_pad

		temp = np.pad(kernel, ((math.ceil(left_pad), math.ceil(right_pad)),(math.ceil(down_pad), math.ceil(up_pad))), 'constant', constant_values = 0)
		motion_kernel[:,:,t] = temp

		left_pad += x_trans
		down_pad += y_trans
	
	return motion_kernel

def genGabor(sz, omega, theta, func=np.cos, K=np.pi):
    radius = (int(sz[0]/2.0), int(sz[1]/2.0))
    [x, y] = np.meshgrid(range(-radius[0], radius[0]+1), range(-radius[1], radius[1]+1))

    x1 = x * np.cos(theta) + y * np.sin(theta)
    y1 = -x * np.sin(theta) + y * np.cos(theta)
    
    gauss = omega**2 / (4*np.pi * K**2) * np.exp(- omega**2 / (8*K**2) * ( 4 * x1**2 + y1**2))
#     myimshow(gauss)
    sinusoid = func(omega * x1) * np.exp(K**2 / 2)
#     myimshow(sinusoid)
    gabor = gauss * sinusoid
    return gabor

############visualize###############

def myimshow(I, **kwargs):
    # utility function to show image
    plt.figure();
    plt.axis('off')
    plt.imshow(I, cmap=plt.gray(), **kwargs)

def viz_motion_kernels(motion_kernel):
	fig = plt.figure()

	im = plt.imshow(motion_kernel[:,:,0], animated = True)
	def animate(i, motion_kernel = motion_kernel):
		im = motion_kernel[:,:, i - 1]
		return im

	anim = animation.FuncAnimation(fig, animate,
							   frames=motion_kernel.shape[2], interval=100, blit=True, repeat=False)

	plt.show()

if __name__ == "__main__":
	#kernel = genGabor((22,22), 0.4, np.pi / 4)
	motion_kernel = motion_kernel(np.pi / 4)
	myimshow(motion_kernel[:,:,2])
	plt.show()
	#viz_motion_kernels(motion_kernel)
