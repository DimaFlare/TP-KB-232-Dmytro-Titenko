def makeLog(a,operation,b,result):
    f = open("calcmodules/log/log.txt", "a")
    f.write("{a=" + str(a) + ";operation=" + operation + ";b=" + str(b) + ";result=" + str(result)+ "}\n")
    f.close()
    return
