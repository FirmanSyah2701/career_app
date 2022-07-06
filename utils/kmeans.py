import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def predict():
    df = pd.read_csv('students.csv', sep = ",")

    data_question = df.loc[:, 'pernyataan_satu':'pernyataan_limabelas']

    question_trap = [
        'pernyataan_dua', 
        'pernyataan_lima', 
        'pernyataan_enam', 
        'pernyataan_sembilan', 
        'pernyataan_empatbelas', 
        'pernyataan_limabelas'
    ]

    data_question = data_question.replace({'SS': 4, 'S': 3, 'TS': 2, 'STS': 1})
    data_question[question_trap] = data_question[question_trap].replace({'SS': 1, 'S': 2, 'TS': 3, 'STS': 4})

    data_question['career_planning']            = data_question['pernyataan_satu'] + data_question['pernyataan_dua']
    data_question['career_exploration']         = data_question['pernyataan_tiga'] + data_question['pernyataan_empat']
    data_question['make_career_decisions']      = data_question['pernyataan_lima'] + data_question['pernyataan_enam'] + data_question['pernyataan_tujuh']
    data_question['world_of_work_information']  = data_question['pernyataan_delapan'] + data_question['pernyataan_sembilan'] + data_question['pernyataan_sepuluh'] + data_question['pernyataan_sebelas'] + data_question['pernyataan_duabelas']
    data_question['prefered_group_work']        = data_question['pernyataan_tigabelas'] + data_question['pernyataan_empatbelas'] + data_question['pernyataan_limabelas']

    df2 = data_question.loc[:, 'career_planning':'prefered_group_work']

    scaler = StandardScaler()
    #df_scaled = scaler.fit_transform(data_question)
    df_scaled = scaler.fit_transform(df2)

    km = KMeans(n_clusters=3)
    X = df_scaled
    y_predicted = km.fit_predict(X)
    df['kematangan_karir'] = y_predicted
    data_question['kematangan_karir'] = y_predicted

    df['kematangan_karir'] = df['kematangan_karir'].map({0: 'tinggi', 1: 'sedang', 2: 'rendah'})
    return df