import pandas as pd
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('portuguese'))
times = ['flamengo', 'vasco', 'palmeiras', 'corinthians', 'corinthian', 'mengo', 'cruzeiro', 'grêmio', 'galo', 'fortaleza', 'fluminense', 'inter', 'bragantino', 'paulo', 'sao', 'bahia' ]

def clean_text(text: str) -> None:
    
    text = re.sub(r'http\S+', '', text)

    text = re.sub(r'\b\w*(\w)\1{2,}\w*\b', '', text)

    text = re.sub(r'\b\w{1,3}\b', '', text)

    if any(word in text for word in times):
        text = re.sub(r'\b(?:{})\b'.format('|'.join(times)), '', text)

    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

df = pd.read_csv('./all_comments_2022.csv')
df['text'] = df['text'].apply(clean_text)
df.to_csv('./all_comments_2022_cleaned.csv', index=False)
