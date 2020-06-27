#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from datetime import datetime
import os
from google.cloud import firestore
import sys
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = # TO DO: replace with the path to the service account key, or simply remove if you are using default account


now = datetime.now()
new = str(now).split('.')
datetime = new[0]
file_name = datetime.replace(':','_').replace('-','_').replace(' ','_').replace('2020','export')

export_file = file_name + ".txt"

db = firestore.Client()
coll_ref = db.collection(u'collection101')







def export_to_txt(export_file):
    with open(export_file, "w", encoding="utf-8") as f:
        f.write("Below are all Firestore Documents under collection101 \n\n\n")
        docs = coll_ref.stream()
        for doc in docs:
            document_id = str(doc.id)
            title1 = str(doc.to_dict()['title'])
            body1 = str(doc.to_dict()['body'])

            try:
                media_link = str(doc.to_dict())['media_link']
            except:
                media_link = str(doc.to_dict()['link'])
 
            all_options=options1
                


            
            all1 = 'Document_ID: ' + document_id + '\n\n' + 'Title: \n' + title1 +  '\n\n' + 'Text: \n' + body1 + '\n \n \n \n'

            f.write(all1)

    return 'done'


export_to_txt(export_file)
print(export_file)






