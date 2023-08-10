
'''
plot three categories of graphs 

1. Compare the cold start time between different applications.
2. Compare the execution time between different inputs for one application.
3. Show the varability of one apploication with a single node. 

'''

import statistics
import numpy as np
from scipy.interpolate import make_interp_spline
#compare the cold start time with different applications (it's related to the dependencies of different applications)

# 110.dynamic-html | Generate dynamic HTML from a template.
# 120.uploader        Python, Node.js        Uploader file from provided URL to cloud storage.
# 210.thumbnailer        Python, Node.js        Generate a thumbnail of an image.
# Multimedia        220.video-processing        Python        Add a watermark and generate gif of a video file.
# Utilities        311.compression        Python        Create a .zip file for a group of files in storage and return to user to download.
# Utilities        504.dna-visualization        Python        Creates a visualization data for DNA sequence.
# Inference        411.image-recognition        Python        Image recognition with ResNet and pytorch.
# Scientific        501.graph-pagerank        Python        PageRank implementation with igraph.
# Scientific        501.graph-mst        Python        Minimum spanning tree (MST) implementation with igraph.
# Scientific        501.graph-bfs        Python        Breadth-first search (BFS) implementation with igraph.


import matplotlib.pyplot as plt

def draw_coldstart():
    # Data
    labels = ["dynamic-html", "uploader", "thumbnailer", "video-processing", "compression", "dna-visualization", "image-recognition",   
    "graph-pagerank",      
    "graph-mst",        
    "graph-bfs"]

    plt.bar(x=[1], height=[0.721], width = 2, color ='r', edgecolor = 'black')
    plt.bar(x=[3], height=[0.907], width = 2, color ='orange', edgecolor = 'black')
    plt.bar(x=[5], height=[1.196], width = 2, color ='purple', edgecolor = 'black')
    plt.bar(x=[7], height=[3.036], width = 2, color ='#778899', edgecolor = 'black')
    plt.bar(x=[9], height=[1.915], width = 2, color ='gold', edgecolor = 'black')
    plt.bar(x=[11], height=[2.934], width = 2, color ='darkgray', edgecolor = 'black')
    plt.bar(x=[13], height=[5.987], width = 2, color ='#6495ED', edgecolor = 'black')
    plt.bar(x=[15], height=[0.3826], width = 2, color ='#00FFFF', edgecolor = 'black')
    plt.bar(x=[17], height=[0.549], width = 2, color ='#FFC0CB', edgecolor = 'black')
    plt.bar(x=[19], height=[0.74], width = 2, color ='#F08080', edgecolor = 'black')
    x = [1,3,5,7,9,11,13,15,17,19]
    _ = plt.xticks(x, labels)
    plt.show()
																					

# compare case 110 501 502 503
def draw_input():
    

    input_size_110 = [10,100,1000,10000,20000,40000,60000,80000,85000,90000,95000,100000]
    execution_time_110 = [0.001769304276,0.001878976822,0.002649784088,0.1615536213,0.279766798,0.6142299175,0.9496650696, 1.376121044,1.438201189,2.507167578,2.537019014,2.723516703]

    times_110 = np.array(input_size_110)
    node_110 = np.array(execution_time_110)
    model0_110 = make_interp_spline(times_110, node_110)
    x_110 = np.linspace(0,100000,24)
    ys0_110 = model0_110(x_110)

    input_size_501=[10,100,1000,10000,20000,40000,60000,80000,85000,90000,95000,100000]
    execution_time_501 = [0.0002963542938,
    0.0006296634674,
    0.01042056084,
    0.2521569729,
    0.7795288563,
    1.367158651,
    2.227839947,
    3.455668211,
    3.685416937,
    3.931820154,
    4.117727995,
    4.793433905]

    times_501 = np.array(input_size_501)
    node_501 = np.array(execution_time_501)
    model0_501 = make_interp_spline(times_501, node_501)
    x_501 = np.linspace(0,100000,23)
    ys0_501= model0_501(x_501)

    #502
    input_size_502=[10,100,1000,10000,20000,40000,60000,80000,85000,90000,95000,100000]
    execution_time_502 = [
        0.000342130661,
    0.0004580020905,
    0.002484083176,
    0.08141732216,
    0.2441539764,
    0.6431322098,
    1.107880831,
    1.59154129,
    1.708641291,
    1.833094358,
    1.976682186,
    2.163918257
    ]

    times_502 = np.array(input_size_502)
    node_502 = np.array(execution_time_502)
    model0_502 = make_interp_spline(times_502, node_502)
    x_502 = np.linspace(0,100000,23)
    ys0_502= model0_502(x_502)

    #503
    input_size_503=input_size_501
    execution_time_503 = [
    0.0002853870392,
    0.0004465579987,
    0.002298116684,
    0.08135533333,
    0.2646849155,
    0.6419961452,
    1.093874454,
    1.553319693,
    1.716982603,
    1.883199692,
    2.011758089,
    2.130761147
    ]
    times_503 = np.array(input_size_503)
    node_503 = np.array(execution_time_503)
    model0_503 = make_interp_spline(times_503, node_503)
    x_503 = np.linspace(0,100000,23)
    ys0_503= model0_503(x_503)


    plt.plot(x_110, ys0_110,color='r',label = "dynamic-html")
    plt.plot(x_501, ys0_501,color='b', label = "graph-pagerank")
    plt.plot(x_502, ys0_502,color='black', label = "graph-mst")
    plt.plot(x_503, ys0_503,color='purple', label = "graph-bfs")
    plt.scatter(input_size_110, execution_time_110,color = 'r')
    plt.scatter(input_size_501, execution_time_501, color = 'b')
    plt.scatter(input_size_502, execution_time_502, color = 'black')
    plt.scatter(input_size_503, execution_time_503, color = 'purple')
    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (/s)")
    plt.legend(loc="upper left")
    plt.show()

def draw_varability():
    
    plt.show()




draw_coldstart()
draw_input()
