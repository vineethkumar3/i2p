import subprocess

def ip_address():
    command= f"nmap -sn 192.69.1.0/24 | grep 'Nap scan report for' I cut -d ' ' -f 5"
    result= subprocess.run(command,shell=True,stdout=subprocess.PIPE, text=True)
    response=result.stdout.strip().split('\n')
    ip_list=[]
    for ip_range in response:
        ip_list.append(ip_range.split(".")[0].replace('-','.'))
    print(ip_range)
    return ip_range
