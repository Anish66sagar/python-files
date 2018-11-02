import csv
import matplotlib.pyplot as plt
x = []
y = []
with open('excel2.csv','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))
plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Intersting Graph\nCheck It Out')
plt.legend()
plt.show()