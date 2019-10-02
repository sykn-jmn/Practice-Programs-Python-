import time


FPS = 1/3  # Seconds per Frame... Means 1 second per 3 Frames
currentTime = 0
timePassed = 0
pastTime = time.time()
while True:
    currentTime = time.time()
    timePassed += currentTime-pastTime
    pastTime = currentTime
    if timePassed >= FPS:
        print('1 Frame')
        timePassed = 0
