import requests
import pandas as pd
from tqdm import tqdm
items = []
seller = input('Seller url:\n')
janson_Url = seller+'.json'
pages = requests.get(janson_Url).json()['pagination']['pageCount']
if int(pages) == 0:
    pages = 1
for i in tqdm(range(1, int(pages)+1)):
    try:
        r = requests.get(f'{janson_Url}?page={i}')
        if r.ok:
            janson = r.json()
            for item in janson['items']:
                items.append(item)
    except:
        pass
df = pd.json_normalize(items)
df.to_csv(f'{seller.split("/")[-1]}.csv', index=False)
