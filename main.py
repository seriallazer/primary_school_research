import pandas as pd
import json

data_dir = './research_data/'

## This script has data for 2CS
## Change the data for other phases from here: https://elite.com.sg/ballot


def primary_school_research():
    data = json.load(open('./school_data.json'))
    ll = len(data['props']['pageProps']['sortedSchools'])
    print("Num-schools:", ll)
    df = pd.DataFrame(data['props']['pageProps']['sortedSchools'])
    kl = list(df.schoolInfo)
    df['schoolName'] = df.schoolInfo.apply(lambda x: x['schoolName'])
    df['schoolArea'] = df.schoolInfo.apply(lambda x: x['schoolArea'])

    bdf = pd.read_csv('./research_data/myra_school_ballotdata.csv')
    kdf = df.merge(bdf, how='left', left_on='schoolName', right_on='School')
    pdf = kdf[kdf.Avail > 0]
    pdf = pdf.sort_values(by=['rank'])

    df.to_csv('./research_data/ranking_data.csv')
    pdf.to_csv('./research_data/summary_data_2csuppAvail.csv')

    gdf = pdf.groupby(by='schoolArea')['rank'].count().reset_index().rename(columns={'rank': 'total_score'})
    gdf = gdf.sort_values(by=['total_score'], ascending=False)
    print(gdf)


primary_school_research()
