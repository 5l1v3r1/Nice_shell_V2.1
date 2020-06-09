import os,platform,time
print("be good per")
time.sleep(2) # wait 3 sec
pl= platform.system()
if (pl == 'Windows'):
    os.system('python nice_shell.py && cls ')
else:
    os.system('nohup python nice_shell.py & clear ')
