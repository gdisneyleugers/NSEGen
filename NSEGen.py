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

print genScript("python Test.py",443,'tcp','open',output='GenNSE1.nse',text="Python Test: ")
