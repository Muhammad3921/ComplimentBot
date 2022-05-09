# Download the helper library from https://www.twilio.com/docs/python/install
from random import randint
from twilio.rest import Client
import time

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ="AC5abec30cd213fff77859a055f6099d8f"
auth_token = "6236ae61186a40b8eba07ef00ccc94e4"
client = Client(account_sid, auth_token)
compliments = ["I love it when u slap me."
                ,"You have the most amazing eyes I have ever seen."
                ,"Your hate for birds in the morning is so cute."
                ,"Your hair is so soft and luscious."
                ,"I wish I could see your smile right now."
                ,"When you smile it lights up the room."
                ,"I love that you make me a better person everyday."
                ,"You make life worth living, worth getting out of bed so I can see your face."
                ,"You are honestly the funniest woman on this planet, thank you fot the countless laughs"
                ,"I admire your confidence and strive to be like you."
                ,"YOU ARE SMOKING HOT DONT FORGET THAT - HUBBY"
                ,"I like the way you carry yourself, increadibly sexy."
                ,"Your mannerisms are ones I hope to achieve one day."
                ,"I love the way you treat other people, nothing is more sexier than nice Iman."
                ,"I love your red cheeks, that get all shy when you smile."
                ,"Your fashion sense is the most beautiful thing, thats why Ive decide that you will dress me my whole life. Thank you!"
                ,"I love the way you put me before yourself, even though I dont sometimes!"
                ,"You have the most amazing body in the world, even though you might not see it I AM INCREDIBLY IN LOVE." 
                ,"I love the way you look out for me all the time even though I get mad at you, i still appreciate it."
                ,"You carry yourself with such confidence, SEXY CONFIDENT IMAN."
                ,"You are a natural born leader, it is literally in your name. I love how you always take initative."
                ,"One day I know you are going to make the most beautiful mother to our children. I could have asked for nothing more of god."
                ,"Even though you piss me off, I love it when you piss me off and I love our dynamic."
                ,"Thank you being patient with me, I know im difficult (VERY)."
                ,"I love your lips, and would like to kiss your right now."
                ,"I love how I can lean on your for any situation and you will not hesitate to help me."
                ,"You always listen to what I have to say and never complain."
                ,"YOU SMELL INCREDIBLE, I love your sent and it marks you."
                ,"I love it when you zone out and I just get so stare at you."
                ,"Always looking for opportunities to learn and better yourself, I admire that about you." 
                ,"I love your gifs especially the poster, made my whole world."
                ,"I have so much fun with you and would love to spend every single minute of my life with you."
                ,"You push me to become a better person, everyday. I am only in this position because of you my heart."
                ,"I love it when you get mad you look so cute."
                ,"I LOVE YOU WIHT MY WHOLE WHOLE HEART, YOU MAKE MY LIFE COMPLETE!"]
num = 0
def createmessage():

    time.sleep(86000)
    
    ms = compliments[num]

    message = client.messages \
                    .create(
                        body=ms,
                        from_='+19853317404',
                        to='+16476319543'
                    )

    print(message.sid)
    num = num + 1