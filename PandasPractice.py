import pandas as pd
import glob

data = list()
for filePath in glob.glob('./res_gossiping_2/*.txt'):
#    print(filePath)
    with open(filePath, 'r', encoding='utf-8') as f:
        tmpList = f.read().split('---split---')[1].split('\n')[1:-1]
        data.append(tmpList)

columns = [r.split(': ')[0] for r in data[0]]

print(columns)
df = pd.DataFrame(data=data, columns=columns)

df.to_csv('./result/ptt_index.csv', index=False, encoding='utf-8-sig')
