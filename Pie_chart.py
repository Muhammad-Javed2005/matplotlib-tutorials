import matplotlib.pyplot as plt 


# Syntax:
#   plot(value , label = label_list , colors = color_list , autopct = %1.1f%% )



region = ["North" , "South" ,"East" ,"West"]
value = [10, 15, 7, 12]

plt.pie(value ,labels = region , autopct = '%1.1f%%' , colors = ["gold" ,"skyblue" ,"lightgreen" ,"coral"] )
plt.title("Revenue Constribution of Region")
plt.show()


a = ["A" , "B" ,"C","D","E","F","G","H","I","J"]
b = [23,67,45,98,67,56,24,18,49,34]


plt.pie(b ,labels = a , autopct = '%1.1f%%' )
plt.show()


