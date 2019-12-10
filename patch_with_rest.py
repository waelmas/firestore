import requests
import json

endpoint = "https://firestore.googleapis.com/v1/projects/waela-firestore/databases/(default)/documents/posts/post1?currentDocument.exists=true&updateMask.fieldPaths=nameid"

body = {
    "fields" : {
        "nameid" : {
            "stringValue" : "random testing"
        }
    }
}

data = json.dumps(body)

headers = {"Authorization": "Bearer [AUTH_TOKEN]"}
print(requests.patch(endpoint, data=data,  headers=headers).json())
