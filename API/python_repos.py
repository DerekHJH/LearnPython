import requests;
import pygal;
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS;


url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
#Use the API, which has speed limit
#api.github.com/rate_limit
r = requests.get(url);
print("Status Code:", r.status_code);
#If the code = 200, then the response is successful;

response_dict = r.json();

print("total_count:", response_dict["total_count"]);


repo_dicts = response_dict["items"];
print("Number of items:", len(repo_dicts));

'''
repo_dict = repo_dicts[0];
print("Number of Keys in one item:", len(repo_dict));

print("\nSelected information about each repository:");
for repo_dict in repo_dicts:
    print("\nName:", repo_dict["name"]);
    print("Owner:", repo_dict["owner"]["login"]);
    print("Stars:", repo_dict["stargazers_count"]);
    print("Repository:", repo_dict["html_url"]);
    print("Description:", repo_dict["description"]);
'''

names, plot_dicts = [], [];
for repo_dict in repo_dicts:
    names.append(repo_dict["name"]);
    plot_dict = {"value": repo_dict["stargazers_count"], "label": str(repo_dict["description"]), "xlink": repo_dict["html_url"]};#Add in link;
    plot_dicts.append(plot_dict);

my_style = LS("#336699", base_style = LCS);

my_config = pygal.Config();#Use this to customize the appearance of the diagram;
my_config.x_label_rotation = 45;
my_config.show_legend = False;
my_config.title_font_size = 24;
my_config.label_font_size = 14;#vice-label --- other labels;
my_config.major_label_font_size = 18;#majir-label --- the numbers on the axis;
my_config.truncate_label = 15;#Truncate long labels into ones with at most 15 chars;
my_config.show_y_guides = False;#Disguise the paralell lines on the chart;
my_config.width = 1000;#The width of the chart;



chart = pygal.Bar(my_config, style = my_style); 
#chart = pygal.Bar(style = my_style, x_label_rotation = 45, show_legend = False); 
chart.title = "Most-Starred Python Projects on GitHub";
chart.x_labels = names;
chart.add("", plot_dicts);
chart.render_to_file("python_repos.svg");
