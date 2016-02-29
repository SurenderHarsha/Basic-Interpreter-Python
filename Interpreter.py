#INTERPRETER
import re
data={}
while True:
    print '@',
    exp=raw_input()
    if exp=="":
        continue
    if exp=="exit":
        break
    try:
        if "=" in exp:
            left,right=exp.split("=")
            #print "DEBUG:"+left+" DEBUG:"+right
            if re.search('[+-/*]',left):
                #print "DEBUG INSIDE ERROR"
                print exp[1000000]
            #print "DEBUG SAFE 1"
            if data=={}:
                data[left]=right
                continue
            for key in data:
                #print "DEBUG KEY"+key
                if key in right:

                    right=right.replace(key,data[key])
            data[left]=str(eval(right))
            #print data
            continue
        #print "SEARCH FOR DIGI"
        if re.search('[0-9]',exp[0]):
            ##print data
            for key in data:
                #print key
                if key in exp:
                    #print "INSIDE"
                    exp=exp.replace(str(key),data[key])
                    #print exp
            print eval(exp)
            continue
        else:
            #print data
            for key in data:
                if key in exp:
                    exp=exp.replace(str(key),data[key])
            print eval(exp)
    except:
        print "Invalid Syntax Enter another Expression"
