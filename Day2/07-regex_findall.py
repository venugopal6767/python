# import re

# str = "the ball is blue"
# pattern = r"ball"

# match = re.match(pattern, str)
# if match:
#     print("matchfound:" , match.group())
# else:
#     print("no match found")

import re

text = "The quick brown fox"
pattern = r"The"

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")