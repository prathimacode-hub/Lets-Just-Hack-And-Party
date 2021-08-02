
import os
from dotenv import load_dotenv
from google.cloud import language_v1
from google.oauth2 import service_account
from pprint import pprint


# Instantiates a client
load_dotenv()
KEYDIR_PATH = os.getenv('KEYDIR_PATH')
if __debug__:
    pprint('-' * 100)
    pprint(f'KEYDIR_PATH: {KEYDIR_PATH}')

credentials = service_account.Credentials.from_service_account_file(filename=KEYDIR_PATH)
client = language_v1.LanguageServiceClient(credentials=credentials)

text = u"Hello, world!"
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment

if __debug__:
    pprint('-' * 100)
    pprint('Text:')
    pprint('-' * 100)
    pprint(f'{text}')
    pprint('-' * 100)
    pprint('Sentiment:')
    pprint('-' * 100)
    pprint(f'Score: {sentiment.score}')
    pprint(f'Magnitude: {sentiment.magnitude}')
