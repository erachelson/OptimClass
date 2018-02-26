### WRITE YOUR CODE HERE
# If you get stuck, uncomment the line above to load a correction in this cell (then you can execute this code).

x0 = np.array([-0.8,-0.7])
res = sopt.fmin_cg(func1, x0, retall=True, disp=True)
xopt = res[0]
steps = np.array(res[1])

print(steps)
X0 = np.arange(-1,1,0.05)
X1 = np.arange(-1,1,0.05)
plot_contours_func(func1,X0,X1,xp=steps.T,plot_line=True,add_levels=True)
