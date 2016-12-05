# NSEGen
Generate NMAP NSE Scripts that run host commands for automation 
--
==
genScript("python Test.py",443,'tcp','open',output='GenNSE1.nse',text="Python Test: ")

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
{ ~ }  » nmap 10.0.0.1 --script=GenNSE0.nse -v -A -Pn -p 443                                  ~ 1

Starting Nmap 7.12 ( https://nmap.org ) at 2016-12-05 01:10 Ame
NSE: Loaded 37 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 01:10
Completed NSE at 01:10, 0.00s elapsed
Initiating NSE at 01:10
Completed NSE at 01:10, 0.00s elapsed
Initiating ARP Ping Scan at 01:10
Scanning 10.0.0.1 [1 port]
Completed ARP Ping Scan at 01:10, 0.33s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 01:10
Completed Parallel DNS resolution of 1 host. at 01:10, 0.03s elapsed
Initiating SYN Stealth Scan at 01:10
Scanning 10.0.0.1 [1 port]
Discovered open port 443/tcp on 10.0.0.1
Completed SYN Stealth Scan at 01:10, 0.00s elapsed (1 total ports)
Initiating Service scan at 01:10
Scanning 1 service on 10.0.0.1
Completed Service scan at 01:10, 0.90s elapsed (1 service on 1 host)
Initiating OS detection (try #1) against 10.0.0.1
NSE: Script scanning 10.0.0.1.
Initiating NSE at 01:10
------------------------------------------
|This is a python script running: Test.py|
------------------------------------------
Completed NSE at 01:10, 0.62s elapsed
Initiating NSE at 01:10
Completed NSE at 01:10, 0.00s elapsed
Nmap scan report for 10.0.0.1
Host is up (0.0017s latency).
PORT    STATE SERVICE    VERSION
443/tcp open  tcpwrapped
| GenNSE0:
|   Python Test:
|_  true
```
