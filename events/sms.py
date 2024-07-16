
TWILIO_PHONE_NUMBER = '+18777639132'
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

def send_sms2(phone_number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
    except Exception as e:
        print(f"Error sending SMS: {e}")

def main(): 
    send_sms2(6612210015, "hello")


  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 