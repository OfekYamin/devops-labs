"""
GCP LAB04 - Cloud Function Sample
This is a simple HTTP-triggered cloud function that returns a greeting message.
"""

import json
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def hello_world(request):
    """
    HTTP Cloud Function that returns a greeting message.
    
    Args:
        request (flask.Request): The request object.
        https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data
        
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response
    """
    # Log the request
    request_json = request.get_json(silent=True)
    request_args = request.args
    
    # Get name from request or use default
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    
    # Get current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Log the invocation
    logging.info(f"Function executed at {current_time} with name={name}")
    
    # Return response
    return json.dumps({
        'message': f'Hello {name}!',
        'timestamp': current_time
    }) 