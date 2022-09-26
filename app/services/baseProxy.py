from datetime import datetime
from flask import request

def proxy_entity():
    print("Endpoint:",request.endpoint)
    print("Method:", request.method)
    print("Date:", datetime.today())