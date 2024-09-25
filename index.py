from twilio.rest import Client
import datetime

account_sid = 'xyz'
auth_token = 'zxd'
twilio_phone_number = '99999999'
recipient_phone_number = '999999999' 
birthday_messages = [
    "🎉 Happy Birthday! 🎂🎈",
    "Wishing you a fantastic year ahead! 🌟",
    "May all your dreams come true! 🌠"
]

def send_birthday_message():
    client = Client(account_sid, auth_token)
    today = datetime.date.today()
    current_month, current_day = today.month, today.day

    
    friend_birthday_month = 9
    friend_birthday_day = 25

    if current_month == friend_birthday_month and current_day == friend_birthday_day:
        
        message = random.choice(birthday_messages)
        client.messages.create(
            body=message,
            from_=f'whatsapp:{twilio_phone_number}',
            to=f'whatsapp:{recipient_phone_number}'
        )
        print(f"Sent: {message}")
    else:
        print("No birthdays today. 😊")

if __name__ == "__main__":
    send_birthday_message()
