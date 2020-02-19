import pandas as pd
import os

galago_path = os.path.join(os.getcwd(), 'galago.eval')
anserini_path = os.path.join(os.getcwd(), 'anserini.eval')

def get_data(path, name):

    data = []
    with open(path, 'r') as f:
        for l in f:
            if 'enwiki:' in l:
                data.append(l.split())

    df = pd.DataFrame(data=data, columns=['metrics', 'query', name])
    df[name] = df[name].astype(float)
    return df


def join_galago_anserini():

    galago_df = get_data(path=galago_path, name='galago')
    anserini_df = get_data(path=anserini_path, name='anserini')

    df = galago_df.merge(right=anserini_df, how='outer', on=['metrics', 'query'])

    df['galago_best'] = df['galago'] - df['anserini']
    df['anserini_best'] =  df['anserini'] - df['galago']
    df['abs_diff'] = abs(df['galago'] - df['anserini'])


    return df

if __name__ == '__main__':

    df = join_galago_anserini()
    df.to_csv(os.path.join(os.getcwd(), 'df.csv'), index=False)