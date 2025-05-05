import pandas as pd

data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
mean_age = (df['Age'].mean())

"f tells python - This is a special string. Evaluate the expressions inside {} and insert their values."
print(f"The mean age is: {mean_age}")