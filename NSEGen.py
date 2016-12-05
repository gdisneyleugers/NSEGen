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
if __name__ == "__main__":
	cmd = raw_input("Command: ")
	port = input("Port: ")
	proto = raw_input("Proto: ")
	state = raw_input("State: ")
	text = raw_input("Output Text: ")
	output = raw_input("Save As: ")
	print genScript(cmd,port,proto,state,output,text)
