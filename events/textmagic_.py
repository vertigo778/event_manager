
from textmagic.rest import TextmagicRestClient
username = "spxsignals"
token = "xWMQ2KW63O0UuA6JWLbdG32ZoffqBn"
client = TextmagicRestClient(username, token)
#message = client.messages.create(phones="+16612210015", text="Hello TextMagic")

TURN_OFF = True

def sendtext(content, number):

    message = client.messages.create(phones=("+1" + number), text=content)

        
def main():
    sendtext("test", "6612210015")

if __name__=="__main__":
    main()
    
