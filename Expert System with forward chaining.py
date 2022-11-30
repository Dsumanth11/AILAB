facts=[['croaks','frogs'],['eats flies','frogs'],['frogs','green'],
       ['chirp','canary'],['sing','canary'],['canary','yellow']]
def check(knowns,facts):
    R=[]
    for known in knowns:
        for A,B in facts:
            if known==A and (A,B) not in R:
                R.append((A,B))
                knowns.append(B)
    return R
print("Result:",check(['croaks','eats flies'],facts))

facts=[['croaks','frogs'],['eat flies','frogs'],['frogs','green'],
       ['chirp','canary'],['sing','canary'],['canary','yellow']]
