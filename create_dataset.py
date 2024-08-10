import os
import pandas as pd
import numpy as np

mapIdToVideoName_2022 = [
        ('MSPic_A3H-o', 'ceaxfla-2turno-2022'), ('pOcFt9vupV8', 'amgxacg-2turno-2023'), ('0EAw5LZQ7sE', 'camxcor-2turno-2022'), ('FRisKPSITJY', 'capxbot-2turno-2022'), ('x3Ejm712UMc', 'sanxfor-2turno-2022'), ('2OklvldSx38', 'saoxgoi-2turno-2022'), ('h7D2aA6ysWA', 'cuixcor-2turno-2022'), ('awIuYMHgibs', 'flaxava-2turno-2022'), ('IvJ0xO2mO7s', 'botxsan-2turno-2022'), ('Dij69oqRjN0', 'juvxfla-2turno-2022'), ('AzAXikPgq2o', 'acgxcap-2turno-2022'), ('6ps0T5JSPNE', 'palxamg-2turno-2022'), ('iInEHMvmC8Q', 'forxbra-2turno-2022'), ('KjuSVZYLNps', 'avaxcea-2turno-2022'), ('r2zCe5o2BY4', 'crcxcor-2turno-2022'), ('90_gjSRSC6A', 'fluxgoi-2turno-2022'), ('K8e7H62mMN8', 'saoxint-2turno-2022'), ('Y9DcfdXCElQ', 'camxbot-2turno-2022'), ('qcA7JDX5JdQ', 'cuixpal-2turno-2022'), ('PjI4thS_vTA', 'forxacg-2turno-2022'), ('kUkSxhgl3hY', 'corxfla-2turno-2022'), ('HdB2S-NR_MU', 'intxcap-2turno-2022'), ('ms8xRdUZgTU', 'corxcea-2turno-2022'), ('4ao9KTVqbJQ', 'braxamg-2turno-2022'), ('aTEBi6DKrQc', 'goixjuv-2turno-2022'), ('RFVt3Mhe0Dw', 'sanxava-2turno-2022'), ('sf3oAmd27B8', 'fluxsao-2turno-2022'), ('CCip_i7qOeU', 'flaxcor-2turno-2022'), ('azB3AcUaOFY', 'palxfor-2turno-2022'), ('uDqXgo7FLCA', 'avaxbra-2turno-2022'), ('97LUIFAQNUQ', 'juvxcor-2turno-2022'), ('jdjnRyZ5e3I', 'acgxsan-2turno-2022'), ('YjRLrLDsiZw', 'capxgoi-2turno-2022'), ('zZjRSUmSttI', 'amgxint-2turno-2023'), ('LfhlXBXEXI8', 'saoxcam-2turno-2022'), ('xdGBb3xmn3Y', 'botxcui-2turno-2022'), ('fY-qNT74i_I', 'ceaxflu-2turno-2023'), ('Ulr4P2b_dig', 'goixcor-2turno-2022'), ('1ii8D5XY5-U', 'cuixava-2turno-2022'), ('yFIHrJr1urc', 'camxjuv-2turno-2022'), ('wpCFDM2cP3c', 'saoxsan-2turno-2022'), ('o2W88T4cONc', 'intxcea-2turno-2022'), ('FY-I7FD_gvI', 'corxflu-2turno-2022'), ('ePrNk6hVl60', 'flaxsan-2turno-2022'), ('OzpLObmZx7c', 'capxpal-2turno-2022'), ('6gs5EP-bk7k', 'forxcam-2turno-2022'), ('COnQkK_1xI0', 'acgxcea-2turno-2022'), ('YtCePnmUX0c', 'corxint-2turno-2022'), ('fQkGK0tiLBs', 'juvxsao-2turno-2022'), ('64qsfn9vZQU', 'fluxbot-2turno-2022'), ('XobM5Vbw4cQ', 'palxava-2turno-2022'), ('l0JIzl94sKQ', 'amgxfla-2turno-2022'), ('gz4vImf_MoQ', 'sanxcor-2turno-2022'), ('ZdVcdAL0qtA', 'braxcap-2turno-2022'), ('UUiO1YiAc2k', 'saoxcrc-2turno-2022'), ('MRSUbchlxIA', 'braxsan-2turno-2022'), ('hWTYFVNcO4g', 'capxcrc-2turno-2022'), ('a82-AK_kzMo', 'avaxflu-2turno-2022'), ('bIU2_RJ6aKs', 'botxint-2turno-2022'), ('bnh_owfBWhc', 'juvxacg-2turno-2022'), ('LQvTmPQG93c', 'ceaxcui-2turno-2022'), ('XJ794NAAh9A', 'palxsao-2turno-2022'), ('L6KWS7wn_lA', 'amgxfor-2turno-2022'), ('OXe474Zd7RU', 'flaxcam-2turno-2022'), ('R3KXD1ni4ZI', 'sanxjuv-2turno-2022'), ('i0eR5zrukGo', 'acg-pal-2turno-2022'), ('51oD-ZK9mDg', 'fluxamg-2turno-2022'), ('P71Xfi5kA5g', 'camxcea-2turno-2022'), ('7f52jm54W5U', 'forxava-2turno-2022'), ('SGZQEyu6C3o', 'saoxbot-2turno-2022'), ('TvVaGfWpE2I', 'intxgoi-2turno-2022'), ('zQ5nGlFGFRc', 'avaxbot-2turno-2022'), ('ATn1RLbACU8', 'palxcrc-2turno-2022'), ('P4VCqtJBZ-w', 'sanxcam-2turno-2022'), ('dUr7ykV92L4', 'flaxint-2turno-2022'), ('uRZTWJtsSmA', 'capxfor-2turno-2022'), ('zFQKsTpY4a4', 'acgxflu-2turno-2022'), ('2tDZcs_wWlU', 'ceaxgoi-2turno-2022'), ('5LhzbPyhZ8c', 'braxcui-2turno-2022'), ('NoC_-wM_LJQ', 'juvxcor-2turno-2022'), ('R8Nd42RBaoQ', 'botxpal-2turno-2022'), ('H-EOwRaCIC0', 'corxcui-2turno-2022'), ('6mMoljMNoLg', 'capxjuv-2turno-2022'), ('npM1UQ7aVP4', 'goixfor-2turno-2022'), ('h5dSNaMGO08', 'avaxacg-2turno-2022'), ('E_6rKsMJ3xo', 'flaxbra-2turno-2022'), ('M9WdRzYdurA', 'ceaxamg-2turno-2022'), ('ZN8FtrEnfyM', 'camxflu-2turno-2022'), ('k8Th3G6QiJc', 'intxsan-2turno-2022'), ('Q1u7XzbqQ1g', 'cuixamg-2turno-2022'), ('IQsaRIGm8_k', 'goixbot-2turno-2022'), ('ryRPeeIB59k', 'intxbra-2turno-2022'), ('t54-C3agkR4', 'camxpal-2turno-2022'), ('GwRDfG2VMAc', 'corxcea-2turno-2022'), ('Ir9Rom4Z_9I', 'corxacg-2turno-2022'), ('dMLOQjZbWbo', 'fluxjuv-2turno-2022'), ('kmM8BVh3oFg', 'sanxcap-2turno-2022'), ('Xkkwqt1xXPo', 'saoxava-2turno-2022'), ('BljnTSYeKdA', 'acgxint-2turno-2022'), ('3YJgpOjqg8s', 'capxcui-2turno-2022'), ('cJ7m3vg9tpM', 'palxsan-2turno-2022'), ('dKPro0ejw18', 'juvxfor-2turno-2022'), ('FsKOubl-qhI', 'amgxcor-2turno-2022'), ('QQnxz8pSzHw', 'ceaxsao-2turno-2022'), ('gM7gQkQrWco', 'botxcrc-2turno-2022'), ('l4zalgSV9ec', 'avaxcam-2turno-2022'), ('OefMLbXXpes', 'goixfla-2turno-2022'), ('fbnaFzlSWI0', 'crcxacg-2turno-2022'), ('F7g1pv5_I3I', 'saoxcor-2turno-2022'), ('7qGGVdlUiHkl', 'grexvas-2turno-2022'), ('T86F4acM4p8', 'avaxcap-2turno-2022'), ('YaXSQWnP0yw', 'botxamg-2turno-2022'), ('ZR6_Al5Mr1A', 'palxjuv-2turno-2022'), ('bXLFmtUhOoA', 'ceaxsantos-2turno-2022'), ('ku3NFL9kjrI', 'intxcea-2turno-2022'), ('2coas3SXGWY', 'camxbra-2turno-2022'), ('84ecGme8Pqk', 'sanxgoi-2turno-2022'), ('TTWo4tJ0jZE', 'cuixsao-2turno-2022'), ('gvj3p7g6Zzk', 'acgxcam-2turno-2022'), ('4_CZsKOhbe0', 'corxint-2turno-2022'), ('HzAvAP1d6Ag', 'forxbot-2turno-2022'), ('jxxMKbELuN0', 'flaxcea-2turno-2022'), ('Xpp_xx8dUA4', 'amgxcor-2turno-2022'), ('0vSPbI4xfOE', 'braxpal-2turno-2022'), ('kkV2D9_i_HE', 'juvxavai-2turno-2022'), ('JygD-xd_Kyo', 'corxbra-2turno-2022'), ('0m5LfTQHTA8', 'intxjuv-2turno-2022'), ('ZAzOCSoyBbU', 'cuixsan-2turno-2022'), ('Hd7Ck6RfCRU', 'botxfla-2turno-2022'), ('p7Hs10bLY68', 'saoxfor-2turno-2022'), ('i8p_rAJ-rvA', 'amgxcam-2turono-2022'), ('yLeHLTrB2s', 'ceaxcap-2turno-2022'), ('svvVhAmCv7g', 'fluxpal-2turno-2022'), ('QZgh9R391lI', 'goixacg-2turno-2022'), ('OMans9_MZ2c', 'avaixint-2turno-2022'), ('Jud3ag2RnRs', 'sanxsao-2turno-2022'), ('5UqMpJamTHU', 'braxcea-2turno-2022'), ('MxgRGemQL4Y', 'capxamg-2turno-2022'), ('y1p9sqMxmtA', 'acgxcui-2turno-2022'), ('7z0kV-OWtlcl', 'palxfla-2turno-2022'), ('2IwqIldp338', 'juvxbot-2turno-2022'), ('o8Ky8sgyWmw', 'fluxcor-2turno-2022'), ('QYc4bSwOQ38', 'camxgoi-2turno-2022'), ('R_mkStueuMQ', 'amgxsan-2turno-2022'), ('0V09LXLzg7g', 'ceaxfor-2turno-2022'), ('mqZaNRhVplw', 'flaxcap-2turno-2022'), ('wNFz6akXBYw', 'saoxbra-2turno-2022'), ('ojujZqGL14E', 'crcxcam-2turno-2022'), ('t2HnSQmTCgY', 'botxacg-2turno-2022'), ('O0zEdroA-XI', 'cuixjuv-2turno-2022'), ('tPG9Wf6X_RE', 'goixava-2turno-2022'), ('jF3soAVwBtI', 'crcxsan-2turno-2022'), ('rlA-qFaMYNU', 'camxcap-2turno-2022'), ('u0lYbW0Gr1A', 'forxint-2turno-2022'), ('Mv9duojMMiM', 'fluxcui-2turno-2022'), ('cCXRh5gHxhY', 'saoxfla-2turno-2022'), ('Ee-G_I8aMTE', 'avaxcor-2turno-2022'), ('C1GJiRkQSyE', 'acgxbra-2turno-2022'), ('KvhH2Cj-ecw', 'juvxamg-2turno-2022'), ('fENVMErphCk', 'botxcea-2turno-2022'), ('YLzvgahYH8A', 'sanxflu-2turno-2022'), ('xyN_wiHEimU', 'braxjuv-2turno-2022'), ('xmUydTb7muU', 'amgxava-2turno-2022'), ('4z_4jJs7Xt0', 'cuixfor-2turno-2022'), ('EQZrNHIuF3w', 'intxcam-2turno-2022'), ('yQ6scJqcmoc', 'capxsao-2turno-2022'), ('RlilubciJDg', 'flaxacg-2turno-2022'), ('U7RmcgkBxAM', 'corxbot-2turno-2022'), ('KvRTjzFHhpA', 'ceaxpal-2turno-2022')]

video_ids_2022 = [video_id for video_id, _ in mapIdToVideoName_2022]


def build_dataframe(video_ids):
    dfs = []
    for video_id in video_ids:
        input_file = f"{video_id}_comments_for_nlp.csv"
        path = os.path.join('./data/', input_file)
        if not os.path.exists(path):
            print(f"Arquivo {input_file} não encontrado. Pulando para o próximo vídeo...")
            continue
        else:
            print(f"Lendo arquivo {input_file}")
        df = pd.read_csv(path)
        dfs.append(df)
    return pd.concat(dfs)


df = build_dataframe(video_ids_2022)
#print(df.shape)
#print(df.head(10))


# Salva o dataframe em um arquivo csv
df.to_csv("all_comments_dataset.csv", index=False)


######################### Núvem de palavras #########################

import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('portuguese'))

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = text.translate(str.maketrans('', '', string.punctuation))

    text = text.lower()

    tokens = word_tokenize(text)

    tokens = [word for word in tokens if word not in stop_words]

    return " ".join(tokens)

def remove_emojis(df):
    # Definir o padrão de emoji
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F" 
        "\U0001F300-\U0001F5FF" 
        "\U0001F680-\U0001F6FF" 
        "\U0001F1E0-\U0001F1FF" 
        "\U00002702-\U000027B0"  
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "\U0001f926-\U0001f937"
        "\U00010000-\U0010ffff"
        "\u2640-\u2642" 
        "\u2600-\u2B55"
        "\u200d"
        "\u23cf"
        "\u23e9"
        "\u231a"
        "\ufe0f"
        "\u3030"
        "]+",
        flags=re.UNICODE
    )
    
    # Remover emojis apenas de strings, ignorando valores nulos ou de outros tipos
    df['text'] = df['text'].apply(lambda x: emoji_pattern.sub(r'', str(x)) if isinstance(x, str) else x)
    return df


#df['cleaned_text'] = df['text'].apply(clean_text)
df['cleaned_text'] = df['text'].head(10).apply(clean_text)
print(df['cleaned_text'].head(10))

print(df.head(10))

df['cleaned_text'] = df['text'].tail(10).apply(clean_text)

#df['cleaned_text'] = df['cleaned_text'].apply(remove_emojis)
#df = remove_emojis(df)
df_cleaned = df.copy()
df_cleaned = remove_emojis(df_cleaned)
print(df_cleaned.tail(10))

print(df.tail(10))
