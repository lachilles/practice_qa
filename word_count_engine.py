# #my partner's solution O(n)
#
#
# import re
# def word_count_engine(document):
#   map1 = {}
#   map2 = {}
#   tempArr = []
#   wordList = []
#   document = document.lower()
#   document = re.sub('[^a-zA-Z0-9 \n\.]', '', document)
#   wordList = re.sub("[^\w]", " ",  document).split()
#
#   for i in wordList:
#     if i in map1:
#       map1[i] += 1
#     else:
#       map1[i] = 1
#
#   tempstore = set()
#
#   for i in wordList:
#     if i in tempstore:
#       continue
#     else:
#       tempstore.add(i)
#       if map1[i] in map2:
#         map2[map1[i]].append(i)
#       else:
#         map2[map1[i]] = [i]
#
#   maxi = max(map2)
#   ans = []
#   for i in range(maxi,0,-1):
#     if i in map2:
#       for j in map2[i]:
#         ans.append([j,str(i)])
#
#   return ans
#
# x = word_count_engine('Practice makes perfect. you\'ll only get Perfect by practice. just practice!')
#
# print(x)
#
# # my solution
#
# from collections import OrderedDict
#
# def word_count_engine(document):
# """
# input:  document = "Practice makes perfect. you'll only
#                     get Perfect by practice. just practice!"
#
# output: [ ["practice", "3"], ["perfect", "2"],
#           ["makes", "1"], ["youll", "1"], ["only", "1"],
#           ["get", "1"], ["by", "1"], ["just", "1"] ]
# # case insensitive   “Perfect” == “perfect”
# # strip punctuation eg. '.-'
#
#      document = makes perfect by practice practice perfect practice just
#      seen =
#
#
#
#            "1",["by","makes","just"]
#            "2" , ["perfect"]
#            "3", ["partice"]
#
#      key      value
#      word -> number of occurences
#
#      number of occurences -> words
#
#
#
#
# """
#
# ## fast datastore to keep track of occurances
# ## split words, lower case theme (or upport), remove punctuation
# ## loop through this list once to compute resulting list of lists
#
#   # store words and their corresponding occurrences
#   seen = {
#      # 1: ["by","makes","just"],
#      # 2: ["perfect"],
#      # 3: ["pratice"]
#   }
#
#   # tokenize document into words by using whitespaces as delimiters
#   words = document.lower().split(' ')
#
#   result = []
#
#   for word in words:
#     # clean special characters from word
#     word.strip(',.-!?\'')
#     if word not in seen:
#       seen[word] = 1
#       # seen = { ["practice", "1"]}
#     else:
#       seen[word] += 1
#
#   seen_reversed = {}
#   for word in document:
#     v = seen[word]
#     if v not in seen_reversed:
#       seen_reversed[v] = list(word)
#     else:
#       seen_reversed[v].append(word)
#
#   maxi = max(seen_reversed)
#   for i in range(maxi,0,-1):
#     seen_reversed[i]
#
#
#
#
#
#   ["by", "1"]
#    ["perfect", "2"]
#    ["makes", "1"]
#    ["practice", "3"]
#    ["just", "1"]
#
#   #document = makes perfect by practice practice perfect practice just
#   "1",["makes","by","just"]
#   "3", ["partice"]
#  "2" , ["perfect"]