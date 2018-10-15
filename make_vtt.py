import datetime

def make_vtt(video_width=1920, video_height=1080, duration=120, grid=4, position=5, basefile="thumb-sprites.jpg"):
    #given width and height of video, duration, filename and position

    dar = video_width / video_height

    w = 160
    h = int(w // dar)  #calculate height 90 in this case
    x = 0
    y = 0
    imagenum = 1

    # setup 00:00
    t = datetime.datetime(2018,1,1,0,0,0)
    # get duration in HH:MM format
    d = t + datetime.timedelta(0,duration)
    # header
    vtt = ["WEBVTT",""]

    # vtt = open('thumb-sprites.vtt', 'w')
    while t < d:
        # map the coordinates to it in X,Y,W,H format
        xywh = "{},{},{},{}".format(x,y,w,h)
        # get timestamps
        start = t.strftime("%H:%M:%S")
        end = (t + datetime.timedelta(0,position)).strftime("%H:%M:%S")
        
        # append things we care about to vtt
        vtt.append("{} --> {}".format(start,end)) #00:00.000 --> 00:05.000
        vtt.append("{}#xywh={}".format(basefile,xywh))
        vtt.append("") #Linebreak

        # increment timestamp by position
        t = t + datetime.timedelta(0,position)
        # increment x
        if imagenum % grid == 0:
            x = 0
        else:
            x += w
        # increment y
        if imagenum % grid == 0:
            y += h
        # increment imagenum
        imagenum += 1 

    vtt =  "\n".join(vtt)
    #output to file
    with open('thumb-sprites.vtt', 'w') as f:
        f.write(vtt)
        f.close()
    print("Wrote vtt file")

make_sprite()