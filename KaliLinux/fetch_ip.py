import subprocess
command= f"nmap -sn 192.69.1.0/24 | grep 'Nmap scan report for' | cut -d ' ' -f 5"
result= subprocess.run(command,shell=Ture, stdout=subprocess.PIPE, text=True)
response=result.stdout.strip().split('\n')
print(response)
for ip_range in response:
    print(ip_range.split(".")[0].replace('-','.'))
    print('\n')
