"""
 Example code demonstrating how to use Azure AI Translator
 for dictionary lookups
"""

import uuid
import json
import requests

def makereq(xibody, xiparams):
    """
      Construct a request to the Azure Translation service,
      asking for a dictionary translation and displaying the result.
    """

    ## URL we'll be requesting
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/dictionary/lookup'
    url = endpoint + path

    # Timeout for web requests, in seconds
    timeout=5

    ## Build the headers for the request.
    key = "<<REPLACE ME>>"

    # location, also known as region.
    # required if you're using a multi-service or regional (not global) resource.
    # It can be found in the Azure portal on the Keys and Endpoint page.
    location = "global"

    headers = {
                 'Ocp-Apim-Subscription-Key': key,
                 # location required if you're using a multi-service or
                 # regional (not global) resource.
                'Ocp-Apim-Subscription-Region': location,
                'Content-type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())
              }

    basep = {
              'api-version': '3.0'
            }

    # Merge the basic parameters with any that we got in the function call.
    requestp = basep | xiparams

    # Make the request
    request = requests.post(url,
                            timeout=timeout,
                            headers=headers,
                            params=requestp,
                            json=xibody)
    response = request.json()

    print(json.dumps(response,
                     sort_keys=True,
                     ensure_ascii=False,
                     indent=2,
                     separators=(',', ': ')))


def main():
    """
      Main function. Build the body, and set parameters before calling the service.
    """

    # You can pass up to ten objects in body.
    body = [
             {
               'text': 'Radioactive'
             },
             {
               'text': 'spouse'
             },
             {
               'text': 'fork'
             },
             {
               'text': 'computer'
             }
           ]

    params = {
               'from': 'en',
               'to': ['fr']
             }

    print("Issuing request")
    makereq(body, params)


# Start executing at main()
if __name__=="__main__":
    main()
