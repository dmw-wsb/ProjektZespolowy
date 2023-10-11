def lambda_handler(event, context):
    # Wydrukuj "Hello, World!" do dziennika CloudWatch
    print("Hello, World!")
    
    # Zwróć "Hello, World!" jako odpowiedź
    return {
        'statusCode': 200,
        'body': 'Hello, World!'
    }
