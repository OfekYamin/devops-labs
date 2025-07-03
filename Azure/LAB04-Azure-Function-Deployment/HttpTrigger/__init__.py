import logging
import azure.functions as func
import json
import datetime

"""
Azure Function HTTP Trigger

This is the code for the HTTP-triggered Azure Function.
Students should modify this to add more functionality.
"""

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP trigger function endpoint.
    
    TODO: Implement this function to:
    1. Extract query or body parameters
    2. Process the request
    3. Return an appropriate response
    
    Args:
        req: HTTP request object with headers, params, body
        
    Returns:
        HTTP response with appropriate status code and body
    """
    logging.info('Python HTTP trigger function processed a request.')

    # Get name from query parameter or request body
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            req_body = {}
        name = req_body.get('name')

    # TODO: Add more processing logic here
    
    timestamp = datetime.datetime.now().isoformat()
    
    if name:
        response_body = {
            "message": f"Hello, {name}! This HTTP triggered function executed successfully.",
            "timestamp": timestamp
        }
        return func.HttpResponse(
            json.dumps(response_body),
            mimetype="application/json",
            status_code=200
        )
    else:
        response_body = {
            "message": "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            "timestamp": timestamp
        }
        return func.HttpResponse(
            json.dumps(response_body),
            mimetype="application/json",
            status_code=200
        ) 