import pandas as pd
data = {"ID":range(100),"Score":[10]*2+[20]*3+[30]*5+[50]*15+[60]*20+[70]*25+[80]*15 +[90]*8 +[100,100,5,5,0,0,5000]}

df = pd.DataFrame(data)
print(df)


print(df.shape)
print(df.dtypes)
print(df.describe())

df_original = df.copy()

import matplotlib.pyplot as plt
#df['Score'].plot.hist(bins=300, edgecolor='black')
#plt.show()

#Without the last score of 5000. 
#df['Score'][:-1].plot.hist(bins=300, edgecolor='black')
#plt.show()

q1 = df["Score"].quantile(0.25)
q3 = df["Score"].quantile(0.75)
iqr = q3 - q1

# Use the equation above to replace None
lower = q1 - 1.5*iqr
upper = q3 + 1.5*iqr

print(lower)
print(upper)

df_score_cleaned = df[(df["Score"] >= lower) & (df["Score"] <= upper)]
df_score_cleaned['Score'].plot.hist(bins=300, edgecolor='black')
#plt.show()

mean = df["Score"].mean()
std = df["Score"].std()

# Use the equation above to replace None
z_scores = (df["Score"]-mean)/std

df_score_cleaned = df[z_scores.abs() <= 3]
df_score_cleaned['Score'].plot.hist(bins=300, edgecolor='black')
plt.show()