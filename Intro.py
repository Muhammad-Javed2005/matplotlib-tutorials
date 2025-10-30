import matplotlib.pyplot as plt 



# Simple Graph 01:
x = [1,2,3,4,5,6,7,8,9,10,11,12,14,15]
y = [12,34,56,34,56,76,43,87,98,56,43,44,23,67]

# plt.plot(x,y)
# plt.show()

# Simple Graph 02:

name= ["Javed", "Fabha", "Mehwish", "Rida", "Qurratulain","Zunaira", "Anus", "Ammad", "Rafay", "Muzna" ]
age =  [22, 21, 23, 24, 25, 20, 22, 21, 24, 23]

plt.plot(age , name)
plt.show()



# Simple Graph 03:

name= ["Javed", "Fabha", "Mehwish", "Rida", "Qurratulain","Zunaira", "Anus", "Ammad", "Rafay", "Muzna" ]
roll_no =  [201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
plt.plot(roll_no , name)
plt.show()



#  1. Import the required library
# matplotlib.pyplot is used for creating static plots like line graph, bar chart, etc.


#  2. Data Points: (x, y) values represent actual plotted points
x = [1, 2, 3, 4, 5]              # X-axis values → input
y = [10, 20, 15, 25, 30]         # Y-axis values → output



# 3. Figure: This creates the full window or canvas for plotting
plt.figure(figsize=(8, 5))       # Optional: define the size of the plot window



#  4. Plot: This function draws a line graph connecting the data points
plt.plot(
    x, y,
    label="Sales",               # ➤ Legend label
    color='green',               # ➤ Color of the line
    marker='o',                  # ➤ Marker shape (o = circle)
    linestyle='--',              # ➤ Line style (dashed)
    linewidth=2                  # ➤ Thickness of the line
)


#  5. Marker: Used to highlight each data point on the graph
# ➤ marker='o' means circle, 's'=square, 'D'=diamond, 'x'=cross, etc.



#  6. Line Style: Controls how the line appears
# ➤ '-', '--', ':', '-.' are valid styles



#  7. Color: You can use named colors like 'red', 'blue', or short codes like 'r', 'b', etc.



#  8. X and Y Axis Labels
plt.xlabel("Days")              # Label for X-axis
plt.ylabel("Sales Amount")      # Label for Y-axis



# 9. Title: Adds a title to the graph
plt.title("Daily Sales Report")



# 10. Grid: Adds background grid lines for better visual guidance
plt.grid(True)



# 11. Legend: Displays labels for plot lines
plt.legend()



# 12. Show the final plot (must be last)
plt.show()



# 13. Keyword Arguments:
# All the customization options (like color, marker, label) are keyword arguments in Python.
# Example: color='green', linestyle='--', marker='o'



# 14. Object-Oriented API (Not used here, but allows more control using axes objects)
# For example:
# fig, ax = plt.subplots()
# ax.plot(x, y)



# Bar chart using same data
x = ["Mon", "Tue", "Wed", "Thu", "Fri"]
y = [100, 150, 130, 120, 180]



plt.figure(figsize=(8, 4))              # Figure (canvas)
plt.bar(x, y, color='skyblue')          # Bar plot
plt.xlabel("Weekdays")                  # X-axis label
plt.ylabel("Visitors")                  # Y-axis label
plt.title("Website Traffic Report")     # Title
plt.grid(axis='y')                      # Grid lines only on y-axis
plt.show()






