import os
import pandas as pd

for year in ['2022', '2023']:
    matches = pd.read_csv(f"brzao{year}.csv") 

    comments_data = []

    for index, row in matches.iterrows():
        video_id = row['id']
        input_file = f"{video_id}_comments_for_nlp.csv"
        path = os.path.join(f"./data/{year}/", input_file)
        if not os.path.exists(path):
            print(f"Arquivo {input_file} não encontrado. Pulando para o próximo vídeo...")
            continue
        else:
            print(f"Lendo arquivo {input_file}")
        df = pd.read_csv(path)
        comments_data.append([video_id, row['rodada'], df.shape[0], row['views']])

    df_comments = pd.DataFrame(comments_data, columns=['id', 'rodada', 'num_comments', 'views'])
    df_comments.to_csv(f"comments_per_video{year}.csv", index=False)