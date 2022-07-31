from fastapi.responses import StreamingResponse
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import io
import json 

def predict(list_data: list, current_user: str, student_id: str = None, options: str = None):
    #Generate to dataframe
    df = pd.DataFrame(list_data)
    data_question = df.loc[:, 'cp_one':'pgw_three']

    question_trap = ['cp_two', 'mcd_one', 'mcd_two', 'wwi_two', 'pgw_two', 'pgw_three']

    data_question = data_question.replace({'SS': 4, 'S': 3, 'TS': 2, 'STS': 1})
    data_question[question_trap] = data_question[question_trap].replace({'SS': 1, 'S': 2, 'TS': 3, 'STS': 4})

    data_question['career_planning']            = data_question['cp_one'] + data_question['cp_two']
    data_question['career_exploration']         = data_question['ce_one'] + data_question['ce_two']
    data_question['make_career_decisions']      = data_question['mcd_one'] + data_question['mcd_two'] + data_question['mcd_three']
    data_question['world_of_work_information']  = data_question['wwi_one'] + data_question['wwi_two'] 
    + data_question['wwi_three'] + data_question['wwi_four'] + data_question['wwi_five']
    data_question['prefered_group_work']        = data_question['pgw_one'] + data_question['pgw_two'] + data_question['pgw_three']

    df2 = data_question.loc[:, 'career_planning':'prefered_group_work']

    # Data Processing Normalization
    scaler = StandardScaler()
    #df_scaled = scaler.fit_transform(data_question)
    df_scaled = scaler.fit_transform(df2)

    # Clustering by KMeans
    km = KMeans(n_clusters=3, random_state = 42)
    X = df_scaled
    y_predicted = km.fit_predict(X)
    df['maturity_career'] = y_predicted

    conditions = [
        (df['maturity_career'] == 0),
        (df['maturity_career'] == 1),
        (df['maturity_career'] == 2)
    ]

    choices = ['Tinggi','Rata-rata', 'Rendah']
    df['maturity_career'] = np.select(conditions, choices)
    
    if current_user['school_name']:
        df = df[df.school_id == current_user['id']]    

    if options is None :
        res = df.to_json(orient="records")
        parsed = json.loads(res)
        return parsed

    if student_id :
        new_df = pd.concat([df, df2], axis=1, join='inner')
        new_df['career_planning'] = new_df['career_planning'] / 8 * 100
        new_df['career_exploration'] = new_df['career_exploration'] / 8 * 100
        new_df['make_career_decisions'] = new_df['make_career_decisions'] / 12 * 100 
        new_df['world_of_work_information'] = new_df['world_of_work_information'] / 20 * 100
        new_df['prefered_group_work'] = new_df['prefered_group_work'] / 12 * 100
        new_df['average'] = (new_df['career_planning'] + new_df['career_exploration'] + new_df['make_career_decisions'] + new_df['world_of_work_information'] + new_df['prefered_group_work']) / 5
        new_df = new_df[new_df._id == student_id]
        res = new_df.to_json(orient="records")
        parsed = json.loads(res)
        return parsed

    if options == 'export':
        stream = io.StringIO()
        new_columns = [
            'NIS', 
            'Nama', 
            'Kelas', 
            'JK', 
            'Jurusan',
            #'Tanggal'
            'Saya sudah membuat keputusan untuk melanjutkan kuliah atau bekerja sesuai jurusan yang saya tempuh setelah lulus sekolah',
            'Saya kesulitan dalam menentukan karir yang sesuai dengan jurusan yang saya tempuh setelah lulus sekolah',
            'Saya mengumpulkan informasi terkait karier yang sesuai dengan saya melalui berbagai macam media (koran, sosmed, internet)',
            'Saya berkonsultasi dengan guru BK mengenai karir yang akan saya jalani',
            'Saya masih ragu dalam menentukan karier yang sesuai bagi saya',
            'Saya menentukan karier berdasarkan pekerjaan yang populer pada saat ini',
            'Saya memutuskan karier saya tanpa mempedulikan orang lain karena saya lebih tau diri saya sendiri',
            'Saya mengetahui persyaratan yang harus dipenuhi untuk masuk dunia kerja',
            'Saya merasa ragu bahwa kemampuan saya cukup untuk memasuki dunia kerja',
            'Saya memahami resiko-resiko yang ada dunia kerja',
            'Saya memiliki gambaran terkait dunia kerja melalui program magang atau praktek kerja lapangan',
            'Saya mengetahui gambaran tentang dunia kerja dari sosial media yang dibagikan oleh orang lain',
            'Saya memilih karier yang sesuai dengan minat dan kemampuan yang saya miliki',
            'Saya siap bekerja tidak sesuai dengan minat dan jurusan yang saya tempuh',
            'Saya siap bekerja dimana saja asalkan gaji tinggi',
            'Kematangan Karier'
        ]
        new_df = df.iloc[:,:23].copy()
        #print(new_df)
        new_df.drop(["_id", 'school_id'], axis=1, inplace=True)
        new_df.columns = new_columns
        new_df.to_csv(stream)
        
        response = StreamingResponse(iter([stream.getvalue()]), media_type="text/csv")
        response.headers["Content-Disposition"] = "attachment; filename=karir_siswa.csv"
        return response
    
    if options == 'dashboard':
        cluster_counts = df['maturity_career'].value_counts().sort_index(ascending=True)
        response = cluster_counts.to_dict()
        return response

""" def evaluation_sse(list_data: list):
    X = predict(list_data)
    sse = []
    for i in range(1, 11):
        kmeans = KMeans(n_clusters = i, random_state = 42)
        kmeans.fit_predict(X)
        sse_ = kmeans.inertia_
        sse.append(sse_)

    return sse """