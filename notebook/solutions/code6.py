### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

x0 = np.array([-5,-4])
res = sopt.fmin_ncg(func, x0, fprime=func_der, fhess=func_hess, retall=True)
xopt = res[0]
steps = np.array(res[1])

print(steps)
X0 = np.arange(-6,6,0.1)
X1 = np.arange(-6,6,0.1)
levels = np.array([0.15, 0.2, 0.25, 0.5, 1., 2., 3., 4., 5.])
plot_contours_func(func,X0,X1,levels=levels,xp=steps.T,plot_line=True,add_levels=False)

