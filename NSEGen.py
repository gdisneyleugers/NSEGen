def genScript(cmd,port,proto,state,output,text):
	script = "portrule = function(host, port)\n" 
	script += '\treturn port.protocol == "{0}"\n'.format(proto)
        script += "\tand port.number == {0}\n".format(port)
        script += '\tand port.state == "{0}"\n'.format(state)
	script += "end\n"
	script += "action = function(host, port)\n"
	script += '\tlocal rel = os.execute("{0}")\n'.format(cmd)
    	script += "\treturn"+"{"+"'{0}', rel".format(text)+"}\n"
   	script += "end"
	nse_out = file(output, 'w')
	nse_out.write(script)
	nse_out.close()
	return script

def ManiGen(script,output):
	scripts = []
	t = file(output,'w')
	counter = 0
	for i in script:
		scripts.append('local script{1} = require {0}\n'.format(i,counter))
		tick = counter+1
                counter=tick
	for i in scripts:
		t.write(i)
	t.close()
	return scripts

sc = ["'GenNSE.nse'","'GenNSE0.nse'", "'GenNSE1.nse'"]
print genScript("python Test.py",443,'tcp','open',output='GenNSE1.nse',text="Python Test: ")
mani = ManiGen(sc,"manifest.nse")
