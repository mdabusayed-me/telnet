import telnetlib
import time

Host = '192.168.2.243'
password = 'cisco'
username = 'Cisco'

tn = telnetlib.Telnet(Host)
tn.read_until(b"Username: ")
tn.write(username.encode("ascii") + b"\n") 
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")

print("Successfully connected to %s" % Host)


tn.write(b"sh run\n")
time.sleep(2)

output = tn.read_very_eager()

print (type("output"))
print(output)
print("done")
