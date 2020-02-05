import matplotlib.pyplot as plt;
from random_walk import RandomWalk;
while True:
    rw = RandomWalk();
    rw.fill_walk();

    plt.figure(figsize = (10, 6));
    #Unit --- inches assuming that 80 pixels/inch. Put this before any drawing;

    point_numbers = list(range(rw.max_points));
    #plt.plot(rw.x, rw.y, linewidth = 0.5);#Make comparison between plot and scatter;
    plt.scatter(rw.x, rw.y, c = point_numbers, cmap = plt.cm.Blues, edgecolor = "none", s = 1);
    plt.scatter(0, 0, c = "green", edgecolor = "none", s = 10);
    plt.scatter(rw.x[-1], rw.y[-1], c = "red", edgecolor = "none", s = 10);

    plt.axes().get_xaxis().set_visible(False);
    plt.axes().get_yaxis().set_visible(False);
    #Make the x and y axes invisible;
    
    plt.savefig("rw.png", bbox_inches = "tight");
    #plt.show();

    keep_running = input("Make another walk? (y/n):");
    if(keep_running == 'n'):
        break;

