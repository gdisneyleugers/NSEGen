# NSEGen
Generate NMAP NSE Scripts that run host commands for automation 
--
==
genScript("python Test.py",443,'tcp','open',output='GenNSE1.nse',text="Python Test: ")

# Output
==
- portrule = function(host, port)
-        return port.protocol == "tcp"
-        and port.number == 443
-        and port.state == "open"
- end
- action = function(host, port)
-        local rel = os.execute("python Test.py")
-        return{'Python Test: ', rel}
- end
==
