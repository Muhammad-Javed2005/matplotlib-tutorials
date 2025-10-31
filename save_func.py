import matplotlib.pyplot as plt 


# Syntax:
    #  plt.savefig("File_name.extension" , dpi = value , bbox_inches = "tight" , pad_inches = 0.1)

region = ["North" , "South" ,"East" ,"West"]
value = [10, 15, 7, 12]

plt.pie(value ,labels = region , autopct = '%1.1f%%' , colors = ["gold" ,"skyblue" ,"lightgreen" ,"coral"] )
plt.title("Revenue Constribution of Region")
plt.savefig("Pie_Chart_001.png" , dpi = 300 , bbox_inches = "tight" , pad_inches = 0.1)

plt.show()



