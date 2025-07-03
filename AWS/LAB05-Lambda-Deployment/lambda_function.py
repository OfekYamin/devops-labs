"""
Lambda function for AWS LAB05

This file contains a simple AWS Lambda function handler that returns a successful response.
This is the function that will be deployed to AWS Lambda.
"""

def lambda_handler(event, context):
    """
    Simple Lambda function handler.
    
    Parameters:
    - event: The event data passed to the Lambda function
    - context: Runtime information provided by AWS Lambda
    
    Returns:
    - A dictionary containing the response with status code and body message
    """
    # TODO: Add your Lambda function logic here
    # This is a simple example that returns a success message
    # You can modify this to process the event data, interact with other AWS services, etc.
    
    # Print some information for CloudWatch logs
    print("Lambda function invoked!")
    print(f"Event: {event}")
    
    # Return a successful response
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda! This function was deployed using Python and boto3.'
    } 