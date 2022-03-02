from http.client import HTTPSConnection as Connect
import json

# keep updating old_submissions with recent_ac_submissions
old_submissions = [
    {'id': '651591927', 'title': 'Is Subsequence', 'titleSlug': 'is-subsequence', 'timestamp': '1646186643'},
    {'id': '650908728', 'title': 'Counting Bits', 'titleSlug': 'counting-bits', 'timestamp': '1646099407'},
    {'id': '650861739', 'title': 'Maximum Number of Occurrences of a Substring',
     'titleSlug': 'maximum-number-of-occurrences-of-a-substring', 'timestamp': '1646092400'},
    {'id': '650844059', 'title': 'Divide Array in Sets of K Consecutive Numbers',
     'titleSlug': 'divide-array-in-sets-of-k-consecutive-numbers', 'timestamp': '1646089325'},
    {'id': '650825661', 'title': 'Find Numbers with Even Number of Digits',
     'titleSlug': 'find-numbers-with-even-number-of-digits', 'timestamp': '1646086394'},
    {'id': '650711992', 'title': 'Maximize the Confusion of an Exam', 'titleSlug': 'maximize-the-confusion-of-an-exam',
     'timestamp': '1646071566'},
    {'id': '650697083', 'title': 'Number of Pairs of Strings With Concatenation Equal to Target',
     'titleSlug': 'number-of-pairs-of-strings-with-concatenation-equal-to-target', 'timestamp': '1646069998'},
    {'id': '650695646', 'title': 'Convert 1D Array Into 2D Array', 'titleSlug': 'convert-1d-array-into-2d-array',
     'timestamp': '1646069849'},
    {'id': '650248509', 'title': 'Summary Ranges', 'titleSlug': 'summary-ranges', 'timestamp': '1646011205'},
    {'id': '650223934', 'title': 'Maximum Width of Binary Tree', 'titleSlug': 'maximum-width-of-binary-tree',
     'timestamp': '1646007920'},
    {'id': '650111090', 'title': 'Jump Game III', 'titleSlug': 'jump-game-iii', 'timestamp': '1645992485'},
    {'id': '650105356', 'title': 'All Elements in Two Binary Search Trees',
     'titleSlug': 'all-elements-in-two-binary-search-trees', 'timestamp': '1645991787'},
    {'id': '650103675', 'title': 'Find N Unique Integers Sum up to Zero',
     'titleSlug': 'find-n-unique-integers-sum-up-to-zero', 'timestamp': '1645991587'},
    {'id': '649958187', 'title': 'Remove Colored Pieces if Both Neighbors are the Same Color',
     'titleSlug': 'remove-colored-pieces-if-both-neighbors-are-the-same-color', 'timestamp': '1645974641'},
    {'id': '649953654', 'title': 'Minimum Number of Moves to Seat Everyone',
     'titleSlug': 'minimum-number-of-moves-to-seat-everyone', 'timestamp': '1645974023'},
    {'id': '649718740', 'title': 'Minimum Speed to Arrive on Time', 'titleSlug': 'minimum-speed-to-arrive-on-time',
     'timestamp': '1645941511'},
    {'id': '649584395', 'title': 'Minimum Time to Complete Trips', 'titleSlug': 'minimum-time-to-complete-trips',
     'timestamp': '1645930222'}, {'id': '649566020', 'title': 'Minimum Number of Steps to Make Two Strings Anagram II',
                                  'titleSlug': 'minimum-number-of-steps-to-make-two-strings-anagram-ii',
                                  'timestamp': '1645929385'},
    {'id': '649556672', 'title': 'Counting Words With a Given Prefix',
     'titleSlug': 'counting-words-with-a-given-prefix', 'timestamp': '1645929093'},
    {'id': '649542974', 'title': 'Element Appearing More Than 25% In Sorted Array',
     'titleSlug': 'element-appearing-more-than-25-in-sorted-array', 'timestamp': '1645927183'}]


# will consider title slug of each submission for uniqueness
def convert_to_hashable_iterable(submission_list):
    return set(submission["titleSlug"] for submission in submission_list)


# default behaviour: last 100 AC submissions by alphasingh
def get_user_ac_submissions(username="alphasingh", limit=100):
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
    old = convert_to_hashable_iterable(old_submissions)
    recent = convert_to_hashable_iterable(recent_ac_submissions)
    ac_submissions_in_one_day = recent.difference(old)
    print(recent_ac_submissions)
    print('fetched {} recent AC submissions for username {}'.format(len(recent), username))
    print('{} new submissions compared with old'.format(len(ac_submissions_in_one_day)))


get_user_ac_submissions()
