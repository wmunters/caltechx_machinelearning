import numpy as np
import matplotlib.pyplot as plt

d = 2

# draw a random x out of a uniform distribution between -1 and 1
a = 2*(np.random.rand(d)-0.5)
b = 2*(np.random.rand(d)-0.5)


# parametrize the line between points a and b 
slope = (b[1] - a[1])/(b[0] - a[0])
intercept = a[1] - slope*a[0]
x1 = np.arange(start=-1, stop=1, step=.01)
x2 = slope*x1 + intercept
print('slope, intercept = ', slope, intercept)

w0 = intercept
w1 = slope
w2 = -1

# generate a number of N random samples
N = 100
samples = np.zeros((N, d))
for i in range(N):
    samples[i,:] = 2*(np.random.rand(d) - .5)


# Plotting
plt.close('all')
plt.figure()
plt.axhline(y=0, color='0.5', linestyle=':')
plt.axvline(x=0, color='0.5', linestyle=':')

# plot the line and connecting points
plt.axhline(y=0, color='0.5', linestyle=':')
plt.axvline(x=0, color='0.5', linestyle=':')
plt.plot(x1, x2, 'k')
plt.plot(a[0], a[1], 'o', color='k')
plt.plot(b[0], b[1], 'o', color='k')

# For each sample, determine on which side of the line the samples is located
# Draw in the corresponding designated color
for sample in samples:
    if w0 + w1*sample[0] + w2*sample[1] > 0:
        plt.plot(sample[0], sample[1], 'o', color='C1')
    elif w0 + w1*sample[0] + w2*sample[1] < 0:
        plt.plot(sample[0], sample[1], 'o', color='C2')
    else:
        plt.plot(sample[0], sample[1], 'o', color='C3')

# Some plot formatting
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

