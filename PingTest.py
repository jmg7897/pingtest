#!/usr/bin/env python
import os
import subprocess
def main():
    print("*** Beginning Test ***\n\t\t5\n\t\t4\n\t\t3\n\t\t2\n\t\t1\n")
    netOut=subprocess.check_output(["ip", "route", "show"]).split()
    defGate=netOut[2].decode()
    print("Your default gateway is ", defGate)
    defTest=os.system("ping -c 1 "+defGate+" >/dev/null 2>&1")
    if defTest!=0:
        print("Connection to the default gateway is UNSUCCESSFULL!")
    else:
        print("Connection to the default gateway is SUCCESSFULL!")
    remote="8.8.8.8"
    remoteTest=os.system("ping -c 1 "+remote+" >/dev/null 2>&1")
    if remoteTest!=0:
        print("Remote connection UNSUCCESSFULL!")
    else:
        print("Remote connection SUCCESSFULL!")
    dnsTest=os.system("ping -c 1 google.com >/dev/null 2>&1")
    if dnsTest!=0:
        print("DNS resolution UNSUCCESSFULL!")
    else:
        print("DNS resolution SUCCESSFULL!")
    print("*** Test Complete ***")

main()