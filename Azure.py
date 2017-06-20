########### Python 3.2 #############
####Microsoft Azure API - Learning restaurant picture content#######
import http.client, urllib.request, urllib.parse, urllib.error, base64

import json
import pandas as pd
import numpy as np
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '141a0f1eacf3419da312393e364234fb',
}

params = urllib.parse.urlencode({
    # Request parameters
    'visualFeatures': 'Tags',
    'language': 'en',
})
df= pd.DataFrame.from_csv('Yelp Business.csv',encoding = "ISO-8859-1")
sLength=len(df['id'])
df['Tag1']=pd.Series(np.random.randn(sLength),index=df.index)
df['Confidence1']=pd.Series(np.random.randn(sLength),index=df.index)
df['Tag2']=pd.Series(np.random.randn(sLength),index=df.index)
df['Confidence2']=pd.Series(np.random.randn(sLength),index=df.index)
df['Tag3']=pd.Series(np.random.randn(sLength),index=df.index)
df['Confidence3']=pd.Series(np.random.randn(sLength),index=df.index)
df['Tag4']=pd.Series(np.random.randn(sLength),index=df.index)
df['Confidence4']=pd.Series(np.random.randn(sLength),index=df.index)
df['Tag5']=pd.Series(np.random.randn(sLength),index=df.index)
df['Confidence5']=pd.Series(np.random.randn(sLength),index=df.index)



for i in range(0,10):
    body = df['image_url'][i]
    try:
        conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        data = data.decode("utf-8")
        jsonData = json.loads(data)
        listCon = []
        listName = []
        for element in jsonData['tags']:
            listCon.append((element['confidence']))
            listName.append((element['name']))
        if len(listCon) == 4:
            listCon.append("")
            listName.append("")
        if len(listCon) == 3:
            listCon.append("")
            listCon.append("")
            listName.append("")
            listName.append("")
        if len(listCon) == 2:
            listCon.append("")
            listCon.append("")
            listCon.append("")
            listName.append("")
            listName.append("")
            listName.append("")
        if len(listCon) == 1:
            listCon.append("")
            listCon.append("")
            listCon.append("")
            listCon.append("")
            listName.append("")
            listName.append("")
            listName.append("")
            listName.append("")
        df['Tag1'][i]=listName[0]
        df['Tag2'][i]=listName[1]
        df['Tag3'][i]=listName[2]
        df['Tag4'][i]=listName[3]
        df['Tag5'][i]=listName[4]
        df['Confidence1'][i]=listCon[0]
        df['Confidence2'][i]=listCon[1]
        df['Confidence3'][i]=listCon[3]
        df['Confidence4'][i]=listCon[4]
        df['Confidence5'][i]=listCon[5]
        df.to_csv('Output YelpBusiness.csv',sep='\t', encoding='utf-8')



        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    ####################################

