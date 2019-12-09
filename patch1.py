import requests
endpoint = "https://firestore.googleapis.com/v1/projects/[PROJECT_ID]/databases/(default)/documents/posts?updateMask.fieldPaths=post1\nameid&updateMask.fieldPaths=post1\test"


body = {
    "fields": {
        "nameid": {
            "stringValue": "5"
        },
        "test": {"stringValue": "test"}
    }
}

"""
body = {
    "fields": {
        "nameid": "test"
    }
}
"""
headers = {"Authorization": "Bearer [TOKEN]"}
#data=data,
print(requests.patch(endpoint, data=body,  headers=headers).json())
