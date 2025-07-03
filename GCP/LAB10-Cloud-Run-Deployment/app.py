#!/usr/bin/env python3
"""
Simple Flask application to demonstrate Cloud Run deployment.
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    """Return a simple JSON response."""
    return jsonify({
        "message": "Hello from Cloud Run!",
        "service": "DevOps Python Lab",
        "environment": "GCP Cloud Run"
    })

@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    # Get port from environment variable or default to 8080
    port = int(os.environ.get('PORT', 8080))
    # Run with 0.0.0.0 to allow external connections
    app.run(host='0.0.0.0', port=port) 