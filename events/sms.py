#TWILIO_ACCOUNT_SID = 'AC48b5aa48c277f916a5d621be8cca271f'
#TWILIO_AUTH_TOKEN = 'ad5cdaf8caa92fdfc59bd86c5d2e3b82'
TWILIO_PHONE_NUMBER = '+14153160675'

from twilio.rest import Client

# Add this function to send SMS
def send_sms(phone_number, message):
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
    send_sms(6612210015, "hello")
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 