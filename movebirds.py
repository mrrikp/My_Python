import os, os.path
import smtplib
import datetime

## Set variables
dir = "/mnt/motionvideos/"
outdir = "/mnt/mycloud/Birdbox/"
logfile  = "/home/pi/Webcam/Copylog/Copylog.log"
ljpg=[]
lavi=[]
total_items = 0
tjpg = 0
tavi = 0
terr = 0
## Open the log file

log = open(logfile,"a")
folder_date = datetime.datetime.now().strftime("%d%m%Y-%H%M")
log.write("\n" + "\n" + folder_date + " - Copy Files" + "\n")

## check NAS is mounted

rv = os.path.ismount ('/mnt/mycloud')

if rv != True :

    rv = os.system('sudo mount.cifs -o guest //192.168.1.8/Public/ /mnt/mycloud')

    if rv > 0:
        log.write('NAS drive not opened - RV = ' + str(rv) + '\n')
        log.close()
        sys.exit(90)

## set up new folders

outjpg = outdir + "Pictures/" + folder_date
try: 
    rv = os.system("sudo mkdir " + outjpg)
except:
    log.write(" Failed to create picture directory " + outjpg + "RV = " + str(rv) + "\n")
    terr +=1
    log.close()
    sys.exit(91)
outavi = outdir + "Video/" + folder_date
try:
    rv =os.system("sudo mkdir " + outavi)
except:
    log.write(" Failed to create picture directory " + outjpg + "RV = " + str(rv) + "\n")
    terr +=1
    log.close()
    sys.exit(92)
## get the items to be moved
items = os.listdir(dir)
total_items = len(items)
## are there any items to process?
if total_items > 0 :
## sort them into pictures and videos
    for file in items:
        if file.endswith(".jpg"):
            tjpg +=1
            ljpg.append(file)
        if file.endswith(".avi"):
            tavi +=1
            lavi.append(file)
## copy the Pictures files
    if tjpg > 0:
        for file in ljpg:
            bashcmd ="sudo cp " + dir + file + " " + outjpg
            rv = os.system(bashcmd)
##          if the copy worked delete the file
            if rv != 0:
##                if the copy failed leave the file and log the return code
                log.write(dir + file + " Copy RC=" + str(rv) + "\n")
                terr +=1
            else:
                bashcmd = "sudo rm "+ dir + file
                rv = os.system(bashcmd)
                if rv != 0 :
                    log.write (dir + file + "Delete RC=" + str(rv)+ "\n")
                    terr +=1
## copy the Video files
    if tavi > 0:
        for file in lavi:
            bashcmd ="sudo cp " + dir + file + " " + outavi
            rv = os.system(bashcmd)

            if rv != 0:
##                if the copy failed leave the file and log the return code
                log.write (dir + file + " Copy RC=" + str(rv) + "\n")
                terr +=1
            else:
##          if the copy worked delete the file
                bashcmd = "sudo rm "+ dir + file
                rv = os.system(bashcmd)
##              if the delete fails log the file and return code
                if rv != 0 :
                    log.write (dir + file + "Delete RC=" + str(rv) + "\n")
                    terr +=1

##    now sent the email
    date = datetime.datetime.now().strftime("%d/%m/%y-%H:%M")
    gmail_sender = 'mrrikp.pi@gmail.com'
    gmail_password = 'MyRaspb3rry'

    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
##
    server.login(gmail_sender, gmail_password)

    to_addr ='rik.pettman@gmail.com'
    mail_subject = 'Birdbox News - '+ date
    mail_text = 'Hi \n\nYou have '+ str(tjpg) + ' pictures and '+ str(tavi) + ' videos. \n\nHere is a  Pictures link file://192.168.1.8/Public/Birdbox/Pictures/' + folder_date + '/' + ' \nHere is a  Videos link file://192.168.1.8/Public/Birdbox/Video/' + folder_date + '/'
    mail_body = '\r\n'.join(['To: %s' % to_addr,
                             'From: %s' % gmail_sender,
                             'Subject: %s' % mail_subject,
                             '', mail_text])
    try:
        server.sendmail(gmail_sender, [to_addr], mail_body)
        a=1
    except:
        log.write ('error sending mail')
        terr +=1

    server.quit()
    ## now log files copied
    log.write ("Pictures processed = " + str(tjpg) + "\n")
    log.write ("Videos processed = " + str(tavi) + "\n")
    if terr != 0:
        log.write ("Total errors = " + str(Terr) + "\n")
                    
                    
else:
##    no files to process so log entry
    log.write ("No items to move" + "\n")
    
log.close()



