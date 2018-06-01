import os

rv = os.path.ismount ('/mnt/mycloud')

print (rv)

if rv != True :

    rv = os.system('sudo mount.cifs -o guest //192.168.1.8/Public/ /mnt/mycloud')

    print (rv)
    rv = os.path.ismount ('/mnt/mycloud')

    print (rv)