"""
 Example code demonstrating how to use Azure AI Translator
 for dictionary lookups
"""
from azait01 import makereq


def az_ai_dictionary_lookup():
    """
      Construct a request to the Azure Translation service,
      asking for a dictionary translation and displaying the result.
    """

    lservice = 'dictionary'

    # You can pass up to ten objects in the body for a dictionary
    # service request.
    lbody = [
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

    lparams = {
                'from': 'en',
                'to': ['fr']
              }

    print("Issuing dictionary request")
    makereq(lservice, lbody, lparams)

def main():
    """
      Main function.
    """
    az_ai_dictionary_lookup()


# Start executing at main()
if __name__=="__main__":
    main()
