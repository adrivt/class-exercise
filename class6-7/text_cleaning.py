import pandas as pd
data = {"ID":range(4),"Message":["Now Here  "," now here ", "  NOW HERE", "Now   here"]}
df = pd.DataFrame(data)
#print(df)

# Strip Whitespace
df["Message"] = df["Message"].str.strip()
#print(df)
# Convert to Lowercase
df["Message"] = df["Message"].str.lower() 
#print(df)

# removing repeated whitespace between words?
#print(df["Message"].str.replace(' ',''))

#Difference between "" vs r""
print("a\nb") #a    b
print(r"a\tb") # a\tb

#One or more consecutive whitespace characters
pattern = r"\s+"

#One or more consecutive non-whitespace characters
pattern = r"\S+"

import re
re.sub(r"\s+", " ", "Hi     there") 
re.findall(r"\S+", "Hi there") 

import re

def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

