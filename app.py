# Import
import streamlit as st
import requests, uuid, json
import configparser
config = configparser.ConfigParser()
config.read('config.ini') # read the configuration file

# Text on page
st.title('Translate')
text=st.text_area('Enter your text', value='My name is Tue Hellstern')
target_lang = st.selectbox('Enter target language', ('da', 'it', 'de', 'sv'))

# Setup
subscription_key = config.get('azureapi', 'subscription_key') # Get key from ini file
endpoint = 'https://api.cognitive.microsofttranslator.com'
location = 'northeurope'
path = '/translate'
constructed_url = endpoint + path

params = {
  'api-version': '3.0',
  'to': target_lang[:2]
}
constructed_url = endpoint + path


headers = {
  'Ocp-Apim-Subscription-Key': subscription_key,
  'Ocp-Apim-Subscription-Region': location,
  'Content-type': 'application/json',
  'X-ClientTraceId': str(uuid.uuid4())
}
body = [{
  'text': text
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

# Button
if st.button('Submit'):
  st.write(response[0]['translations'][0]['text'])