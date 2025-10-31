import matplotlib.pyplot as plt 


x = ["Mon" , "Tue" , "Wed" , "Thu" , "Fri" , "Sat" , "Sun"]
y = [10 , 15 , 7 , 12 , 20 , 18 ,34]

# plt.plot(x,y)

# plt.xlabel("Days")
# plt.ylabel("Values")
# plt.title("Plotting Days and Values")
# plt.show()



# Syntax:
#      plt.plot(x , y ,color='color_name' , linestyle = "line_style" , linewidth = value , marker = "marker" , markersize = value ,   label = "Lable_name ")

#      plt.xlabel("text") -> to set the label of x-axis
#      plt.ylabel("text") -> to set the label of y-axis
#      plt.title("text") -> to set the title of the plot
#      plt.legend(loc = "upper left" or "lower right") -> to display the legend of the plot
#      plt.show() -> to display the plot
#      plt.grid(color='color_name' , linestyle = "line_style" , linewidth = value ) -> to display the grid of the plot
#      plt.xticks(rotation = 45) -> to rotate the x-axis labels by 45 degree
#      plt.yticks(rotation = 45) -> to rotate the y-axis labels by 45 degree
#      plt.xticks(old_value , new_value) -> to change the value of x-axis labels
#      plt.yticks(old_value , new_value) -> to change the value of y-axis labels

#      plt.xlim(start_point , end_point) -> to set the range of x-axis
#      plt.ylim(start_point , end_point) -> to set the range of y-axis


a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
b=[123,456,768,567,876,234,627,896,456,735,147,729,360,901,76]

plt.plot(a,b, color = "Red" , linestyle = "--" , linewidth = 2 , marker = "*" , label = "2025 Sales Data")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.grid(color = "Grey" , linestyle = "--" , linewidth = 0.5 )
plt.legend(loc = "upper left")
plt.title("Plotting Days and Sales")
plt.xlim(3,12)
plt.xticks([3,4,5,6,7,8,9,10,11,12] , ["D1" ,"D2","D3", "D4","D5","D6","D7","D8","D9","D10"])
plt.xticks(rotation = 45)
plt.yticks(rotation = 45)
plt.ylim(0,5000)
plt.show()









# -----------------------------------------------
# Plotting sales data with custom line styling
# -----------------------------------------------

# ➤ color: Sets the color of the line.
#     Common options: 'red', 'blue', 'green', 'black', 'orange', etc.
#     Also supports short codes: 'r', 'g', 'b', 'k', 'y'
#     Recommended professional colors: 'blue', 'black', 'darkgreen', 'gray'

# ➤ linestyle: Defines the style of the line connecting data points.
#     '-'  : Solid line (default, most commonly used in reports)
#     '--' : Dashed line (often used for projections or comparisons)
#     '-.' : Dash-dot line
#     ':'  : Dotted line

# ➤ linewidth: Sets the thickness of the line.
#     Recommended values:
#         1    → thin line
#         1.5  → medium (commonly used)
#         2+   → thick, for emphasis

# ➤ marker: Adds a symbol at each data point.
#     'o'  : Circle      (professional look)
#     's'  : Square
#     '^'  : Triangle up
#     '*'  : Star        (used for highlight or decoration)
#     'x', '+' : Cross, plus (rarely used)

# ➤ label: Used for legend to identify what this line represents.
#     Call plt.legend() to display it on the chart.

# ➤ Extra tips (optional professional styling):
#     plt.grid(True)            → adds background grid
#     plt.tight_layout()        → adjusts layout for no overlap
#     plt.figure(figsize=(x,y)) → sets custom size

