import re
text = "HE is a good boy"
pattern = r"is"

replacement = "was"

new_text = re.sub(pattern, replacement, text)
print(new_text)