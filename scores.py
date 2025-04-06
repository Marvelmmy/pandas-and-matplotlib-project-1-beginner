#importing the package 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

#inserting the data
score = pd.read_csv('data.csv')

#clean the data and sorting
score = score.fillna(0)
new_score = score.sort_values(["Names"],ascending=True) 
#note: in the code above, i sorted the values because previously i used my friends' name 
#but i changed it in the data.csv to anonymous names due to privacy

# Ensure Plus Point is numeric
new_score['Plus Point'] = pd.to_numeric(new_score['Plus Point'], errors='coerce').fillna(0)

# Calculate means
mean_plus_point = round(new_score['Plus Point'].mean(), 2)
mean_Video = round(new_score['Video'].mean(), 2)
mean_formatif = round(new_score['Formatif'].mean(), 2)
mean_summative = round(new_score['Summative'].mean(), 2)

# Calculate totals
total_plus_point = new_score['Plus Point'].sum()
total_Video = new_score['Video'].sum()
total_formatif = new_score['Formatif'].sum()
total_summative = new_score['Summative'].sum()

# Create Mean and Total rows
new_score2 = pd.DataFrame([{
    'Names': 'Mean',
    'Plus Point': mean_plus_point,
    'Video': mean_Video,
    'Formatif': mean_formatif,
    'Summative': mean_summative
}, {
    'Names': 'Total',
    'Plus Point': total_plus_point,
    'Video': total_Video,
    'Formatif': total_formatif,
    'Summative': total_summative
}])

# Combine all
new_score = pd.concat([new_score, new_score2], ignore_index=True)
new_score.index = range(1, len(new_score) + 1)

#setting the coordinates for the graph
x = np.arange(1,22)
y1 = new_score.iloc[1:22,3]
y2 = new_score.iloc[1:22,4]
plt.figure(figsize=(20,10))

#making the bar width to seperate the formative and summative scores
bar_width = 0.4

#plotting the graph 
plt.bar(x - bar_width/2 , y1, width=bar_width, color=(173/255, 216/255, 230/255), label='Formative')
plt.bar(x + bar_width/2, y2, width=bar_width,color=(255/255, 182/255, 193/255), label='Summative')
plt.title("Formative vs Summative of each students", fontdict={'fontname' : 'Comic Sans MS', 'fontsize':20})
plt.xlabel("Absent numbers",fontdict={'fontname' : 'Comic Sans MS', 'fontsize':15})
plt.ylabel("Scores",fontdict={'fontname' : 'Comic Sans MS', 'fontsize':15})
plt.xticks(x, fontsize=15)
plt.legend()

#showing the graph
plt.show()


