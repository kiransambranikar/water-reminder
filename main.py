import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="**It's Time to Drink Water!!",
            message ="The National Academics of Sciences,Engineering, and Medicine Determined that an adequate daily fluid intake is : About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            # app_icon ="C:\Users\hp\Desktop\water reminder\icon.ico",
            timeout = 12
        ) 
        # time.sleep(6)
        time.sleep(60*60)