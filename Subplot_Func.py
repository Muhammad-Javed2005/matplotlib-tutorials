import matplotlib.pyplot as plt 


# Syntax:
#   plt.subplot(number_rows , number_column , index)
#   plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st plot 


x = [ 1,2,3,4,5,6,7,8,9,10]
y = [ 12,56,87,45,98,90,45,26,87,67]

plt.subplot(1,2,1) # 1 row, 2 columns, 1st plot
plt.plot(x,y)
plt.title('Line Chart')
plt.xlabel("Roll No")
plt.ylabel("Percentage")



plt.subplot(1,2,2) # 1 row, 2 columns, 2nd plot
plt.bar(x,y) # 'r' is for red color
plt.title('Bar Chart')
plt.xlabel("Roll No")
plt.ylabel("Percentage")

plt.show()




# fig , ax = plt.subplots(number_of_rows , number_of_columns , figsize = (width , height))



fig , ax = plt.subplots(1,2, figsize = (10,5))

a = [1,2,3,4,5]
b = [12,56,87,45,98]

ax[0].plot(a,b)
ax[0].set_title('Line Chart')
ax[0].set_xlabel("Roll No")
ax[0].set_ylabel("Percentage")

ax[1].bar(a,b)
ax[1].set_title('Bar Chart')
ax[1].set_xlabel("Roll No")
ax[1].set_ylabel("Percentage")


fig.suptitle("Comparsion of Line and Bar Chart")

plt.tight_layout()
plt.show()

