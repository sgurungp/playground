"""
 Example code demonstrating how to use Azure AI Translator to translate text
 and mark profanity.
"""
from azait01 import makereq

def az_ai_translate_lookup(xiparams):
    """
      Construct a request to the Azure Translation service,
      translating from French to English and displaying the result.
    """

    lservice = 'translate'

    lbody = [
              {
                'text': '''Il t'a demandé de la vendre?
                           Oui! Putain de merde, c'était énervant. 
                            
                           Il m'a dit c'était haute joaillerie. 
                           J'ai ri, et j'ai répondu, «Merde alors, c'est precieux»
                           '''
              }
            ]

    lbase_params = {
                     'api-version': '3.0',
                     'from': 'fr',
                     'to': ['en']
                   }
    # Merge the base parameters with the ones we received
    lparams = lbase_params | xiparams

    print("Issuing translation request")
    makereq(lservice, lbody, lparams)

def main():
    """
      Main function. Build the body, and set parameters before calling the service.
    """

    # You can pass more than one object in body.

    print("Case 1: No profanity filtering")
    profanity_params = {
                         'ProfanityAction': 'NoAction'
                       }
    az_ai_translate_lookup(profanity_params)

    print("Case 2: Profanity is tagged")
    profanity_params = {
                         'ProfanityAction': 'Marked',
                         'ProfanityMarker': 'Asterisk'
                       }
    az_ai_translate_lookup(profanity_params)


# Start executing at main()
if __name__=="__main__":
    main()
