"""
 Example code demonstrating how to use Azure AI Translator to translate text.
 Modified from the sample offered by the Azure portal to pass pylint
 checking and to use a multiline string as the sample text to translate.
"""

import uuid
import json
import requests

# Add your key and endpoint
KEY = "<<REPLACE ME>>"
ENDPOINT = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource.
# It can be found in the Azure portal on the Keys and Endpoint page.
LOCATION = "global"

PATH = '/translate'
CONSTRUCTED_URL = ENDPOINT + PATH

params = {
    'api-version': '3.0',
    'from': 'it',
    'to': ['en']
}

headers = {
    'Ocp-Apim-Subscription-Key': KEY,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': LOCATION,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
# The samples here are from Dante and Ferrante: the first few lines of Canto 1 of Inferno
# and of My Beautiful Friend.
#
body = [
         {
           'text': '''Nel mezzo del cammin di nostra vita
                      mi ritrovai per una selva oscura,
                      ché la diritta via era smarrita.
                      
                      Ahi quanto a dir qual era è cosa dura
                      esta selva selvaggia e aspra e forte
                      che nel pensier rinova la paura!
                      
                      Tant\'è amara che poco è più morte;
                      ma per trattar del ben ch\'i\'vi trovai,
                      dirò de l'altre cose ch\'i\' v\'ho scorte.
                      '''
        },
        {
          'text': '''Stamattina mi ha telefonato Rino, ho creduto che volesse ancora soldi
                     e mi sono preparata a negarglieli. Invece il motivo della telefonata era
                     un altro: sua madre non si trovara più.
                  '''
        }
      ]

# Timeout for web requests, in seconds
TIMEOUT=5

request = requests.post(CONSTRUCTED_URL, params=params, headers=headers, json=body, timeout=TIMEOUT)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=2, separators=(',', ': ')))
