from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import FormRecognizerClient
import os
import sys
import logging


# Create a logger for the 'azure' SDK
logger = logging.getLogger('azure')
logger.setLevel(logging.DEBUG)

# Configure a console output
handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(handler)

def analyze_form(endpoint, key, local_path):
    form_recognizer_client = FormRecognizerClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
        logging_enable=True )
    with open(local_path, "rb") as f:
        poller = form_recognizer_client.begin_recognize_receipts(receipt=f)
        poller.wait()

if __name__ == '__main__':
    local_path = os.getenv('FR_LOCAL_PATH')
    key = os.getenv('FR_KEY')
    endpoint = os.getenv("FR_ENDPOINT")
    analyze_form(endpoint, key, local_path)
