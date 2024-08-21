"""
 Example code demonstrating how to use Azure AI Translator to translate text.
 Modified from the sample offered by the Azure portal to pass pylint
 checking and to use a multiline string as the sample text to translate.
"""
from azait01 import makereq

def az_ai_translate_lookup():
    """
      Construct a request to the Azure Translation service,
      translating from Italian to English and displaying the result.
    """

    lservice = 'translate'

    # You can pass more than one object in body.
    lbody = [
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

    lparams = {
                'from': 'it',
                'to': ['en']
              }

    print("Issuing translation request")
    makereq(lservice, lbody, lparams)

def main():
    """
      Main function.
    """
    az_ai_translate_lookup()


# Start executing at main()
if __name__=="__main__":
    main()
