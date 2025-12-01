import pandas as pd

data = {
    'Math': [80, 90, 85],
    'Science': [75, 95, 88],
    'History': [70, 85, 78],
    'English': [82, 88, 91]
}

df = pd.DataFrame(data, index=["Alice", "Bob", "Charlie"])

average_scores = [df['Math'].mean(), df['Science'].mean(), df['History'].mean(), df['English'].mean()]
subjects = ['Math', 'Science', 'History', 'English']

print(f'''Average Scores per subject:
      
        Math: {average_scores[0]}
        Science: {average_scores[1]}
        History: {average_scores[2]}
        English: {average_scores[3]}''')

print(f'The subject with the highest score was {subjects[average_scores.index(max(average_scores))]} with an average of {max(average_scores)}')