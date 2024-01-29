import requests
import json
import time

# 1. Read config
config = dict()
with open("config.txt", "r") as f:
	for line in f:
		key, value = map(str.strip, line.split('=>'))
		config[key] = value

username = config['username']
password = config['password']
output_path = config['output_path']

api_url = f"https://api.github.com/users/{username}/starred"
headers = {"Accept": "application/vnd.github.v3+json"}

# 2. Fetch all pages of starred repositories
page = 1
starred_repos = []
while True:
	r = requests.get(api_url, auth=(username, password), headers=headers, params={"per_page": 100, "page": page})
	if r.status_code == 200:
		data = r.json()
		if not data:
			break
		
		dataLite = []
		for item in data:
			itemLite = {
				"id": item["id"],
				"full_name": item["full_name"],
				"owner": {
					"html_url": item["owner"]["html_url"],
				},
				"html_url": item["html_url"],
				"description": item["description"],
			}
			dataLite.append(itemLite)
		starred_repos.extend(dataLite)
		
		print(f"page: {page} data({len(dataLite)} items) received")
		time.sleep(0.2)
		page += 1
	else:
		print("API request failed with error code:", r.status_code)
		break

# 3. Save the data to a JSON file
with open(output_path, "w") as f:
	json.dump(starred_repos, f, indent=2)

print(f"The list({page - 1} pages, {len(starred_repos)} items) of all starred repositories has been saved as './{output_path}' file.")