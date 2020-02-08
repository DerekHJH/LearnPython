import csv;
from matplotlib import pyplot as plt;
from datetime import datetime;

filename = "death_valley_2014.csv"
with open(filename) as f:
    reader = csv.reader(f);
    header_row = next(reader);#Read one line;
    
    #for index, column_header in enumerate(header_row):#turn a list into a dict 
    #    print(index, column_header);
    
    highs = [];
    dates = [];
    lows = [];
    for row in reader:
        try:
            date = datetime.strptime(row[0], "%Y-%m-%d");
            high = int(row[1]);
            low = int(row[3]);
        except ValueError:
            print("missing!!");
        else:
            dates.append(date);
            highs.append(high);
            lows.append(low);

    fig = plt.figure(dpi = 128, figsize = (10, 6));
    plt.plot(dates, highs, c = "red", alpha = 0.5);#alpha is the level of transparency
    plt.plot(dates, lows, c = "blue", alpha = 0.5);#alpha=0, totally transparent;
    plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1);
    #facecolor is the color of the area within
    plt.title("Daily high and low temperatures - 2014\nDeath Valley, CA", fontsize = 24);
    plt.xlabel("", fontsize = 16);
    fig.autofmt_xdate();#Draw in an oblique way;
    plt.ylabel("Temperature (F)", fontsize = 16);
    plt.tick_params(axis = "both", which = "major", labelsize = 16);
    
    #plt.savefig("haha.png", bbox_inches = "tight");
    plt.show();
