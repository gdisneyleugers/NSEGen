# NSEGen
Generate Nmap NSE scripts that run host commands for extending Nmap.
--
Usages included simplifying PoC reproduction and automation.
--
# Usage:
```
genScript("python Test.py",
          443,
          'tcp',
          'open',
          output='GenNSE0.nse',
          text="Python Test: ")
```
# Output
--
```
portrule = function(host, port)
        return port.protocol == "tcp"
        and port.number == 443
        and port.state == "open"
end
action = function(host, port)
        local rel = os.execute("python Test.py")
        return{'Python Test: ', rel}
end
```
# Running the Script
```
{ ~ }  » python NSEGen.py                                                                       ~
Command: python Test.py
Port: 443
Proto: tcp
State: open
Output Text: Python Test
Save As: PythonTest.nse
portrule = function(host, port)
        return port.protocol == "tcp"
        and port.number == 443
        and port.state == "open"
end
action = function(host, port)
        local rel = os.execute("python Test.py")
        return{'Python Test: ', rel}
end
{ ~ }  » nmap 10.0.0.1 --script=PythonTest.nse -v -A -Pn -p 443                                 ~

Starting Nmap 7.12 ( https://nmap.org ) at 2016-12-05 01:40 Ame
NSE: Loaded 37 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 01:40
Initiating OS detection (try #1) against 10.0.0.1
NSE: Script scanning 10.0.0.1.
Initiating NSE at 01:40
------------------------------------------
|This is a python script running: Test.py|
------------------------------------------
Completed NSE at 01:40, 0.48s elapsed
Initiating NSE at 01:40
Completed NSE at 01:40, 0.00s elapsed
Nmap scan report for 10.0.0.1
Host is up (0.0041s latency).
PORT    STATE SERVICE    VERSION
443/tcp open  tcpwrapped
| PythonTest:
|   Python Test:
|_  true
```
# Scapy example
```
ubuntu@tegra-kali:~/NSEGen$ python NSEGen.py
Command: python ScapyTest.py 10.0.0.1 443
Port: 443
Proto: tcp
State: open
Output Text: Scapy Test
Save As: ScapyTest.nse
portrule = function(host, port)
        return port.protocol == "tcp"
        and port.number == 443
        and port.state == "open"
end
action = function(host, port)
        local rel = os.execute("python ScapyTest.py 10.0.0.1 443")
        return{'Scapy Test: ', rel}
end

sudo nmap 10.0.0.1 --script=ScapyTest.nse  -v -Pn -p 443 -T5
Scanning 10.0.0.1 [1 port]
Discovered open port 443/tcp on 10.0.0.1
Completed SYN Stealth Scan at 02:58, 0.11s elapsed (1 total ports)
NSE: Script scanning 10.0.0.1.
Initiating NSE at 02:58
WARNING: No route found for IPv6 destination :: (no default route?)
--------------
Testing Scapy!
--------------
.
Sent 1 packets.
Completed NSE at 02:58, 1.04s elapsed
Nmap scan report for 10.0.0.1
Host is up (0.031s latency).
PORT    STATE SERVICE
443/tcp open  https
| ScapyTest:
|   Scapy Test:
|_  true
```
