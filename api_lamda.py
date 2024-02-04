import json

def lambda_handler(event, context):
    print("event:", event)
    body="hello from Lambda!"
    status_code = 200
    return {
        "statusCode": status_code,
        "body": json.dumps(body),
        "headers": {
            "content_type": "application/json"
        }
    }
