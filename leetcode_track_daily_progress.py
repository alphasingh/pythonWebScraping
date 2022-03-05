from http.client import HTTPSConnection as Connect
import json

# keep updating old_submissions with recent_ac_submissions
old_submissions = {
    "alphasingh": [{'id': '653519104', 'title': 'Maximum Matrix Sum', 'titleSlug': 'maximum-matrix-sum',
                    'timestamp': '1646445993'},
                   {'id': '653513892', 'title': 'Minimum Time to Type Word Using Special Typewriter',
                    'titleSlug': 'minimum-time-to-type-word-using-special-typewriter', 'timestamp': '1646444987'},
                   {'id': '653508875', 'title': 'Delete and Earn', 'titleSlug': 'delete-and-earn',
                    'timestamp': '1646443986'},
                   {'id': '653313686', 'title': 'Find the Smallest Divisor Given a Threshold',
                    'titleSlug': 'find-the-smallest-divisor-given-a-threshold', 'timestamp': '1646413594'},
                   {'id': '653310881', 'title': 'Group the People Given the Group Size They Belong To',
                    'titleSlug': 'group-the-people-given-the-group-size-they-belong-to', 'timestamp': '1646413261'},
                   {'id': '653306074', 'title': 'Subtract the Product and Sum of Digits of an Integer',
                    'titleSlug': 'subtract-the-product-and-sum-of-digits-of-an-integer', 'timestamp': '1646412690'},
                   {'id': '653018893', 'title': 'Champagne Tower', 'titleSlug': 'champagne-tower',
                    'timestamp': '1646370374'},
                   {'id': '652566945', 'title': 'Operations on Tree', 'titleSlug': 'operations-on-tree',
                    'timestamp': '1646310421'}, {'id': '652547432', 'title': 'Find All Groups of Farmland',
                                                 'titleSlug': 'find-all-groups-of-farmland', 'timestamp': '1646306934'},
                   {'id': '652541054', 'title': 'Find the Middle Index in Array',
                    'titleSlug': 'find-the-middle-index-in-array', 'timestamp': '1646305808'},
                   {'id': '652287690', 'title': 'Arithmetic Slices', 'titleSlug': 'arithmetic-slices',
                    'timestamp': '1646275044'}, {'id': '652079841',
                                                 'title': 'Maximum Side Length of a Square with Sum Less than or Equal to Threshold',
                                                 'titleSlug': 'maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold',
                                                 'timestamp': '1646245451'},
                   {'id': '652045418', 'title': 'The Time When the Network Becomes Idle',
                    'titleSlug': 'the-time-when-the-network-becomes-idle', 'timestamp': '1646241971'},
                   {'id': '652033612', 'title': 'Sequential Digits', 'titleSlug': 'sequential-digits',
                    'timestamp': '1646240765'},
                   {'id': '652028988', 'title': 'Convert Binary Number in a Linked List to Integer',
                    'titleSlug': 'convert-binary-number-in-a-linked-list-to-integer', 'timestamp': '1646240304'},
                   {'id': '652025197', 'title': 'Maximum Earnings From Taxi', 'titleSlug': 'maximum-earnings-from-taxi',
                    'timestamp': '1646239926'}, {'id': '651862934', 'title': 'Find Original Array From Doubled Array',
                                                 'titleSlug': 'find-original-array-from-doubled-array',
                                                 'timestamp': '1646218213'},
                   {'id': '651860644', 'title': 'Count Number of Pairs With Absolute Difference K',
                    'titleSlug': 'count-number-of-pairs-with-absolute-difference-k', 'timestamp': '1646217808'},
                   {'id': '651591927', 'title': 'Is Subsequence', 'titleSlug': 'is-subsequence',
                    'timestamp': '1646186643'},
                   {'id': '650908728', 'title': 'Counting Bits', 'titleSlug': 'counting-bits',
                    'timestamp': '1646099407'}],
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
    "sam_si": [{'id': '653700700', 'title': 'As Far from Land as Possible', 'titleSlug': 'as-far-from-land-as-possible',
                'timestamp': '1646472848'},
               {'id': '653688575', 'title': 'Pacific Atlantic Water Flow', 'titleSlug': 'pacific-atlantic-water-flow',
                'timestamp': '1646470828'},
               {'id': '653685855', 'title': 'Count Sub Islands', 'titleSlug': 'count-sub-islands',
                'timestamp': '1646470384'},
               {'id': '653648269', 'title': 'Delete and Earn', 'titleSlug': 'delete-and-earn',
                'timestamp': '1646464785'}, {'id': '653369002', 'title': 'Largest Time for Given Digits',
                                             'titleSlug': 'largest-time-for-given-digits', 'timestamp': '1646420085'},
               {'id': '653362119', 'title': 'Peeking Iterator', 'titleSlug': 'peeking-iterator',
                'timestamp': '1646419197'},
               {'id': '653352827', 'title': 'Number of Boomerangs', 'titleSlug': 'number-of-boomerangs',
                'timestamp': '1646418134'}, {'id': '653331034', 'title': 'Maximum Level Sum of a Binary Tree',
                                             'titleSlug': 'maximum-level-sum-of-a-binary-tree',
                                             'timestamp': '1646415650'},
               {'id': '653207936', 'title': 'Number of Enclaves', 'titleSlug': 'number-of-enclaves',
                'timestamp': '1646398396'},
               {'id': '653190566', 'title': 'Number of Closed Islands', 'titleSlug': 'number-of-closed-islands',
                'timestamp': '1646395023'},
               {'id': '653188420', 'title': 'Max Area of Island', 'titleSlug': 'max-area-of-island',
                'timestamp': '1646394596'},
               {'id': '653169429', 'title': 'Number of Islands', 'titleSlug': 'number-of-islands',
                'timestamp': '1646390776'},
               {'id': '653169069', 'title': 'Flood Fill', 'titleSlug': 'flood-fill', 'timestamp': '1646390709'},
               {'id': '653113462', 'title': 'Champagne Tower', 'titleSlug': 'champagne-tower',
                'timestamp': '1646381259'},
               {'id': '653099391', 'title': 'Two Sum', 'titleSlug': 'two-sum', 'timestamp': '1646379369'},
               {'id': '652780673', 'title': 'Longest Consecutive Sequence', 'titleSlug': 'longest-consecutive-sequence',
                'timestamp': '1646336046'},
               {'id': '652777324', 'title': 'Next Permutation', 'titleSlug': 'next-permutation',
                'timestamp': '1646335624'},
               {'id': '652770185', 'title': 'Longest Substring Without Repeating Characters',
                'titleSlug': 'longest-substring-without-repeating-characters', 'timestamp': '1646334755'},
               {'id': '652642505', 'title': 'Predict the Winner', 'titleSlug': 'predict-the-winner',
                'timestamp': '1646320878'},
               {'id': '652448348', 'title': 'Arithmetic Slices', 'titleSlug': 'arithmetic-slices',
                'timestamp': '1646291806'}],
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
