from random import choice;

class RandomWalk():
    def __init__(self, max_points = 5000):
        self.max_points = max_points;
        self.x = [0];
        self.y = [0];
    def fill_walk(self):
        while(len(self.x) < self.max_points):
            x_dir = choice([1, -1]);
            x_dis = choice(list(range(0,5)));
            x_step = x_dir * x_dis;
            
            y_dir = choice([1, -1]);          
            y_dis = choice(list(range(0,5)));
            y_step = y_dir * y_dis;
             
            if(x_step == 0 and y_step == 0):
                continue;

            x_next = self.x[-1] + x_step;
            y_next = self.y[-1] + y_step;

            self.x.append(x_next);
            self.y.append(y_next);
