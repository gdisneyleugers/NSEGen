---
# Scapy L3 NSE
For layer 3 testing Scapy with prepouplating target ip and port. 
```
python NSEGen.py
Command: python ScapyTest.py
Port: 443
Proto: tcp
State: open
Output Text: NMAP Input Works
Save As: ScapyNSE.nse
portrule = function(host, port)
        return port.protocol == "tcp"
        and port.number == 443
        and port.state == "open"
end
action = function(host, port)
        local cmd = string.format('%s %s %s', 'python ScapyTest.py', host.ip, port.number)
        local rel = os.execute(cmd)
        return{'NMAP Input Works: ', rel}
end


~/NSEGen$ sudo nmap 10.0.0.1 --script=ScapyNSE.nse -v -Pn -p 443
sudo: unable to resolve host tegra-kali

Starting Nmap 7.30 ( https://nmap.org ) at 2016-12-05 03:47 UTC
NSE: Loaded 1 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 03:47
NSE: Script scanning 10.0.0.1.
Initiating NSE at 03:47
WARNING: No route found for IPv6 destination :: (no default route?)
---------------------
Scapy Works!
Testing: 10.0.0.1:443
---------------------
.
Sent 1 packets.
<IP  frag=0 proto=tcp dst=10.0.0.1 |<TCP  dport=https |>>
---------------------
Completed NSE at 03:47, 1.04s elapsed
Nmap scan report for 10.0.0.1
Host is up (0.022s latency).
PORT    STATE SERVICE
443/tcp open  https
| ScapyNSE:
|   NMAP Input Works:
|_  true
```
