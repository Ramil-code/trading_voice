import time
import boto3
import requests

def get_crypto_quote():
    try:
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
        response.raise_for_status()
        price = response.json()['bitcoin']['usd']
        return f"The current price of Bitcoin is {price} dollars."
    except requests.RequestException as e:
        print(f"Error fetching crypto quote: {e}")
        return "Error fetching crypto quote."

def synthesize_speech(text, filename):
    polly_client = boto3.client('polly', region_name='us-east-1')
    try:
        print(f"Synthesizing speech for: {text}")
        response = polly_client.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            VoiceId='Joanna'
        )
        with open(filename, 'wb') as file:
            file.write(response['AudioStream'].read())
        print(f'Updated file: {filename}')
    except Exception as e:
        print(f"Error synthesizing speech: {e}")


def update_crypto_quote_mp3():
    while True:
        quote = get_crypto_quote()
        synthesize_speech(quote, '/home/ubuntu/crypto_quote.mp3')
        time.sleep(31)

if __name__ == "__main__":
    update_crypto_quote_mp3()