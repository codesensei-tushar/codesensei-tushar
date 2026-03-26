import requests, re, csv, os
from datetime import datetime

USERNAME = "codesensei-tushar"
CSV_FILE = "views_log.csv"

svg = requests.get(f"https://komarev.com/ghpvc/?username={USERNAME}&style=flat").text
count = int(re.search(r'(\d+)', svg).group(1))
today = str(datetime.today().date())

file_exists = os.path.exists(CSV_FILE)
with open(CSV_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["date", "total_views"])
    writer.writerow([today, count])

print(f"Logged {count} views for {today}")