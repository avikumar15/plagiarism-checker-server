from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import re
# Paste your Access token here
token = "access_token=" + "93b53c152f465923da3427d1e1d0c3ff20e747c9"

# Base API Endpoint
base_api_url = 'https://api.github.com/'

def fetchresults(code):
	# replace special characters by single space
	code = re.sub('[^a-zA-Z0-9\n ]', ' ', code)
	# get a list of words to search
	code = code.split()
	# to get a list of queries
	search_queries = list()
	current_query_length = 0
	current_query = ""
	# loop through the words in the code
	# and create segments of upto 128 characters
	for word in code:
		if len(word) + current_query_length < 128:
			current_query = current_query + '+' + word
			current_query_length = len(current_query)
		else:
			search_queries.append(current_query)
			current_query = word
			current_query_length = len(current_query)
	search_queries.append(current_query)
	# a dictionary to store the results of the plagiarism check
	results = dict()
	results['total_results'] = 0
	results['items'] = dict()
	# result_items is a dictionary indexed by the repo id
	# containing the details of the repo where a match was found,
	# the number of queries that got matched in the repo, and
	# the text match metadata
	result_items = results['items']

	for query in search_queries:
		search_str = base_api_url + 'search/code?q=' + query + '&' + token
		response = requests.get(search_str, 
				headers={'Accept': 'application/vnd.github.v3.text-match+json'},).json()

		if response:
			if response['total_count'] != 0:
				for item in response['items']:
					repo_id = item['repository']['id']
					# if the repo was previously matched, update the number of matches
					# and the match metadata
					if repo_id in result_items:
						result_items[repo_id]['total_matched'] = result_items[repo_id]['total_matched'] + 1
						result_items[repo_id]['matches'].append(item['text_matches'])
					# else create a new entry for this repo
					else:
						results['total_results'] = results['total_results'] + 1
						result_items[repo_id] = dict()
						result_items[repo_id]['total_matched'] = 1
						result_items[repo_id]['name'] = item['name']
						result_items[repo_id]['url'] = item['html_url']
						result_items[repo_id]['owner'] = item['repository']['owner']['login']
						result_items[repo_id]['matches'] = item['text_matches']
	return results

@csrf_exempt
def api(request):
	if request.method == "POST":
		code = request.body.decode('utf-8')
		return JsonResponse(fetchresults(code))