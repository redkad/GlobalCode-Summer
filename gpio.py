from gpiozero import Button
button = Button(2)
import requests

button.when_pressed = requests.post("https://maker.ifttt.com/trigger/glblcd/with/key/mGh-lQN4x9c62thYIg_mkh0Z27glI7okoIl6ilVcWat")
print(r.status_code)

pause()
 