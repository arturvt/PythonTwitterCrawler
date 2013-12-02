#Code by http://denis.papathanasiou.org/2012/05/07/using-microsofts-translator-api-with-python/
# Vem um XML, falta pegar o valor!
import json
import requests
import urllib
import msmt


from lxml import etree # http://lxml.de/tutorial.html VER AQUI
 
MY_CLIENT_ID = 'arturvt'
MY_CLIENT_SECRET = '1IFBkF30YGoMvp/8sVsc1qu7SY8ur3FjcxKSytCHcOo='
token = msmt.get_access_token(MY_CLIENT_ID, MY_CLIENT_SECRET)


def get_text_from_msmt_xml (xml):
    """Parse the xml string returned by the MS machine translation API, and return just the text"""
 
    text = []
    doc = etree.fromstring(xml)
    for elem in doc.xpath('/foo:string', namespaces={'foo': 'http://schemas.microsoft.com/2003/10/Serialization/'}):
        if elem.text:
            elem_text = ' '.join(elem.text.split())
            if len(elem_text) > 0:
                text.append(elem_text)
 
    return ' '.join(text)


def translateToEnglish(value):

    args = {
            'client_id': 'arturvt',#your client id here
            'client_secret': '1IFBkF30YGoMvp/8sVsc1qu7SY8ur3FjcxKSytCHcOo=',#your azure secret here
            'scope': 'http://api.microsofttranslator.com',
            'grant_type': 'client_credentials'
        }
    oauth_url = 'https://datamarket.accesscontrol.windows.net/v2/OAuth2-13'
    oauth_junk = json.loads(requests.post(oauth_url,data=urllib.urlencode(args)).content)
    translation_args = {
            'text': "Hello there",
            'to': 'pt',
            'from': 'en'
            }
    headers={'Authorization': 'Bearer '+oauth_junk['access_token']}
    translation_url = 'http://api.microsofttranslator.com/V2/Ajax.svc/Translate?'
    translation_result = requests.get(translation_url+urllib.urlencode(translation_args),headers=headers)
    return translation_result


def translate_text(text):
        xmlresponse = msmt.translate(token, text, 'en', 'pt')
        return get_text_from_msmt_xml(xmlresponse)
    
