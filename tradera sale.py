import requests
import pandas as pd
items = []
for i in range(1, 206):
    try:
        r = requests.get(f'https://www.tradera.com/profile/items/4835264/roffesbonader.json?page={i}')
        if r.ok:
            janson = r.json()
            for item in janson['items']:
                items.append(item)
        print(i)
    except:
        pass
df = pd.json_normalize(items)
df.to_csv('seller.csv', index=False)
