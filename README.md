# streamlit demo
This a small demo of Azure Translate API and streamlit. It is a slightly modified version af the Microsoft example - [**Quickstart: Get started with Translator**](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/quickstart-translator?tabs=python)


## Code - modified version
- config.ini file usede
- drop down with the different languages

```python
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
```

## Azure
Use your Kea email credential as the Azure subscription.

## config.ini
You need to create a **config.ini** file and place it in the samen folder as the **app.py** file.

The key form Azure is placed in this file.

## .gitignore
You need to include the **config.ini** file in the **.gitignore** file.

**Remember that the config.ini file has your Subscription Key in clear text.**

        # Ini file
        config.ini

## Windows
In windows you can run the app.py with this command

        py -m streamlit run app.py

## Mac


## Links
- [Translator documentation](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/)
- [Microsoft Text Translation](https://www.microsoft.com/en-us/translator/business/translator-api/)
