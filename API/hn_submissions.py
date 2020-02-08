import requests;
from operator import itemgetter;

url = "https://hacker-news.firebaseio.com/v0/topstories.json";
r = requests.get(url);
print("Status Code:", r.status_code);

submission_ids = r.json();
submission_dicts = [];
for submission_id in submission_ids[:30]:
    url = ("https://hacker-news.firebaseio.com/v0/item/" + str(submission_id) + ".json");
    submission_r = requests(url);
    print("Status Code:", submission_r.status_code);
    response_dict = submission_r.json();

    submission_dict = {
        "title": response_dict["title"],
        "link": "http://news.ycombinator.com/item?id=" + str(submission_id),
        "comments": response_dict.get("descendants", 0),#Not exists returning 0;
    };
    submission_dicts.append(submission_dict);

submission_dicts = sorted(submission_dicts, key = itemgetter("comments"), reverse = True);#itemgetter extracts all the comments from the dicts;

for submission_dict in submission_dicts:
    print("\nTitle", submission_dict["title"]);
    print("Discussion Link", submission_dict["link"]);
    print("Comments", submission_dict["comments"]);
