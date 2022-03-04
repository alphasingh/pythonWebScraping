from http.client import HTTPSConnection as Connect
import json

# keep updating old_submissions with recent_ac_submissions
old_submissions = {
    "alphasingh": [
        {'id': '653018893', 'title': 'Champagne Tower', 'titleSlug': 'champagne-tower', 'timestamp': '1646370374'},
        {'id': '652566945', 'title': 'Operations on Tree', 'titleSlug': 'operations-on-tree',
         'timestamp': '1646310421'},
        {'id': '652547432', 'title': 'Find All Groups of Farmland', 'titleSlug': 'find-all-groups-of-farmland',
         'timestamp': '1646306934'},
        {'id': '652541054', 'title': 'Find the Middle Index in Array', 'titleSlug': 'find-the-middle-index-in-array',
         'timestamp': '1646305808'},
        {'id': '652287690', 'title': 'Arithmetic Slices', 'titleSlug': 'arithmetic-slices', 'timestamp': '1646275044'},
        {'id': '652079841', 'title': 'Maximum Side Length of a Square with Sum Less than or Equal to Threshold',
         'titleSlug': 'maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold',
         'timestamp': '1646245451'}, {'id': '652045418', 'title': 'The Time When the Network Becomes Idle',
                                      'titleSlug': 'the-time-when-the-network-becomes-idle', 'timestamp': '1646241971'},
        {'id': '652033612', 'title': 'Sequential Digits', 'titleSlug': 'sequential-digits', 'timestamp': '1646240765'},
        {'id': '652028988', 'title': 'Convert Binary Number in a Linked List to Integer',
         'titleSlug': 'convert-binary-number-in-a-linked-list-to-integer', 'timestamp': '1646240304'},
        {'id': '652025197', 'title': 'Maximum Earnings From Taxi', 'titleSlug': 'maximum-earnings-from-taxi',
         'timestamp': '1646239926'}, {'id': '651862934', 'title': 'Find Original Array From Doubled Array',
                                      'titleSlug': 'find-original-array-from-doubled-array', 'timestamp': '1646218213'},
        {'id': '651860644', 'title': 'Count Number of Pairs With Absolute Difference K',
         'titleSlug': 'count-number-of-pairs-with-absolute-difference-k', 'timestamp': '1646217808'},
        {'id': '651591927', 'title': 'Is Subsequence', 'titleSlug': 'is-subsequence', 'timestamp': '1646186643'},
        {'id': '650908728', 'title': 'Counting Bits', 'titleSlug': 'counting-bits', 'timestamp': '1646099407'},
        {'id': '650861739', 'title': 'Maximum Number of Occurrences of a Substring',
         'titleSlug': 'maximum-number-of-occurrences-of-a-substring', 'timestamp': '1646092400'},
        {'id': '650844059', 'title': 'Divide Array in Sets of K Consecutive Numbers',
         'titleSlug': 'divide-array-in-sets-of-k-consecutive-numbers', 'timestamp': '1646089325'},
        {'id': '650825661', 'title': 'Find Numbers with Even Number of Digits',
         'titleSlug': 'find-numbers-with-even-number-of-digits', 'timestamp': '1646086394'},
        {'id': '650711992', 'title': 'Maximize the Confusion of an Exam',
         'titleSlug': 'maximize-the-confusion-of-an-exam', 'timestamp': '1646071566'},
        {'id': '650697083', 'title': 'Number of Pairs of Strings With Concatenation Equal to Target',
         'titleSlug': 'number-of-pairs-of-strings-with-concatenation-equal-to-target', 'timestamp': '1646069998'},
        {'id': '650695646', 'title': 'Convert 1D Array Into 2D Array', 'titleSlug': 'convert-1d-array-into-2d-array',
         'timestamp': '1646069849'}],
    "jatinbindra171998": [{'id': '652611731', 'title': 'Maximum Difference Between Increasing Elements',
                           'titleSlug': 'maximum-difference-between-increasing-elements', 'timestamp': '1646317112'},
                          {'id': '651979588', 'title': 'Find Missing Observations',
                           'titleSlug': 'find-missing-observations', 'timestamp': '1646234940'},
                          {'id': '651965845', 'title': 'Minimum Moves to Convert String',
                           'titleSlug': 'minimum-moves-to-convert-string', 'timestamp': '1646233277'},
                          {'id': '651959646', 'title': 'Minimum Operations to Make a Uni-Value Grid',
                           'titleSlug': 'minimum-operations-to-make-a-uni-value-grid', 'timestamp': '1646232542'},
                          {'id': '651942867', 'title': 'Two Out of Three', 'titleSlug': 'two-out-of-three',
                           'timestamp': '1646230532'},
                          {'id': '651287293', 'title': 'Remove Colored Pieces if Both Neighbors are the Same Color',
                           'titleSlug': 'remove-colored-pieces-if-both-neighbors-are-the-same-color',
                           'timestamp': '1646146274'},
                          {'id': '651278154', 'title': 'Minimum Number of Moves to Seat Everyone',
                           'titleSlug': 'minimum-number-of-moves-to-seat-everyone', 'timestamp': '1646145063'},
                          {'id': '651274018', 'title': 'Simple Bank System', 'titleSlug': 'simple-bank-system',
                           'timestamp': '1646144549'},
                          {'id': '651268810', 'title': 'Check if Numbers Are Ascending in a Sentence',
                           'titleSlug': 'check-if-numbers-are-ascending-in-a-sentence', 'timestamp': '1646143873'},
                          {'id': '650610538', 'title': 'Next Greater Numerically Balanced Number',
                           'titleSlug': 'next-greater-numerically-balanced-number', 'timestamp': '1646060002'},
                          {'id': '650256514', 'title': 'Minimum Time to Complete Trips',
                           'titleSlug': 'minimum-time-to-complete-trips', 'timestamp': '1646012243'},
                          {'id': '650232763', 'title': 'Minimum Number of Steps to Make Two Strings Anagram II',
                           'titleSlug': 'minimum-number-of-steps-to-make-two-strings-anagram-ii',
                           'timestamp': '1646009105'},
                          {'id': '650231258', 'title': 'Counting Words With a Given Prefix',
                           'titleSlug': 'counting-words-with-a-given-prefix', 'timestamp': '1646008907'},
                          {'id': '647691231', 'title': 'Kth Distinct String in an Array',
                           'titleSlug': 'kth-distinct-string-in-an-array', 'timestamp': '1645652737'},
                          {'id': '647533322', 'title': 'Maximum Split of Positive Even Integers',
                           'titleSlug': 'maximum-split-of-positive-even-integers', 'timestamp': '1645634321'},
                          {'id': '647518217', 'title': 'Solving Questions With Brainpower',
                           'titleSlug': 'solving-questions-with-brainpower', 'timestamp': '1645632615'},
                          {'id': '647464904', 'title': 'Maximum Split of Positive Even Integers',
                           'titleSlug': 'maximum-split-of-positive-even-integers', 'timestamp': '1645626002'},
                          {'id': '646976113', 'title': 'Minimum Operations to Convert Number',
                           'titleSlug': 'minimum-operations-to-convert-number', 'timestamp': '1645561701'},
                          {'id': '646951791',
                           'title': 'Find the Minimum and Maximum Number of Nodes Between Critical Points',
                           'titleSlug': 'find-the-minimum-and-maximum-number-of-nodes-between-critical-points',
                           'timestamp': '1645558774'}, {'id': '646943750', 'title': 'Smallest Index With Equal Value',
                                                        'titleSlug': 'smallest-index-with-equal-value',
                                                        'timestamp': '1645557890'}],
    "sam_si": [{'id': '652780673', 'title': 'Longest Consecutive Sequence', 'titleSlug': 'longest-consecutive-sequence',
                'timestamp': '1646336046'},
               {'id': '652777324', 'title': 'Next Permutation', 'titleSlug': 'next-permutation',
                'timestamp': '1646335624'},
               {'id': '652770185', 'title': 'Longest Substring Without Repeating Characters',
                'titleSlug': 'longest-substring-without-repeating-characters', 'timestamp': '1646334755'},
               {'id': '652642505', 'title': 'Predict the Winner', 'titleSlug': 'predict-the-winner',
                'timestamp': '1646320878'},
               {'id': '652448348', 'title': 'Arithmetic Slices', 'titleSlug': 'arithmetic-slices',
                'timestamp': '1646291806'},
               {'id': '651729984', 'title': 'Is Subsequence', 'titleSlug': 'is-subsequence', 'timestamp': '1646200969'},
               {'id': '651429790', 'title': 'Longest Turbulent Subarray', 'titleSlug': 'longest-turbulent-subarray',
                'timestamp': '1646162664'},
               {'id': '651115831', 'title': 'Counting Bits', 'titleSlug': 'counting-bits', 'timestamp': '1646120982'},
               {'id': '650767919', 'title': 'Minimum Time to Complete Trips',
                'titleSlug': 'minimum-time-to-complete-trips', 'timestamp': '1646078098'},
               {'id': '650733653', 'title': 'Parallel Courses III', 'titleSlug': 'parallel-courses-iii',
                'timestamp': '1646073904'},
               {'id': '650655523', 'title': 'Summary Ranges', 'titleSlug': 'summary-ranges', 'timestamp': '1646065480'},
               {'id': '649880808', 'title': 'Maximum Width of Binary Tree', 'titleSlug': 'maximum-width-of-binary-tree',
                'timestamp': '1645962628'}, {'id': '649114473', 'title': 'Shortest Path Visiting All Nodes',
                                             'titleSlug': 'shortest-path-visiting-all-nodes',
                                             'timestamp': '1645863422'},
               {'id': '648844131', 'title': 'Binary String With Substrings Representing 1 To N',
                'titleSlug': 'binary-string-with-substrings-representing-1-to-n', 'timestamp': '1645818750'},
               {'id': '648788184', 'title': 'Convert Sorted Array to Binary Search Tree',
                'titleSlug': 'convert-sorted-array-to-binary-search-tree', 'timestamp': '1645811705'},
               {'id': '648701398', 'title': 'Increasing Subsequences', 'titleSlug': 'increasing-subsequences',
                'timestamp': '1645800504'},
               {'id': '648509014', 'title': 'Compare Version Numbers', 'titleSlug': 'compare-version-numbers',
                'timestamp': '1645769189'},
               {'id': '648031353', 'title': 'Repeated String Match', 'titleSlug': 'repeated-string-match',
                'timestamp': '1645699079'},
               {'id': '647923200', 'title': 'Sort List', 'titleSlug': 'sort-list', 'timestamp': '1645683153'},
               {'id': '647545302', 'title': 'Shortest Path Visiting All Nodes',
                'titleSlug': 'shortest-path-visiting-all-nodes', 'timestamp': '1645635586'}],
    "": []}


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
    old = convert_to_hashable_iterable(old_submissions[username])
    recent = convert_to_hashable_iterable(recent_ac_submissions)
    ac_submissions_in_one_day = recent.difference(old)
    print('=' * 30 + '\t' + username + '\t' + '=' * 100)
    print(recent_ac_submissions)
    print('fetched {} recent AC submissions for username {}'.format(len(recent), username))
    print('{} new submissions compared with old'.format(len(ac_submissions_in_one_day)))
    print('new submissions', ac_submissions_in_one_day)


for name in ("jatinbindra171998", "alphasingh", "sam_si"):
    get_user_ac_submissions(name)
