import matplotlib.pyplot as plt;

x = list(range(1, 1001));
y = [x*x for x in range(1, 1001)];

#plt.plot(x, y, linewidth = 5);#Set the width of the drawn line;
plt.title("Square Numbers", fontsize = 24);
plt.xlabel("Value", fontsize = 14);
plt.ylabel("Square of Values", fontsize = 14);
plt.tick_params(axis = "both", which="major", labelsize = 14);#Set the type of the scale;

#plt.scatter(4, 4, s = 200);#Draw a single point at this coordinates and set the size;
#plt.scatter(x ,y, c = "red", edgecolor = "none", s = 40);
#plt.scatter(x ,y, c = [0.5, 0.5, 0.5], edgecolor = "none", s = 40);#RGB to 0 darker
plt.scatter(x ,y, c = y, cmap = plt.cm.Reds, edgecolor = "none", s = 40);
#y with smaller value is drawn with lighter color and vise versa; Blues, Reds....

plt.axis([0, 1100, 0, 1100000]);#The range of x and y to be presented;


plt.show();
#plt.savefig("Squares.png", bbox_inches = "tight");
#bbox to eliminate the extra white space

