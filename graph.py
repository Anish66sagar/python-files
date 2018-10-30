import matplotlib.pyplot as plt
# coordinate of left side of bars
left=[1,2,3,4,5]
#height of the bars
height=[10,24,36,40,5]
#labels for par chart
tick_label=['one','two','three','four','five']
#plotting a bar chart
plt.bar(left,height,tick_label=tick_label,width=0.8,color=['red','yellow'])
#making the graph
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("second graph")
plt.show()