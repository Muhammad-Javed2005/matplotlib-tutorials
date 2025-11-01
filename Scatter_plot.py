import matplotlib.pyplot as plt 

# Syntax:
    # plt.scatter(x,y , color = "color_name" , marker= "marker" ,label = "label_name")


hour_studied = [1,2,3,4,5,6,7]
score1 = [90,85,88,92,89,95,98]
score2 = [56,87,46,90,76,98,67]

plt.scatter(hour_studied,score1, color = "blue" , marker = "o" , label = "Class A")
plt.scatter(hour_studied,score2, color = "orange" , marker = "o" , label = "Class B")
plt.xlabel("Hour Studied")
plt.ylabel("Score")
plt.title("Comparsion of two Classes")
plt.legend()
plt.grid(True)
plt.show()



