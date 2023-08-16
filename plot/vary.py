import statistics
import numpy as np
import matplotlib.pyplot as plt
def draw_varability(data, case,label):
    # Calculate variance and standard deviation
    variance = np.var(data)
    std_dev = np.std(data)
    mean = np.mean(data)
    seasons = ['1','2','3','4','5','6','7','8','9','10']
    # A plot for Aguero
    plt.plot(seasons, data, marker='o', color='#003366',label = label)
    plt.axhline(y=mean, color='#6684a3', linestyle='--', label='mean = %.3fs'%(mean))
    
    # label for x-axis, y-axis
    plt.xlabel('Test#')
    plt.ylabel('Execution Time (/s)')
    # title of a plot
    plt.title('Variability of case %s (standard deviation: %.3f)'%(case,std_dev))
    # explanation(symbol) for a graph
    plt.legend()
    # This will pop up the graph
    plt.show()
#print the data for just dynamic template 
data110 = [2.724, 2.615, 2.615, 2.626, 2.612, 
2.624, 2.270, 2.558, 2.612, 2.599]
draw_varability(data110,1,'Dynamic HTML')
data120 = [0.493, 0.466, 0.466,0.495,0.506,0.493,0.518,0.434,0.553,0.511]
draw_varability(data120,2,'Image Uploader')
data210 =[0.313,0.283,0.263, 0.251, 0.337, 0.295, 0.317,0.302,0.351,0.283]
draw_varability(data210,3,'Thumbnailer')
data220 = [7.565,7.556,7.351, 7.556, 7.532, 7.921,7.534,7.486,7.521,7.525]
draw_varability(data220,4,'Video Processing')

data311 = [6.402,6.868,7.183,6.811, 6.876,6.532, 6.668,6.832,6.739,7.210]
draw_varability(data311,5,'Compression')
data504=[9.180,	9.212, 9.113,9.246,8.934,9.181,9.122,9.297,9.039,9.129] 
draw_varability(data504,6,'DNA Visualization')
data411=[1.735,1.755,	1.766,	1.829,	1.848,	1.722,	1.785,	1.839,	1.764,	1.796]
draw_varability(data411,7,'Image Recognition')

data501=[4.793,	4.742, 4.478, 4.553,4.515,4.54,4.515,4.473,4.54,4.418] 
draw_varability(data501,8,'Graph Pagerank')
data502=[2.164,	2.123,2.172,2.179,2.118,2.112,2.149,2.144,2.127,2.148] 
draw_varability(data502,9,'Graph MST')
data503=[2.131,2.015,2.051,2.003,2.015,2.101,2.034,2.212,2.013,2.042] 
draw_varability(data503,10,'Graph BFS')
