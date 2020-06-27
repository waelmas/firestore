#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from datetime import datetime
import os
from google.cloud import firestore
import sys
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/AeonGen AKA Innaton Technologies/COVID-bot/backend/scraping.json"
# export GOOGLE_APPLICATION_CREDENTIALS='D:\AeonGen AKA Innaton Technologies\COVID-bot\backend\scraping.json'


now = datetime.now()
new = str(now).split('.')
datetime = new[0]
file_name = datetime.replace(':','_').replace('-','_').replace(' ','_').replace('2020','export')

export_file = file_name + ".txt"

db = firestore.Client()
coll_ref = db.collection(u'topics')







def export_to_txt(export_file):
    with open(export_file, "w", encoding="utf-8") as f:
        f.write("Below are all Firestore Documents under topics collection \n\n\n")
        docs = coll_ref.stream()
        for doc in docs:
            document_id = str(doc.id)
            title1 = str(doc.to_dict()['title'])
            body1 = str(doc.to_dict()['body'])
            link1 = str(doc.to_dict()['link'])
            iframe1 = str(doc.to_dict()['iframe'])
            options1 = str(doc.to_dict()['options'])
            show_options1 = str(doc.to_dict()['show_options'])
            show_media = str(doc.to_dict()['show_media'])
            try:
                media_link = str(doc.to_dict())['media_link']
            except:
                media_link = str(doc.to_dict()['link'])
            #all_options=options1.replace('[','').replace(']','').replace("'","").split(',')
            #all_options=json.dumps(options1)
            all_options=options1
                


            if show_options1 == 'True':
                show_options_flag='show options'
            else:
                show_options_flag='dont_show options'
            if show_media == 'True':
                media_flag = 'show media'
            else:
                media_flag='dont_show media'
            
            all1 = 'Document_ID: ' + document_id + '\n\n' + 'Title: \n' + title1 +  '\n\n' + 'Text: \n' + body1 +  '\n\n' + 'Link: \n' + link1 + '\n\n' + show_options_flag + '\n\n' + media_flag + '\n\n' + media_link + '\n\n' + 'Suggestions: \n' + all_options + '\n \n \n \n'

            f.write(all1)

    return 'done'


export_to_txt(export_file)
print(export_file)






