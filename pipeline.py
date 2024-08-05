'''
    Pipeline para obtenção de comentários de um vídeo do YouTube e processamento dos
    mesmos para análise de sentimentos. O pipeline a ser seguid é o seguinte:

                            [Coleta de Dados]
                                     |
                                     v
                            [Processamento Inicial]
                                     |
                                     v
                                [Anonimização]
                                     |
                                     v
                            [Preparação para NLP]
                                     |
                                     v
                        [Análise de Sentimentos (Futuro)]
                                     |
                                     v
                        [Visualização dos Dados (Futuro)]
'''

import json
import pandas as pd
import time
import random
import subprocess

# ---------------------------------------------------------------------------------------
mapIdToVideoName = [('NAqZEW9goNc', 'cruxcap-1turno-2024')]

# ---------------------------------------------------------------------------------------

def download_comments(video_id, output_file):
    subprocess.run([
        'youtube-comment-downloader',
        '--youtubeid', video_id,
        '--output', output_file
    ])

    print(f"Comentários do vídeo {video_id} salvos em {output_file}")


def load_and_process_comments(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        comments = [json.load(line) for line in f]
    df = pd.DataFrame(comments)
    return df


def anonymize_data(df):
    df_anonymized = df.drop(columns=['author', 'channel', 'photo'])
    return df_anonymized

def prepare_for_nlp(df):
    df_nlp = df[['text', 'time', 'votes', 'replies']]
    return df_nlp

def save_date(df, output_file):
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Dados salvos em {output_file}")

def pipeline(video_ids):
    for video_id in video_ids:
        output_file = f"{video_id}_comments.json"

        download_comments(video_id, output_file)

        wait_time = random.randint(1, 60)
        print(f"Aguardando {wait_time:.2f} segundos...")
        time.sleep(wait_time)

        df = load_and_process_comments(output_file)
        df_anonymized = anonymize_data(df)
        df_nlp= prepare_for_nlp(df_anonymized)

        save_date(df_nlp, f"{video_id}_comments_for_nlp.csv")


video_ids = [
        'NAqZEW9goNc',
]

# Inicia o pipeline
pipeline(video_ids)
