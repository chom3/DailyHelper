import smtplib, ssl
from project.config import *
from project.Weather.DailyWeather import *
from project.GoogleSheets.WorkoutBlock import *

def sendText(message):
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, str(message).encode('ascii', 'ignore').decode('ascii'))
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

def main():
    weather = getWeather(weather_api_token)
    dailyWorkout = getDailyWorkout()
    messages = [getWeather(weather_api_token), dailyWorkout]

    for message in messages:
        sendText(message)
    
if __name__ == "__main__":
    main()