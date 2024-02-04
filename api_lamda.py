import json

def lambda_handler(event, context):
    body="hello from Lambda!"
    status_code = 200
    return {
        "statuscode": status_code,
        "body": json.dumps(body),
        "headers": {
            "content_type": "application/json"
        }
    }