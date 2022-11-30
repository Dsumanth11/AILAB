facts=[['croaks','frogs'],['eat flies','frogs'],['frogs','green'],['chirp','canary'],['sing','canary'],['canary','yellow']]

def check(knowns,facts):
    result=[]
    for known in knowns:
        for a,b in facts:
            if (b==known) and (a,b) not in result:
                result.append((a,b))
                knowns.append(a)
                
    return result

print("Result : ",check(['green'],facts))