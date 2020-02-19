
import matplotlib.pyplot as plt
import pandas as pd
import os

def get_biggest_diff(df, col, metric='map'):
    df_metrics = df[df['metrics'] == metric]
    return df_metrics.sort_values(col, ascending=False)



if __name__ == '__main__':

    df = pd.read_csv(os.path.join(os.getcwd(), 'df.csv'))

    df_metrics = get_biggest_diff(df=df, col='anserini_best', metric='map')
    df_metrics.to_csv(os.path.join(os.getcwd(), 'map_diff.csv'), index=False)

    abs_diff = 0.03
    inputs = df_metrics[df_metrics['abs_diff'] > abs_diff]['anserini_best']
    n = len(inputs) / len(df_metrics)

    # the histogram of the data
    plt.hist(inputs, 50, density=False, facecolor='g', alpha=0.75)
    plt.ylabel('Count -> {:.2f}% of data i.e. queries with abs MAP diff > {:.2f}'.format(n, abs_diff))
    plt.xlabel('Anserini MAP minus Galago MAP')
    plt.title('Anserini vs. Galago - histogram of tree-hierarchical (abs diff > {:.2f})'.format(abs_diff))
    plt.grid(True)
    #plt.show()
    plt.savefig('hist.png')







