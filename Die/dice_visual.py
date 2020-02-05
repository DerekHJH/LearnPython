from die import Die;
import pygal;

die_1 = Die();
die_2 = Die(10);

results = [];
for roll_num in range(100000):
    result =die_1.roll() + die_2.roll();
    results.append(result);

frequencies = [];
for value in range(1, die_1.num_sides + die_2.num_sides + 1):
    frequency = results.count(value);
    frequencies.append(frequency);

hist = pygal.Bar();
hist.x_labels = list(map(lambda x:str(x), list(range(1, die_1.num_sides + die_2.num_sides + 1))));
hist.x_title = "Result";
hist.y_title = "Frequency of Result";

hist.add("D6 + D6", frequencies);
hist.render_to_file("dice_visual.svg");
