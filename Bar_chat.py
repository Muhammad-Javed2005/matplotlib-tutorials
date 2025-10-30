import matplotlib.pyplot as plt 

# For vertical Bar chat: 


# Syntax:
#   plot(x, y, color , width , label)

a = ["A" , "B" ,"C","D","E","F","G","H","I","J"]
b = [23,67,45,98,67,56,24,18,49,34]

plt.bar(a , b ,color= "gray" , width=0.5 , label="Bar Chart")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Sales of Products")
plt.xticks(rotation = 45)
plt.legend()
plt.grid()
plt.show()



# # For Horizontal Bar chart:
# # Syntax:
#         #   plot(x, y, color , width , label)


a = ["A" , "B" ,"C","D","E","F","G","H","I","J"]
b = [23,67,45,98,67,56,24,18,49,34]

plt.barh(a , b , color= "pink" , height=0.5 , label="Bar Chart")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.title("Sales of Products")
plt.legend()
plt.tight_layout()
plt.grid(axis = "x")
plt.show()




