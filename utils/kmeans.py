from fastapi.responses import StreamingResponse
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import io
import json 

def predict(list_data: str, options: str = None):
    #Set seed
    np.random.seed(123)

    #Generate to dataframe
    df = pd.DataFrame(list_data)
    data_question = df.loc[:, 'cp_one':'pgw_three']

    question_trap = [
        'cp_two', 
        'mcd_one', 
        'mcd_two', 
        'wwi_two', 
        'pgw_two', 
        'pgw_three'
    ]

    data_question = data_question.replace({'SS': 4, 'S': 3, 'TS': 2, 'STS': 1})
    data_question[question_trap] = data_question[question_trap].replace({'SS': 1, 'S': 2, 'TS': 3, 'STS': 4})

    data_question['career_planning']            = data_question['cp_one'] + data_question['cp_two']
    data_question['career_exploration']         = data_question['ce_one'] + data_question['ce_two']
    data_question['make_career_decisions']      = data_question['mcd_one'] + data_question['mcd_two'] + data_question['mcd_three']
    data_question['world_of_work_information']  = data_question['wwi_one'] + data_question['wwi_two'] + data_question['wwi_three'] + data_question['wwi_four'] + data_question['wwi_five']
    data_question['prefered_group_work']        = data_question['pgw_one'] + data_question['pgw_two'] + data_question['pgw_three']

    df2 = data_question.loc[:, 'career_planning':'prefered_group_work']

    # Data Processing Normalization
    scaler = StandardScaler()
    #df_scaled = scaler.fit_transform(data_question)
    df_scaled = scaler.fit_transform(df2)

    # Clustering by KMeans
    km = KMeans(n_clusters=3, init = 'k-means++', random_state = 123)
    X = df_scaled
    y_predicted = km.fit_predict(X)
    df['maturity_career'] = y_predicted

    conditions = [
        (df['maturity_career'] == 0),
        (df['maturity_career'] == 1),
        (df['maturity_career'] == 2)
    ]

    choices = ['Tinggi','Rata-rata','Rendah']
    df['maturity_career'] = np.select(conditions, choices)

    if options is None :
        res = df.to_json(orient="records")
        parsed = json.loads(res)
        return parsed

    if options == 'export':
        stream = io.StringIO()
        df.to_csv(stream, index=False)
        
        response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=karir_siswa.csv"
        return response
    
    if options == 'dashboard':
        cluster_counts = df['maturity_career'].value_counts().sort_index(ascending=True)
        response = cluster_counts.to_dict()
        return response