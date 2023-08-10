
'''
plot three categories of graphs 

1. Compare the cold start time between different applications.
2. Compare the execution time between different inputs for one application.
3. Show the varability of one apploication with a single node. 

'''

import statistics
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

# Data
labels = ["dynamic-html", "uploader", "thumbnailer", "video-processing", "compression", "dna-visualization", "image-recognition",   
"graph-pagerank",      
"graph-mst",        
"graph-bfs"]


# cold_start = [0.721, 0.907, 1.196, 3.036, 1.915, 2.934, 5.987 ,0.3826,0.549,0.74]  # Example values for the bars

# # Create a bar graph
# plt.bar(labels, cold_start)

# # Adding labels and title
# plt.xlabel("Applications")
# plt.ylabel("Cold Start Time (/s)")
# plt.title("Cold start times with different applications")

# # Display the graph
# plt.show()

#another way for plotting

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
execution_time_100000 = [2.723516703, 2.614780188, 2.614917755, 2.626345873, 2.61181426, 2.624297857, 2.270168543, 2.558188915, 2.612315416, 2.599187136]	
print("Variance of sample set is % s" %(statistics.variance(execution_time_100000)))	
print("mean of sample set is %s"%(statistics.mean(execution_time_100000)))	

