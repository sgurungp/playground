"""
 azait01.py: Module that provides commonly used names and functions
             for use by scripts that want to use the Azure AI Translate
             service over the REST API.
"""

import uuid
import json
import requests

# Constants that should be imported by scripts
ENDPOINT = "https://api.cognitive.microsofttranslator.com"
PATH = { 'dictionary': '/dictionary/lookup',
          'translate' : '/translate'
       }

# Constants that should not be imported by scripts
TIMEOUT = 5
KEY = "<<REPLACE ME>>"
LOCATION = "global"
HEADERS = {
            'Ocp-Apim-Subscription-Key': KEY,
            'Ocp-Apim-Subscription-Region': LOCATION,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
          }
APIVER = "3.0"
PARAMS = {
           'api-version': APIVER
         }

# Functions available for import: makereq.
#
def makereq(xiservice, xibody, xiparams):
    """
      Construct a request to the named Azure service,
      supplying a request body (JSON) and service-specific parameters,
      and displaying the result.
    """

    lurl = ENDPOINT + PATH[xiservice]

    # Merge the basic parameters with any that we got in the function call.
    lparams = PARAMS | xiparams

    # Make the request
    print(f"Calling Azure service at {lurl}")

    lrequest = requests.post(lurl,
                            timeout = TIMEOUT,
                            headers = HEADERS,
                            params = lparams,
                            json = xibody)
    lresponse = lrequest.json()

    print(json.dumps(lresponse,
                     sort_keys = True,
                     ensure_ascii = False,
                     indent = 2,
                     separators = (',', ': ')))
