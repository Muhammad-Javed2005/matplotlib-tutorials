import matplotlib.pyplot as plt 



# Syntax:
#       plt.hist(data , bins=number_of_bins , color = "color_name" , endgcolor = "color_of_edge")
#       plt.show()

data = [23,6,78,65,78,90,7,45,67,45,34,78,90,7,6,56,27,45,87,45,17,38,37,97,35,67,86,34,88,25,37,14,89,57,56]
plt.hist(data , bins=10 , color = "purple" , edgecolor = "black")
plt.show()


