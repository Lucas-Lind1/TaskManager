def success_response(data=None, message="Success"):
    return {
        "statusCode": 200,
        "body": {
            "message": message,
            "data": data
        }
    }

def error_response(message="Error", status_code=400):
    return {
        "statusCode": status_code,
        "body": {
            "message": message
        }
    }