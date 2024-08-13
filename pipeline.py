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
import os

# ---------------------------------------------------------------------------------------
#mapIdToVideoName = [('NAqZEW9goNc', 'cruxcap-1turno-2024')]

mapIdToVideoName_2023 = [
        ('I8NKXi4aoxE', 'palxcui-1turno-2023'), ('v-e_5mHOBdI', 'capxgoi-1turno-2023'), ('Wli77j_au6c', 'camxvas-1turno-2023'), ('uruWA79AmMw', 'flaxcfc-1turno-2023'), ('JvlrWaXKCKU', 'corxcru-1turno-2023'), ('deODK5cSwHU', 'forxint-1turno-2023'), ('9E7j3TJsVVM', 'grexsan-1turno-2023'), ('NIkH9IpGyPs', 'fluxcap-1turno-2023'), ('hvL7_wTtPzo', 'saoxamg-1turno-2023'), ('qsWVm7tukOY', 'cuixbra-1turno-2023'), ('oyc4Fp3k_Lg', 'cruxgre-1turno-2023'), ('UWcO4V1My-A', 'intxfla-1turno-2023'), ('lrWcg4MfB24', 'sanxcam-1turno-2023'), ('jJIHhTRkd84', 'vasxpal-1turno-2023'), ('N27srU6Gud8', 'crcxfor-2023-1turno'), ('4V0x08bzStw', 'goixcor-1turno-2023'), ('SIbyF-fuxp0', 'crcxsao-1turno-2023'), ('_qgRIrmfU20', 'forxflu-1turno-2023'), ('IrYyQKEfYqs', 'palxcor-1turno-2023'), ('uXCZxWnxbmU', 'sanxamg-1turno-2023'), ('h6as7KHQfWE', 'camxcap-1turno-2023'), ('ENVPqj3OYLU', 'flaxbot-1turno-2023'), ('x34Jn_uUz8c', 'intxgoi-1turno-2023'), ('x34Jn_uUz8c', 'intxgoi-1turno-2023'), ('ihMfSbPG5OE', 'cuixgre-1turno-2023'), ('EJ_n2PB5QVw', 'vasxbah-1turno-2023'), ('o75UjMT3S3c', 'cruxsan-1turno-2023'), ('UAdqlL9Ta9I', 'fluxvas-1turno-2023'), ('hj8Yif7Ly44', 'amgxcui-1turno-2023'), ('o_V1PkXDyEs', 'capxfla-1turno-2023'), ('DUpLbmH62fU', 'saoxint-1turno-2023'), ('4o1RQg3azIo', 'bahxcor-1turno-2023'), ('_VoKOsF41Ak', 'botxcam-1turno-2023'), ('qtwodxQwhdc', 'goixpal-1turno-2023'), ('pLByAFU4uZw', 'grexbra-1turno-2023'), ('jfN6kUrdqW0', 'corxfor-1turno-2023'), ('k91ojMextVc', 'intxcap-1turno-2023'), ('7q6MgCu7wOc', 'braxamg-1turno-2023'), ('omm_9rKWmO0', 'sanxbah-1turno-2023'), ('PAC7p2Jg8EY', 'cuixcam-1turno-2023'), ('p54b83Fr3I8', 'flaxgoi-1turno-2023'), ('J6cxWtbNAPo', 'palxgre-1turno-2023'), ('Ab8yFyqtHQo', 'cruxflu-1turno-2023'), ('vPtcuUvgovw', 'corxvas-1turno-2023'), ('PepRWyEoun0', 'botxcor-1turno-2023'), ('Bu-enW6FK2M', 'forxsao-1turno-2023'), ('9dQSeQ4q2nI', 'bahxfla-1turno-2023'), ('tHqk5QF_gIU', 'fluxcui-1turno-2023'), ('iw2uQ8dEIuE', 'palxbra-1turno-2023'), ('EfA8UUy4FmU', 'camxint-1turno-2023'), ('R9qw29SfbiA', 'vasxsan-1turno-2023'), ('8YjMw7afGb4', 'corxsao-1turno-2023'), ('0Y6LBpayQlk', 'grexfor-1turno-2023'), ('W457m3FkF7w', 'amgxcru-1turno-2023'), ('iDQl3LpR-LM', 'capxcor-1turno-2023'), ('E3n9WEsm2xU', 'bahxgoi-1turno-2023'), ('DX1S233fSW8', 'braxcap-1turno-2023'), ('qtCXKI13Ykc', 'amgxfor-1turno-2023'), ('3WrVN9SAthA', 'botxflu-1turno-2023'), ('xaDhdH26GX0', 'crcxcam-1turno-2023'), ('ZbNk5XSpDaI', 'saoxvac-1turno-2023'), ('yO4VPjrt6Ws', 'sanxpal-1turno-2023'), ('HZogEtjdWIg', 'flaxcor-1turno-2023'), ('trdUsEUHATM', 'grexint-1turno-2023'), ('rm6QmVD32iI', 'cruxcui-1turno-2023'), ('AML0OkI9dh4', 'capxgre-1turno-2023'), ('iR1T3GM6wbA', 'forxvas-1turno-2023'), ('v9HY-2H4DcQ', 'flaxcru-1turno-2023'), ('Jn2MsAjBkpA', 'cuixcor-1turno-2023'), ('Vft0kdWGYEE', 'saoxgoi-1turno-2023'), ('yogGxspNprw', 'corxflu-1turno-2023'), ('2Qqw2eSfsH8', 'intxbah-1turno-2023'), ('XzRRuVPzbnI', 'braxsan-1turno-2023'), ('KLrxQfQYs9k', 'camxpal-1turno-2023'), ('iKxvvZ77RRE', 'botxamg-1turno-2023'), ('PijCj3jBG2M', 'forxbah-1turno-2023'), ('WtBwtw4OuEY', 'amgxcor-1turno-2023'), ('fuRDJcnLmEE', 'cruxcam-1turno-2023'), ('0hk6FAa-hhs', 'sanxint-1turno-2023'), ('R8EpqebdXeg', 'fluxbra-1turno-2023'), ('5fsXlFFhAdg', 'grexsao-1turno-2023'), ('rAivMCFNXpc', 'goixcui-1turno-2023'), ('fsb3hdFbVU8', 'palxcor-1turno-2023'), ('wO0n2Rc1s80', 'vasxfla-1turno-2023'), ('_MB-SCfSGbs', 'corxsan-1turno-2023'), ('jEsc2ySCPV0', 'corxcui-1turno-2023'), ('sDZ9Nf2O6t4', 'bahxcru-1turno-2023'), ('lmwEnRh7FEs', 'botxfor-1turno-2023'), ('6CRfI7Epodc', 'amgxcap-1turno-2023'), ('sjx6lzIJKs0', 'intxvas-1turno-2023'), ('B4wESwdGLqM', 'saoxpal-1turno-2023'), ('UfCtSMKe6kw', 'goixflu-1turno-2023'), ('9dpnJRrZ-Qo', 'saoxcap-1turno-2023'), ('KZ8FehVCqvs', 'cruxfor-1turno-2023'), ('AsJZbFxs1p8', 'sanxcor-1turno-2023'), ('C6nbZ6muN2s', 'bahxpal-1turno-2023'), ('u3aj497YT2Y', 'fluxcam-1turno-2023'), ('TJwptQZM7v8', 'grexamg-1turno-2023'), ('JqBorEKVev8', 'vasxgoi-1turno-2023'), ('qj9AN1PEiG4', 'corxint-1turno-2023'), ('mB2lDn43xRs', 'cuixbot-1turno-2023'), ('2S-m_HySl04', 'braxfla-1turno-2023'), ('qxNulbdWAvg', 'capxcor-1turno-2023'), ('vH0q9g5CA8g', 'fluxbah-1turno-2023'), ('h9HlsKo1vRo', 'forxcam-1turno-2023'), ('ql__UfFI0jU', 'cruxsao-1turno-2023'), ('rxnFFj8pxXU', 'palxbot-1turno-2023'), ('754NaPM6xxc', 'grexcor-1turno-2023'), ('jusoT-jenSQ', 'amgxint-1turno-2023'), ('5FXvX2mPjP0', 'sanxfla-1turno-2023'), ('9faykKm-NNo', 'braxgoi-1turno-2023'), ('qkwZ9LlhqII', 'vasxcui-1turno-2023'), ('OtJbR5NLgJ4', 'saoxflu-1turno-2023'), ('rxUzegPiKYM', 'flaxfor-1turno-2023'), ('aNusHZp-F7s', 'bahxgre-1turno-2023'), ('lsbwNZGBNJs', 'intxcru-1turno-2023'), ('2mvyQ2ozRTA', 'corxbra-1turno-2023'), ('OYSv4ocKJes', 'camxamg-1turno-2023'), ('esOxZyD0Yxo', 'capxpal-1turno-2023'), ('GwD4J7d6mLw', 'botxvas-1turno-2023'), ('kjzwhedD_9U', 'cuixsan-1turno-2023'), ('sFkliCCl-h8', 'goixcrc-1turno-2023'), ('mZ4uAAjH9gg', 'cuixbah-1turno-2023'), ('VBlP7vvT9SM', 'vasxcru-1turno-2023'), ('2Pbxo4mFLb8', 'camxcor-1turno-2023'), ('vfWEXQmCzzk', 'corxamg-1turno-2023'), ('37ieZKq9gnQ', 'palxfla-1turno-2023'), ('UxI5XJQszT8', 'sanxgoi-1turno-2023'), ('JHdl_MaaWbg', 'braxsao-1turno-2023'), ('qkm0_n9vszo', 'fluxint-1turno-2023'), ('2ffAdoUFPpE', 'grexbot-1turno-2023'), ('llJrTI6Jr-g', 'forxcap-1turno-2023'), ('nMcN5IPljwY', 'cruxcor-1turno-2023'), ('F5VWycfkjyo', 'forxcui-1turno-2023'), ('_9jlaY7gRfc', 'intxpal-1turno-2023'), ('DYsEAkrAm68', 'capxbah-1turno-2023'), ('cBYZ5qCbmTQ', 'goixcam-1turno-2023'), ('sr2T7GZeCP8', 'flaxamg-1turno-2023'), ('uq-pmKZSl3Q', 'bahxcor-1turno-2023'), ('MLo5zDcCUNs', 'cuixsao-1turno-2023'), ('p5M4WqU91Hw', 'grexcam-1turno-2023'), ('M_DVQtTK3HE', 'braxint-1turno-2023'), ('kTrbM2YT1Ek', 'cruxgoi-1turno-2023'), ('hOTWykI0364', 'sanxbot-1turno-2023'), ('51SHWOapQ_w', 'vasxcap-1turno-2023'), ('5d5WxkaUJjo', 'corxflu-1turno-2023'), ('pfABJ30vQw8', 'fluxsan-1turno-2023'), ('EsU0LVwN9rQ', 'intxcui-1turno-2023'), ('G6IMDUbjw0M', 'forxbra-1turno-2023'), ('iReFc_gwOi4', 'corxvas-1turno-2023'), ('3vDMkYk8M7Y', 'capxcru-1turno-2023'), ('3VWzL0bOYfg', 'camxfla-1turno-2023'), ('24HhvqAKmUA', 'saoxbah-1turno-2023'), ('-vNO-ugZB4M', 'amgxpal-1turno-2023'), ('0OWGvwwY1BM', 'botxcor-1turno-2023'), ('7NTn6Gsim18', 'goixgre-1turno-2023'), ('HVYSgqMs6eo', 'sanxcap-1turno-2023'), ('lchnVMCLGKs', 'intxcor-1turno-2023'), ('rcBCrwJmgdI', 'goixfor-1turno-2023'), ('CyGLFmlO7PU', 'fluxpal-1turno-2023'), ('CWp78UoAow8', 'vasxgre-1turno-2023'), ('Fz1pCBWVEzU', 'saoxcam-1turno-2023'), ('PpTsEJBuEbc', 'cruxbot-1turno-2023'), ('QXZnxsbxP2I', 'corxbra-1turno-2023'), ('NeAq068msrk', 'cuixfla-1turno-2023'), ('Ox-nkfqPuZI', 'bahxamg-1turno-2023'), ('9IVLwIucagc', 'botxint-2turno-2023'), ('ririyaOGla0', 'camxbah-2turno-2023'), ('yuqSzNDzJgI', 'amgxgoi-2turno-2023'), ('prqFVF1G8qg', 'grexflu-2turno-2023'), ('tkg-tDMu3A0', 'corxcrc-2turno-2023'), ('6U6rSYRv9EQ', 'forxsan-2turno-2023'), ('8v4JtoNq_yg', 'flaxsao-2turno-2023'), ('8QG-PFHCsoQ', 'palxcru-2turno-2023'), ('D1W9DUk-x-I', 'braxvas-2turno-2023'), ('z_1I4_aM7Cg', 'intxfor-2turno-2023'), ('9gfyGApWGBY', 'saoxbot-2turno-2023'), ('DFM35bBMtng', 'cuixpal-2turno-2023'), ('2rcK6pBk92c', 'fluxamg-2turno-2023'), ('aBwgIsuVFzY', 'cruxcor-2turno-2023'), ('NQ1jRkjQ_q0', 'vasxcam-2turno-2023'), ('7osEfcMom6A', 'corxfla-2turno-2023'), ('aiyw-Ivlt6I', 'sanxgre-2turno-2023'), ('SACcFEpRqCo', 'bahxbra-2turno-2023'), ('WjpLMB_DysM', 'goixcap-2turno-2023'), ('9GmVqKSK4SE', 'flaxint-2turno-2023'), ('v29iiPP8Khc', 'corxgoi-2turno-2023'), ('ZvxT9R8CatM', 'braxcui-2turno-2023'), ('YkndJ196Ci0', 'botxbah-2turno-2023'), ('r84HfWkg-O0', 'amgxsao-2turno-2023'), ('G3qG2jqI4Zo', 'forxcor-2turno-2023'), ('OI2HO6MfmiU', 'palxvas-2turno-2023'), ('sPdyQLFQr5c', 'capxflu-2turno-2023'), ('WoKQtmYBHgY', 'grexcru-2turno-2023'), ('pZcXU6ePO_U', 'goixint-2turno-2023'), ('nna5MPybgD8', 'botxfla-2turno-2023'), ('lHj508Eflsc', 'corxpal-2turno-2023'), ('hehQTravoXM', 'bahxvas-2turno-2023'), ('ak15L2yNHhI', 'flaxcap-2turno-2023'), ('eZ-ol-BqeqA', 'intxsao-2turno-2023'), ('Ar1QKv_-Vb8', 'forxcor-2turno-2023'), ('jOImdYYtVW8', 'crcxbah-2turno-2023'), ('UfRFpUw_4kU', 'braxgre-2turno-2023'), ('VEw8AHmPbxE', 'sanxcru-2turno-2023'), ('6koZrYFETI8', 'cuixamg-2turno-2023'), ('eEn-zFECvW4', 'palxgoi-2turno-2023'), ('VOk_kg0uiYI', 'vasxflu-2turno-2023'), ('ZjH8fVh-_wk', 'camxbot-2turno-2023'), ('QNYZIILYBv4', 'corxgre-2turno-2023'), ('qVzrSuYixK0', 'amgxbra-2turno-2023'), ('sbcm-82EWss', 'goixfla-2turno-2023'), ('Gvqn75hii-Y', 'saoxfor-2turno-2023'), ('fh2rSEVCGvA', 'fluxcru-2turno-2023'), ('Alg8-7gjqX0', 'vasxcor-2turno-2023'), ('5XdxaMOLIIg', 'capxint-2turno-2023'), ('bNY1b2ljM2Y', 'grexpal-2turno-2023'), ('hhrg7cu-nMA', 'corxbot-2turno-2023'), ('_y9dLZvhHO0', 'amgxvas-2turno-2023'), ('rkCM_w0w4rQ', 'flaxbah-2turno-2023'), ('rAJ-u7ZGw7s', 'forxgre-2turno-2023'), ('ODNwwb131kc', 'cuixflu-2turno-2023'), ('D6O7dqTy9P8', 'saoxcor-2turno-2023'), ('YVCxLM-p9Wg', 'intxcam-2turno-2023'), ('Ot20JfF3VNo', 'corxcap-2turno-2023'), ('LlIH4cN_t2U', 'sanxvas-2turno-2023'), ('0TotX_VPVks', 'cruxamg-2turno-2023'), ('t_6ojQeVfgA', 'braxpal-2turno-2023'), ('iuh7upjTStg', 'goixbah-2turno-2023'), ('zsQlPD-4egw', 'vasxsao-2turno-2023'), ('NTSLHMYnE98', 'corxfla-2turno-2023'), ('2eEONdyxnRY', 'palxsan-2turno-2023'), ('etDqq0AVzLg', 'fluxbot-2turno-2023'), ('1BwRkcSy96I', 'intxgre-2turno-2023'), ('Jkw8WbjWi9w', 'camxcor-2turno-2023'), ('5RNGb3GCy1Y', 'forxamg-2turno-2023'), ('9_i_Iq1-lko', 'cuixcru-2turno-2023'), ('BbzTgrijT1A', 'grexcap-2turno-2023'), ('6Ui7Dynw2iA', 'goixsao-2turno-2023'), ('8x-Ym2VqEhU', 'vasxfor-2turno-2023'), ('1UnxgatcDqQ', 'cruxfla-2turno-2023'), ('UT5hLz8ANoY', 'palxcam-2turno-2023'), ('GH81W9pMQDw', 'sanxbra-2turno-2023'), ('1YvjcvMCI3k', 'fluxcor-2turno-2023'), ('AGTt9MEJ8OE', 'saoxgre-2turno-2023'), ('fwHheaL2GDo', 'botxcap-2turno-2023'), ('8_Y3AY28PYI', 'botxcap-2turno-2023'), ('XR69lJ_B7kE', 'flaxvas-2turno-2023'), ('rtJXoblicWk', 'intxsan-2turno-2023'), ('j02eYyzuTk0', 'camxcru-2turno-2023'), ('zBYDCJKvEZM', 'corxamg-2turno-2023'), ('vBxJiAIeJ6k', 'braxflu-2turno-2023'), ('Dlw7ckPUHzA', 'corxpal-2turno-2023'), ('k2jWqYrSDko', 'braxcam-2turno-2023'), ('5vXYLs90d98', 'fluxgoi-2turno-2023'), ('LaE3MLAe1QY', 'capxamg-2turno-2023'), ('Mv9Cb8WlrFc', 'cruxbah-2turno-2023'), ('E5Yn6JdFC9A', 'palxsao-2turno-2023'), ('YJOJnimeEzk', 'cuixcor-2turno-2023'), ('jBdJJhGEsu8', 'grexfla-2turno-2023'), ('jBdJJhGEsu8', 'vasxint-2turno-2023'), ('AvDZyOo4ST0', 'sanxcor-2turno-2023'), ('kKRkT01W1AM', 'amgxgre-2turno-2023'), ('zE4RVpyHQgE', 'palxbah-2turno-2023'), ('ahVvYGAYAU0', 'camxflu-2turno-2023'), ('6ox2cINoNfQ', 'capxsao-2turno-2023'), ('ZsF9rGU2aMo', 'goixvas-2turno-2023'), ('__RYbPj0lb8', 'corxsan-2turno-2023'), ('7eUonAJ9_JY', 'intxcrc-2turno-2023'), ('NqMbfQ_vWz8', 'botxcui-2turno-2023'), ('FtfwrJ9jNqQ', 'chaxtom-2turno-2023'), ('hvK0zuR8O5I', 'bahxflu-2turno-2023'), ('52uU2WUmKGk', 'intxamg-2turno-2023'), ('U0QGjRN4OG0', 'flaxsan-2turno-2023'), ('AgimpkmxMSQ', 'corxgre-2turno-2023'), ('Z8YtuRj5p20', 'botxpal-2turno-2023'), ('7JJ0NreHY-o', 'camxfor-2turno-2023'), ('k6CpaTx-6Zw', 'cuixvas-2turno-2023'), ('Fii13oLPlmA', 'goixbra-2turno-2023'), ('OpiExzXO6Qc', 'saoxcru-2turno-2023'), ('qd4IMLLzDOk', 'grexbah-2turno-2023'), ('drEhBKvaU58', 'amgxcam-2turno-2023'), ('1miok4MMz0k', 'palxcap-2turno-2023'), ('UPhpVR4Omxk', 'braxcor-2turno-2023'), ('PHUQ9S05UqQ', 'cruxint-2turno-2023'), ('hDfmhdtaIZw', 'forxfla-2turno-2023'), ('gEFBInBIZgI', 'corxgoi-2turno-2023'), ('zkR2h6Z3F-8', 'vasxbot-2turno-2023'), ('HyC_7BjV2Io', 'sanxcui-2turno-2023'), ('5IaWmEvTO_E', 'amgxcor-2turno-2023'), ('eCcCKsRG2lw', 'intxflu-2turno-2023'), ('c147OwpIxqI', 'capxfor-2turno-2023'), ('9bAMc9fjbFQ', 'saoxbra-2turno-2023'), ('0R1AU9ZL3Y0', 'flaxpal-2turno-2023'), ('ys_IyJVCJBE', 'goixsan-2turno-2023'), ('rABjOGT1d2c', 'corxcam-2turno-2023'), ('UamMxlX5ADY', 'botxgre-2turno-2023'), ('oB3_SujbqQI', 'bahxcui-2turno-2023'), ('8UsETPz261g', 'corxcru-2turno-2023'), ('883O6dRuLVc', 'palxint-2turno-2023'), ('cl5QlHVCsYI', 'braxbot-2turno-2023'), ('PCo4fG6E1MM', 'grexcor-2turno-2023'), ('kEAbg4qfTIg', 'bahxcap-2turno-2023'), ('BqciONJw5aE', 'vasxamg-2turno-2023'), ('ue5mAfQucoA', 'camxgoi-2turno-2023'), ('XALXbJQ7vFY', 'cuixfor-2turno-2023'), ('szDL6HRJECc', 'forxcru-2turno-2023'), ('rA2H3xhwTRw', 'cruxvas-2turno-2023'), ('ZeIlRhWTqnw', 'fluxvas-2turno-2023'), ('hsdj82k0kuE', 'forxbot-2turno-2023'), ('XAzhlZz_4hU', 'flaxbra-2turno-2023'), ('k2Ep1eIJROs', 'corxbah-2turno-2023'), ('3HjFifPB3Rc', 'capxvas-2turno-2023'), ('-A2T98U2_T4', 'fluxcor-2turno-2023'), ('Qn4-61V-y40', 'camxgre-2turno-2023'), ('fojrgNpZrtg', 'botxsan-2turno-2023'), ('wn4YOuwQmVM', 'amgxfla-2turno-2023'), ('hi0rYsClPkg', 'saoxcui-2turno-2023'), ('vDHIC1Owj_o', 'forxpal-2turno-2023'), ('NZJNn9gOOiw', 'intxbra-2turno-2023'), ('1cGbzf5hZm8', 'goixcru-2turno-2023'), ('WfT-E45VJaE', 'vasxcor-2turno-2023'), ('73y4d9xjCtc', 'sanxflu-2turno-2023'), ('f0UdnDKaOyE', 'flaxcam-2turno-2023'), ('VbPrpTbk1gg', 'cuixint-2turno-2023'), ('ztcMyvESLt8', 'bahxsao-2turno-2023'), ('bc9x4N3qY-M', 'corxbot-2turno-2023'), ('WLC6lys-PRQ', 'grexgoi-2turno-2023'), ('mE58rqeOkMI', 'cruxcap-2turno-2023'), ('8GJhLL6sgts', 'braxfor-2turno-2023'), ('5WqQ5ysu2pM', 'corxint-2turno-2023'), ('vR7FfX8pnHY', 'camxsao-2turno-2023'), ('C1YVKTNPDhM', 'flaxcui-2turno-2023'), ('J0tUlc4Y3X8', 'forxgoi-2turno-2023'), ('FPQ5p24a1LQ', 'botxcru-2turno-2023'), ('KrbsC2a1IBI', 'braxcor-2turno-2023'), ('1rzapeRwpNU', 'goixamg-2turno-2023'), ('xtCODWmE6CQ', 'cruxpal-2turno-2023'), ('bqnv4lUwAtw', 'bahxcam-2turno-2023'), ('ZFBFOdOA7bE', 'sanxfor-2turno-2023'), ('mrHB279hp1w','cuixcap-2turno2023'), ('s4Jln2NlfgA', 'intxbot-2turno-2023'), ('e5ZJtDFjmPM', 'fluxgre-2turno-2023'), ('JtXCs35NcYI', 'crcxcor-2turno-2023'), ('zRM_Pu-vzs4', 'saoxfla-2turno-2023')]


# Parei no vídeo 176 

ids_1st_turno_2022 = []

matches_2022 = pd.read_csv("brzao2022.csv")
for index, row in matches_2022.iterrows():
    ids_1st_turno_2022.append((row['id'], row['label']))

#mapIdToVideoName_2022 = ids_1st_turno_2022 + mapIdToVideoName_2022

mapIdToVideoName_2021 = []

matches_2021 = pd.read_csv("brzao2021.csv")
for index, row in matches_2021.iterrows():
    mapIdToVideoName_2021.append((row['id'], row['label']))

ids_2022 = pd.read_csv("views_2022.csv")
ids_2022 = list(ids_2022['id'])

# ---------------------------------------------------------------------------------------

def download_comments(video_id, output_file):
    subprocess.run([
        'youtube-comment-downloader',
        '--youtubeid', video_id,
        '--output', output_file
    ])

    print(f"Comentários do vídeo {video_id} salvos em {output_file}")


def load_and_process_comments(input_file_name):
    #with open(input_file, 'r', encoding='utf-8') as f:
    #    comments = [json.load(line) for line in f]
    #df = pd.DataFrame(comments)

    path = os.path.join('./data/2023/', input_file_name)

    with open(path, 'r', encoding='utf-8') as f:
        comments = [json.loads(line) for line in f]
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

blocklist = ['UYP8VzcILsc', 'f5hpBOGpjLg']

def pipeline(video_ids):
    for video_id in video_ids:
        output_file = f"{video_id}_comments.json"

        if (video_id[0] == '-'):
            blocklist.append(video_id)

        if (video_id in blocklist):
            print("Arquivo na blocklist, pulando para o próximo vídeo...")
            continue

        # Verifica se o arquivo de comentários já foi baixado
        if os.path.exists('./data/2023/' + output_file):
            print(f"Arquivo {output_file} já existe...")
            print(f"Verificando se o arquivo NLP já existe...")
            if os.path.exists(f"./data/2023/{video_id}_comments_for_nlp.csv"):
                print(f"Pulanado para o próximo vídeo...")
            else:
                print("Arquivo NLP não existe, criando...")
                df = load_and_process_comments(output_file)
                df_anonymized = anonymize_data(df)
                df_nlp = prepare_for_nlp(df_anonymized)
                save_date(df_nlp, f"{video_id}_comments_for_nlp.csv")

            continue


        download_comments(video_id, output_file)

        wait_time = random.randint(1, 20)
        print(f"Aguardando {wait_time:.2f} segundos...")
        time.sleep(wait_time)
        print("Tentando abrir o arquivo: ", output_file)



        df = load_and_process_comments(output_file)
        df_anonymized = anonymize_data(df)
        df_nlp= prepare_for_nlp(df_anonymized)

        save_date(df_nlp, f"{video_id}_comments_for_nlp.csv")




video_ids = []

#for video_id, _ in mapIdToVideoName_2022:
#    video_ids.append(video_id)

for video_id, _ in mapIdToVideoName_2023:
    video_ids.append(video_id)

#for video_id, _ in mapIdToVideoName_2021:
#    video_ids.append(video_id)


# Inicia o pipeline
print("Iniciando pipeline...")
print("Video IDs:", video_ids)


# Contando a quantidade de comentários que veio de cada vídeo para fazer uam caracterização
# do volume de dados

#contagem_comentarios = {}

#for video_id in video_ids:
#    output_file = f"{video_id}_comments.json"
#    with open(output_file, 'r', encoding='utf-8') as f:
#        comments = [json.load(line) for line in f]
#    contagem_comentarios[video_id] = len(comments)

# Contando quais ids já tem os arquivos csv de comentários baixados
#count = 0
#for video_id in video_ids:
#    output_file = f"./data/2022/{video_id}_comments_for_nlp.csv"
#    if os.path.exists(output_file):
#        print(f"Arquivo {output_file} já existe. Pulando para o próximo vídeo...")
#        continue
#    if video_id[0] == '-':
#        print(f"Arquivo {output_file} na blocklist. Pulando para o próximo vídeo...")
#        continue
#    print("Arquivo não foi baixado: ", output_file)
#    count = count + 1
#print(f"Total de vídeos que ainda não foram processados: {count}")

#pipeline(video_ids)

# Fazendo o append dos ids dos vídeos de 2022 2 turno dentro do arquivo csv "brzao2022 - jogos.csv"

#ids_1st_turno_2022 = []
#matches_2022 = pd.read_csv("brzao2022 - jogos.csv")
#for index, row in matches_2022.iterrows():
#    ids_1st_turno_2022.append((row['label'], row['id'], row['rodada']))
#
## Adicionando os ids dos jogos do 2 turno de 2022
#for video_id, label in mapIdToVideoName_2022:
#    ids_1st_turno_2022.append((label, video_id, 0))
#
## Salvando no csv
#df = pd.DataFrame(ids_1st_turno_2022, columns=['label', 'id', 'rodada'])
#df.to_csv("brzao2022 - jogos - teste.csv", index=False, encoding='utf-8')

# Criando csv para os jogos de 2023

ids_1st_turno_2023 = []
#

aux = pd.read_csv("views_2023.csv")
aux = list(aux['id'])


for video_id,label in mapIdToVideoName_2023:
    ids_1st_turno_2023.append((label, video_id, 0))

df = pd.DataFrame(ids_1st_turno_2023, columns=['label', 'id', 'rodada'])
df.to_csv("brzao2023.csv", index=False, encoding='utf-8')


## Getting the views number of each video
## Using the youtube-dl to get the views number of each video
import subprocess
views = {}



for video_id, _ in mapIdToVideoName_2023:
    # command: youtube-dl --write-annotations --write-info-json --skip-download www.youtube.com/yourvideo
    #command = f"yt-dlp --write-info-json --skip-download https://www.youtube.com/watch?v={video_id}"
    # Será necessário padronizar o saida do arquivo json para pegar o campo view_count
    # usando o -o "{video_id}.%(ext)s"
    
    if os.path.exists(f"./metadata/2023/{video_id}.info.json"):
        print(f"Arquivo {video_id}.info.json já existe...")
        with open(f"./metadata/2023/{video_id}.info.json", 'r', encoding='utf-8') as f:
            video_info = json.load(f)
            views[video_id] = video_info['view_count']
        continue

    command = f"yt-dlp --write-info-json --skip-download -o {video_id} https://www.youtube.com/watch?v={video_id}"
    subprocess.run(command, shell=True, check=True)
        

    # Printando resultado do comando
    print(f"Comando executado: {command}")
    print("Salvo no arquivo: ", f"./{video_id}.info.json)")
    
    # This command will returno a json file with the video information
    # We need to get the field "view_count" from this json file
    with open(f"./metadata/2023/{video_id}.info.json", 'r', encoding='utf-8') as f:
        video_info = json.load(f)
        views[video_id] = video_info['view_count']
    #views[video_id] = subprocess.check_output(command, shell=True).decode('utf-8')
    
    print(f"Views do vídeo {video_id}: ", views[video_id])
    # Esperando um tempo aleatório para fazer a próxima requisição
    wait_time = random.randint(1, 10)
    print(f"Aguardando {wait_time:.2f} segundos...")
    time.sleep(wait_time)

print(views)
# Salvar resultado em um arquivo csv
df = pd.DataFrame(views.items(), columns=['id', 'views'])
df.to_csv("views_2023.csv", index=False, encoding='utf-8')

# Adding the views number to the csv file in a new column

df = pd.read_csv("brzao2023.csv")
df['views'] = df['id'].map(views)
df.to_csv("brzao2023.csv", index=False, encoding='utf-8')




