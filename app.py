def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from DevSecOps Pipeline!'
    }

if __name__ == "__main__":
    print("Hello from DevSecOps Pipeline!")