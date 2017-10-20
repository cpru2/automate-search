import os
from googleapiclient.discovery import build

my_api_key = os.environ.get('API_KEY', None)
my_cse_id = os.environ.get('CSE_ID', None)


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']


results = google_search(
    'satellite launch', my_api_key, my_cse_id, num=10)
fw = open('results.json', 'w')
fw.write(str(results))
fw.close()
