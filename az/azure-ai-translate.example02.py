"""
 Example code demonstrating how to use Azure AI Translator to translate text
 and mark profanity.
"""

import uuid
import json
import requests

def makereq(xibody, xiparams):
    """
      Construct a request to the Azure Translation service,
      translating from French to English and displaying the result.
    """

    ## URL we'll be requesting
    endpoint = "https://api.cognitive.microsofttranslator.com"
    path = '/translate'
    url = endpoint + path

    # Timeout for web requests, in seconds
    timeout=5

    ## Build the headers for the request.
    # Add your key and endpoint
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
              'api-version': '3.0',
              'from': 'fr',
              'to': ['en']
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

    # You can pass more than one object in body.
    body = [
             {
               'text': '''Il t'a demandé de la vendre?
                          Oui! Putain de merde, c'était énervant. 
                          
                          Il m'a dit c'était haute joaillerie. 
                          J'ai ri, et j'ai répondu, «Merde alors, c'est precieux»
                          '''
            }
           ]

    print("Case 1: No profanity filtering")
    params = {
               'ProfanityAction': 'NoAction'
             }
    makereq(body, params)

    print("Case 2: Profanity is tagged")
    params = {
               'ProfanityAction': 'Marked',
               'ProfanityMarker': 'Asterisk'
             }
    makereq(body, params)


# Start executing at main()
if __name__=="__main__":
    main()
