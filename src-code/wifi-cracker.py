import subprocess

checking = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8',
                                                                                 errors="backslashreplace").split('\n')
checking = [i.split(":")[1][1:-1] for i in checking if "All User Profile" in i]

#print([data.encode('utf-8') for data in checking])
for i in checking:
    #i = i.decode('utf-8',errors="backslashreplace")
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile',
                                       i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
    results = [pwd.split(":")[1][1:-1] for pwd in results if "Key Content" in pwd]

    try:
        print("{:<30}|  {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30}|  {:<}".format(i, ""))
