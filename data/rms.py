import subprocess,json

# Replace 'test.py' with the actual script you want to run
script_name = "hex.py"
# Command to run the script using Python
command = f"nohup python {script_name}"
command0 = "ps -ef | grep python"


#close exist terminal
result = subprocess.run(command0, shell=True, stdout=subprocess.PIPE, text=True)

# Split the output into lines and process each line
lines = result.stdout.split('\n')
processes = []

for line in lines:
    parts = line.split()
    if len(parts) >= 8 and "hex.py" in parts[8]:
        process_info = {
            "user": parts[8],
            "pid": int(parts[1])
        }
        command1 = f"kill -9 {process_info['pid']}"
        subprocess.run(command1, shell=True, stdout=subprocess.PIPE, text=True)


# Run the script using subprocess.Popen

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, close_fds=True)
# Wait for the script to finish
#process.wait()
