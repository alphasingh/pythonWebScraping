from datetime import datetime, timedelta
from http.client import HTTPSConnection as Connect
import json


# default behaviour: last 10 days by alphasingh
def get_user_submission_count(username="alphasingh", days=10):
    FILTERS = "{userCalendar(year: $year) {submissionCalendar}}}"
    SIGNATURE = "userProfileCalendar($username: String!, $year: Int)"
    USER = "{matchedUser(username: $username)"
    CALENDAR_DATA_QUERY = "query " + SIGNATURE + USER + FILTERS
    connection = Connect("leetcode.com")
    payload = json.dumps({
        "query": CALENDAR_DATA_QUERY,
        "variables": {
            "username": username
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    connection.request("POST", "/graphql", payload, headers)
    res = connection.getresponse()
    data = res.read()
    json_data = json.loads(data.decode("utf-8"))
    submission_calendar_string = json_data['data']['matchedUser']['userCalendar']['submissionCalendar']
    submissions = json.loads(submission_calendar_string)
    yesterday = datetime.today() - timedelta(days=days)
    yesterday_timestamp = int(yesterday.timestamp())
    print('fetching last {} days submission counts for username: {}'.format(days, username))
    for timestamp, count in submissions.items():
        timestamp = int(timestamp)
        if timestamp >= yesterday_timestamp:
            date = datetime.fromtimestamp(timestamp)
            print('{} problems solved on {}'.format(count, date))


get_user_submission_count()
