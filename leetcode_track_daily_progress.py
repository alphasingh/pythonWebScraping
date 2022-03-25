from http.client import HTTPSConnection as Connect
import json
import sqlite3

CODER_NAMES = ('alphasingh', 'sukhdeep_', 'jatinbindra171998')


# will consider title slug of each submission for uniqueness
def convert_to_hashable_iterable(submission_list):
    return set(submission["titleSlug"] for submission in submission_list)


# default behaviour: last 100 AC submissions by alphasingh
def get_user_ac_submissions(old_submissions, username="alphasingh", limit=100):
    SIGNATURE = "recentAcSubmissions($username: String!, $limit: Int!)"
    USER = "{recentAcSubmissionList(username: $username, limit: $limit)"
    REQUIRED = "{id title titleSlug timestamp}}"
    SUBMISSION_DATA_QUERY = "query " + SIGNATURE + USER + REQUIRED
    connection = Connect("leetcode.com")
    payload = json.dumps({
        "query": SUBMISSION_DATA_QUERY,
        "variables": {
            "username": username,
            "limit": limit
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }
    connection.request("POST", "/graphql", payload, headers)
    res = connection.getresponse()
    data = res.read()
    json_data = json.loads(data.decode("utf-8"))
    recent_ac_submissions = json_data['data']['recentAcSubmissionList']
    old = convert_to_hashable_iterable(old_submissions[username])
    recent = convert_to_hashable_iterable(recent_ac_submissions)
    ac_submissions_in_one_day = recent.difference(old)
    print('=' * 30 + '\t' + username + '\t' + '=' * 100)
    print(recent_ac_submissions)
    print('fetched {} recent AC submissions for username {}'.format(len(recent), username))
    print('{} new submissions compared with old'.format(len(ac_submissions_in_one_day)))
    print('new submissions', ac_submissions_in_one_day)
    return json_data


def compare_diff_for_coders():
    connection = sqlite3.connect('test.db')
    db_cursor = connection.cursor()
    # get old_submissions from DB
    old_submissions = {name: [] for name in CODER_NAMES}
    for row in db_cursor.execute('SELECT * FROM coders'):
        name, json_data = row[0], json.loads(row[1])
        old_submissions[name] = json_data['data']['recentAcSubmissionList']
    for name in CODER_NAMES:
        get_user_ac_submissions(old_submissions, name)
    connection.close()


def update_data_for_coders():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('''DELETE FROM coders''')
    old_submissions = {name: [] for name in CODER_NAMES}
    for name in CODER_NAMES:
        data_in_json = get_user_ac_submissions(old_submissions, name)
        c.execute('''insert into coders values(?, ?)''', (name, json.dumps(data_in_json),))
        conn.commit()
    conn.close()


print('Comparing data for coders')
compare_diff_for_coders()
if input('Do you want to update?Y/n\n').strip().lower()[0] == 'y':
    print('Updating data for coders')
    update_data_for_coders()
