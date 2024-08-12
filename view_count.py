import subprocess
import json
import pandas as pd
import random
import time
import os

if not os.path.exists("./views_2022.csv"):
    views = {}
else:
    df = pd.read_csv("views_2022.csv")
    views = dict(zip(df['id'], df['views']))

mapIdToVideoName_2022 = [
        ('MSPic_A3H-o', 'ceaxfla-2turno-2022'), ('pOcFt9vupV8', 'amgxacg-2turno-2023'), ('0EAw5LZQ7sE', 'camxcor-2turno-2022'), ('FRisKPSITJY', 'capxbot-2turno-2022'), ('x3Ejm712UMc', 'sanxfor-2turno-2022'), ('2OklvldSx38', 'saoxgoi-2turno-2022'), ('h7D2aA6ysWA', 'cuixcor-2turno-2022'), ('awIuYMHgibs', 'flaxava-2turno-2022'), ('IvJ0xO2mO7s', 'botxsan-2turno-2022'), ('Dij69oqRjN0', 'juvxfla-2turno-2022'), ('AzAXikPgq2o', 'acgxcap-2turno-2022'), ('6ps0T5JSPNE', 'palxamg-2turno-2022'), ('iInEHMvmC8Q', 'forxbra-2turno-2022'), ('KjuSVZYLNps', 'avaxcea-2turno-2022'), ('r2zCe5o2BY4', 'crcxcor-2turno-2022'), ('90_gjSRSC6A', 'fluxgoi-2turno-2022'), ('K8e7H62mMN8', 'saoxint-2turno-2022'), ('Y9DcfdXCElQ', 'camxbot-2turno-2022'), ('qcA7JDX5JdQ', 'cuixpal-2turno-2022'), ('PjI4thS_vTA', 'forxacg-2turno-2022'), ('kUkSxhgl3hY', 'corxfla-2turno-2022'), ('HdB2S-NR_MU', 'intxcap-2turno-2022'), ('ms8xRdUZgTU', 'corxcea-2turno-2022'), ('4ao9KTVqbJQ', 'braxamg-2turno-2022'), ('aTEBi6DKrQc', 'goixjuv-2turno-2022'), ('RFVt3Mhe0Dw', 'sanxava-2turno-2022'), ('sf3oAmd27B8', 'fluxsao-2turno-2022'), ('CCip_i7qOeU', 'flaxcor-2turno-2022'), ('azB3AcUaOFY', 'palxfor-2turno-2022'), ('uDqXgo7FLCA', 'avaxbra-2turno-2022'), ('97LUIFAQNUQ', 'juvxcor-2turno-2022'), ('jdjnRyZ5e3I', 'acgxsan-2turno-2022'), ('YjRLrLDsiZw', 'capxgoi-2turno-2022'), ('zZjRSUmSttI', 'amgxint-2turno-2023'), ('LfhlXBXEXI8', 'saoxcam-2turno-2022'), ('xdGBb3xmn3Y', 'botxcui-2turno-2022'), ('fY-qNT74i_I', 'ceaxflu-2turno-2023'), ('Ulr4P2b_dig', 'goixcor-2turno-2022'), ('1ii8D5XY5-U', 'cuixava-2turno-2022'), ('yFIHrJr1urc', 'camxjuv-2turno-2022'), ('wpCFDM2cP3c', 'saoxsan-2turno-2022'), ('o2W88T4cONc', 'intxcea-2turno-2022'), ('FY-I7FD_gvI', 'corxflu-2turno-2022'), ('ePrNk6hVl60', 'flaxsan-2turno-2022'), ('OzpLObmZx7c', 'capxpal-2turno-2022'), ('6gs5EP-bk7k', 'forxcam-2turno-2022'), ('COnQkK_1xI0', 'acgxcea-2turno-2022'), ('YtCePnmUX0c', 'corxint-2turno-2022'), ('fQkGK0tiLBs', 'juvxsao-2turno-2022'), ('64qsfn9vZQU', 'fluxbot-2turno-2022'), ('XobM5Vbw4cQ', 'palxava-2turno-2022'), ('l0JIzl94sKQ', 'amgxfla-2turno-2022'), ('gz4vImf_MoQ', 'sanxcor-2turno-2022'), ('ZdVcdAL0qtA', 'braxcap-2turno-2022'), ('UUiO1YiAc2k', 'saoxcrc-2turno-2022'), ('MRSUbchlxIA', 'braxsan-2turno-2022'), ('hWTYFVNcO4g', 'capxcrc-2turno-2022'), ('a82-AK_kzMo', 'avaxflu-2turno-2022'), ('bIU2_RJ6aKs', 'botxint-2turno-2022'), ('bnh_owfBWhc', 'juvxacg-2turno-2022'), ('LQvTmPQG93c', 'ceaxcui-2turno-2022'), ('XJ794NAAh9A', 'palxsao-2turno-2022'), ('L6KWS7wn_lA', 'amgxfor-2turno-2022'), ('OXe474Zd7RU', 'flaxcam-2turno-2022'), ('R3KXD1ni4ZI', 'sanxjuv-2turno-2022'), ('i0eR5zrukGo', 'acg-pal-2turno-2022'), ('51oD-ZK9mDg', 'fluxamg-2turno-2022'), ('P71Xfi5kA5g', 'camxcea-2turno-2022'), ('7f52jm54W5U', 'forxava-2turno-2022'), ('SGZQEyu6C3o', 'saoxbot-2turno-2022'), ('TvVaGfWpE2I', 'intxgoi-2turno-2022'), ('zQ5nGlFGFRc', 'avaxbot-2turno-2022'), ('ATn1RLbACU8', 'palxcrc-2turno-2022'), ('P4VCqtJBZ-w', 'sanxcam-2turno-2022'), ('dUr7ykV92L4', 'flaxint-2turno-2022'), ('uRZTWJtsSmA', 'capxfor-2turno-2022'), ('zFQKsTpY4a4', 'acgxflu-2turno-2022'), ('2tDZcs_wWlU', 'ceaxgoi-2turno-2022'), ('5LhzbPyhZ8c', 'braxcui-2turno-2022'), ('NoC_-wM_LJQ', 'juvxcor-2turno-2022'), ('R8Nd42RBaoQ', 'botxpal-2turno-2022'), ('H-EOwRaCIC0', 'corxcui-2turno-2022'), ('6mMoljMNoLg', 'capxjuv-2turno-2022'), ('npM1UQ7aVP4', 'goixfor-2turno-2022'), ('h5dSNaMGO08', 'avaxacg-2turno-2022'), ('E_6rKsMJ3xo', 'flaxbra-2turno-2022'), ('M9WdRzYdurA', 'ceaxamg-2turno-2022'), ('ZN8FtrEnfyM', 'camxflu-2turno-2022'), ('k8Th3G6QiJc', 'intxsan-2turno-2022'), ('Q1u7XzbqQ1g', 'cuixamg-2turno-2022'), ('IQsaRIGm8_k', 'goixbot-2turno-2022'), ('ryRPeeIB59k', 'intxbra-2turno-2022'), ('t54-C3agkR4', 'camxpal-2turno-2022'), ('GwRDfG2VMAc', 'corxcea-2turno-2022'), ('Ir9Rom4Z_9I', 'corxacg-2turno-2022'), ('dMLOQjZbWbo', 'fluxjuv-2turno-2022'), ('kmM8BVh3oFg', 'sanxcap-2turno-2022'), ('Xkkwqt1xXPo', 'saoxava-2turno-2022'), ('BljnTSYeKdA', 'acgxint-2turno-2022'), ('3YJgpOjqg8s', 'capxcui-2turno-2022'), ('cJ7m3vg9tpM', 'palxsan-2turno-2022'), ('dKPro0ejw18', 'juvxfor-2turno-2022'), ('FsKOubl-qhI', 'amgxcor-2turno-2022'), ('QQnxz8pSzHw', 'ceaxsao-2turno-2022'), ('gM7gQkQrWco', 'botxcrc-2turno-2022'), ('l4zalgSV9ec', 'avaxcam-2turno-2022'), ('OefMLbXXpes', 'goixfla-2turno-2022'), ('fbnaFzlSWI0', 'crcxacg-2turno-2022'), ('F7g1pv5_I3I', 'saoxcor-2turno-2022'), ('7qGGVdlUiHkl', 'grexvas-2turno-2022'), ('T86F4acM4p8', 'avaxcap-2turno-2022'), ('YaXSQWnP0yw', 'botxamg-2turno-2022'), ('ZR6_Al5Mr1A', 'palxjuv-2turno-2022'), ('bXLFmtUhOoA', 'ceaxsantos-2turno-2022'), ('ku3NFL9kjrI', 'intxcea-2turno-2022'), ('2coas3SXGWY', 'camxbra-2turno-2022'), ('84ecGme8Pqk', 'sanxgoi-2turno-2022'), ('TTWo4tJ0jZE', 'cuixsao-2turno-2022'), ('gvj3p7g6Zzk', 'acgxcam-2turno-2022'), ('4_CZsKOhbe0', 'corxint-2turno-2022'), ('HzAvAP1d6Ag', 'forxbot-2turno-2022'), ('jxxMKbELuN0', 'flaxcea-2turno-2022'), ('Xpp_xx8dUA4', 'amgxcor-2turno-2022'), ('0vSPbI4xfOE', 'braxpal-2turno-2022'), ('kkV2D9_i_HE', 'juvxavai-2turno-2022'), ('JygD-xd_Kyo', 'corxbra-2turno-2022'), ('0m5LfTQHTA8', 'intxjuv-2turno-2022'), ('ZAzOCSoyBbU', 'cuixsan-2turno-2022'), ('Hd7Ck6RfCRU', 'botxfla-2turno-2022'), ('p7Hs10bLY68', 'saoxfor-2turno-2022'), ('i8p_rAJ-rvA', 'amgxcam-2turono-2022'), ('-yLeHLTrB2s', 'ceaxcap-2turno-2022'), ('svvVhAmCv7g', 'fluxpal-2turno-2022'), ('QZgh9R391lI', 'goixacg-2turno-2022'), ('OMans9_MZ2c', 'avaixint-2turno-2022'), ('Jud3ag2RnRs', 'sanxsao-2turno-2022'), ('5UqMpJamTHU', 'braxcea-2turno-2022'), ('MxgRGemQL4Y', 'capxamg-2turno-2022'), ('y1p9sqMxmtA', 'acgxcui-2turno-2022'), ('7z0kV-OWtlcl', 'palxfla-2turno-2022'), ('2IwqIldp338', 'juvxbot-2turno-2022'), ('o8Ky8sgyWmw', 'fluxcor-2turno-2022'), ('QYc4bSwOQ38', 'camxgoi-2turno-2022'), ('R_mkStueuMQ', 'amgxsan-2turno-2022'), ('0V09LXLzg7g', 'ceaxfor-2turno-2022'), ('mqZaNRhVplw', 'flaxcap-2turno-2022'), ('wNFz6akXBYw', 'saoxbra-2turno-2022'), ('ojujZqGL14E', 'crcxcam-2turno-2022'), ('t2HnSQmTCgY', 'botxacg-2turno-2022'), ('O0zEdroA-XI', 'cuixjuv-2turno-2022'), ('tPG9Wf6X_RE', 'goixava-2turno-2022'), ('jF3soAVwBtI', 'crcxsan-2turno-2022'), ('rlA-qFaMYNU', 'camxcap-2turno-2022'), ('u0lYbW0Gr1A', 'forxint-2turno-2022'), ('Mv9duojMMiM', 'fluxcui-2turno-2022'), ('cCXRh5gHxhY', 'saoxfla-2turno-2022'), ('Ee-G_I8aMTE', 'avaxcor-2turno-2022'), ('C1GJiRkQSyE', 'acgxbra-2turno-2022'), ('KvhH2Cj-ecw', 'juvxamg-2turno-2022'), ('fENVMErphCk', 'botxcea-2turno-2022'), ('YLzvgahYH8A', 'sanxflu-2turno-2022'), ('xyN_wiHEimU', 'braxjuv-2turno-2022'), ('xmUydTb7muU', 'amgxava-2turno-2022'), ('4z_4jJs7Xt0', 'cuixfor-2turno-2022'), ('EQZrNHIuF3w', 'intxcam-2turno-2022'), ('yQ6scJqcmoc', 'capxsao-2turno-2022'), ('RlilubciJDg', 'flaxacg-2turno-2022'), ('U7RmcgkBxAM', 'corxbot-2turno-2022'), ('KvRTjzFHhpA', 'ceaxpal-2turno-2022')]

remaining =  """
On5dlkoCPh4,
6jrMq45C7Sc,
Gaz1OWvhH9o,
1eku81aT7AI,
a7fHplGIays,
Jc3tFtsvRd4,
TXyQ9L-TNhc,
HBKQVQ62cVs,
RVHCE_m94hs,
n2Ri-MFc2m4,
9hEMjrlKnAo,
ELAik1Oal7Q,
VDohqzlnoWg,
9Kejp2rGYMk,
jE9e4drVOQc,
Rq_7ingfdHU,
6ZsJL1YaC1g,
ufI9VRqj_is,
HDP3XYlv404,
cS9WOrq5h_U,
BY9eq0VKxuY,
46KgIFv-9XU,
PXq7oaJaRTo,
KahxDM-xZEg,
f5hpBOGpjLg,
0Gni5n81BvY,
EwUy947ppOA,
MkyQ8vsa0m0,
Ax_3hNm57cw,
mwORdXvh6VM,
OCepn1Fw7Bg,
Dyf_xBIIDe4,
bVSVbS9VS70,
-6fZDwzI0j8,
oeu-7ELalkI,
L64DUTKhF9Q,
vWpKqpHGDrs,
zdVquusVIcI,
QoOA3XA6DVI,
Hig-GKAtqkc,
lTrIDZmzUJE,
yQ4hJSGHL-0,
M4DZWWTA634,
G-DjyLlTa0A,
wc4GFWGA6Kc,
Sg-kCX6dSoE,
jg9i17oJ_zU,
hvStNgkJXiA,
l3Gxo5yQIo0,
Uh_Y-Kkl8Ko,
GlN3b2aRWdM,
0aD33hsgRHE,
iUYP8sFzOmU,
n6ipZwDuEnA,
VvP9kek2dzI,
i41Eb9RB2vc,
pK-3GV1xjdM,
b3HH9GN3NTQ,
CPxVlb84q-s,
YSMuW-Gp38M,
lyJuxevpgDM,
SK8jlPlDrgc,
HN7Hs_tzjG4,
no6g6CJZIkE,
OvKsZ8AvX10,
JxwzXRnd-Cw,
4JPn1uH1ycQ,
7IA2p4hf0ms,
lIsRCKF8mgY,
6ed-d5NU3k4,
J2-QI3KYkB0,
ZacUqNnEhms,
KhfE5V_5WpE,
0lrQvmXGTHo,
2Ctj80iW7d0,
3O0jB5MVa0M,
Llbsq5Faz9M,
6PMiloC0a4o,
AXeXAeB48Iw,
nR8mZB06OVE,
ghmtY8oK4s0,
wAnbevVroSo,
W8cPaxsKXVM,
3Ut8V0Ho2CM,
5O76QQuCDRc,
dgj8g8ACGJY,
WfABBMpraY4,
d4wJKwL46Cw,
V1-1BaH2znE,
mLWuKWmT30A,
B1R6pS6kJtE,
JPJ_-Q9-8o4,
JSWHDk1cN04,
w9yfVfibbG8,
6BBYXBbx3Jc,
6pqVuLqwCz0,
tQpREWnEcEY,
cBmQ2ScBJxU,
_IfQWOf1ryU,
164qnLceCYA,
F-0ZsXeiE7A,
-1rPa44y2mU,
ve77kdlbdL8,
n13dMNkFOR0,
vHPQYmFhVOc,
cy0bUGamLBI,
PTAa-CsjXqw,
ufCNy6fQZ08,
GMS9Om8OUlU,
-ns_w-YhHW8,
Q3qDar3fqu8,
y8K5uint7lg,
QltI532Ee14,
wr8utw405_E,
QmXYDDtgauA,
7NmIqmWcBF4,
MGBAUd2Cwqc,
lgjpZmYY9M8,
u9aXoAkob1A,
aOl0wHa44vA,
LTjrKYJOf3I,
sR0fmD6MaHs,
sVh3XjlHzwY,
IUl55RB64t4,
8W0WcYjLr7I,
qn9h91rXPpg,
FGvK8uCgbZQ,
0AX5pUL1GUY,
3Zyj6Bz-e-k,
vU4YyjcGFlE,
vWGW88HVpQU,
KNYw-UY0qBs,
LVAN94LmOzw,
_vyENYHyF5E,
RZNK0spvW7Q,
q__ns-A2NoE,
nTGEwJk_6Fo,
pVi0yxma3-c,
EblbsGUHJY4,
M3fZ9FHFq4Y,
RNDmYO3Zgd8,
HGcgwB7P280,
0nTQnkBc_Fk,
wxI_K26q_Po,
uSJMlX6pWV8,
pf5zKu0patI,
buqAsax5ipg,
fd11O8CM3ZM,
JLarfjEtV9o,
Hk7_uMZH3ps,
nH9JET4QhDU,
cRbj-tJSr88,
5z0jj1XL3B0,
7rauK6d82gU,
6S6X2up8p_g,
itrw7HgLE_w,
t8pOhl-syQg,
8fUKwN-h7Ag,
m3uFohhtyRw,
zAAtCkROT4g,
xdLOj2YK0cA,
4vrQarQDTec,
cES7PP84aQU,
tJvCfCaCuOI,
8-uQru6Jk6E,
ux1fx_xP2uk,
Q2Y06OQZZjk,
YJzVMLMyijQ,
bNX4HvOQyK8,
tK-OD4ieoAE,
iBOhm0MCinQ,
wYtjS5gcUA0,
Pctl8-S1daU,
m_smzJFxiIE,
El2yeAtsD5U,
WMhFjxplPrs,
---6M5M6bZQ,
0uULKdMX9fc,
5Virp_DeiJ0,
k08hRDywdNs,
MrM8YTptbpA,
kusHbdDHzyM,
J5gFh7Y4UJ0,
pfGvOIUTdpo,
rS2EKCJxdCw,
r6ikAWXNAAg,
YnDm8-T-EKg,
Z4ZoLty1LK4,
BPe-M2A0sY0,
qFVikWyYcSg
"""
remaining = remaining.split(",\n")
remaining[-1] = remaining[-1].replace("\n", "")
remaining[0] = remaining[0].replace("\n", "")
print(remaining)
#print(views)

#for video_id, _ in mapIdToVideoName_2022:
for video_id in remaining:
    # command: youtube-dl --write-annotations --write-info-json --skip-download www.youtube.com/yourvideo
    #command = f"yt-dlp --write-info-json --skip-download https://www.youtube.com/watch?v={video_id}"
    # Será necessário padronizar o saida do arquivo json para pegar o campo view_count
    # usando o -o "{video_id}.%(ext)s"
    command = f"yt-dlp --write-info-json --skip-download -o {video_id} https://www.youtube.com/watch?v={video_id}"
    subprocess.run(command, shell=True, check=True)
        
    print(f"Comando executado: {command}")
    print("Salvo no arquivo: ", f"./{video_id}.info.json)")
    
    with open(f"./{video_id}.info.json", 'r', encoding='utf-8') as f:
        video_info = json.load(f)
        views[video_id] = video_info['view_count']
    #views[video_id] = subprocess.check_output(command, shell=True).decode('utf-8')
    
    print(f"Views do vídeo {video_id}: ", views[video_id])

    wait_time = random.randint(1, 10)
    print(f"Aguardando {wait_time:.2f} segundos...")
    time.sleep(wait_time)

print(views)
df = pd.DataFrame(views.items(), columns=['id', 'views'])
df.to_csv("views_2022.csv", index=False, encoding='utf-8')

df = pd.read_csv("brzao2022.csv")
df['views'] = df['id'].map(views)
df.to_csv("brzao2022.csv", index=False, encoding='utf-8')

