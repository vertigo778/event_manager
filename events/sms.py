#TWILIO_ACCOUNT_SID = ''
#TWILIO_AUTH_TOKEN = ''
TWILIO_PHONE_NUMBER = '+14153160675'
import textmagic_

from twilio.rest import Client

# Add this function to send SMS
def send_sms(phone_number, message):
    textmagic_.sendtext(message, phone_number)
    #client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    #try:
    #    client.messages.create(
    #        body=message,
    #        from_=TWILIO_PHONE_NUMBER,
    #        to=phone_number
    #    )
    #except Exception as e:
    #    print(f"Error sending SMS: {e}")


def main(): 
    send_sms(6612210015, "hello")
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 