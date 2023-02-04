# import seaborn as sns
# import pandas as pd
import matplotlib.pyplot as plt

# d = {'col1': [1,2,3,4,8,1], 'col2': [3,4,1,1,5,4]}
# df = pd.DataFrame(data=d)
ages = [21,33,45,99,16,8]
scores = [1,1,5,2,3,3.3]
fig, ax = plt.subplots()
ax.scatter(ages,scores)
ax.set_xlabel('Age')
ax.set_ylabel('Score')
ax.set_title('Ratings of Product X by Survey Participants')
plt.show()