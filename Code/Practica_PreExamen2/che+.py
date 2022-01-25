def getOpt(textopts="",inputOptText="",rangeList=[],exceptions=[]):
    while True:
        print(textopts)
        opc = input(inputOptText)
        if opc.isdigit():
            for i in rangeList:
                if int(opc) == i:
                    return opc

        print(opc[0])
        for j in exceptions:
            if len(opc) ==1:
                if str(opc) == j:
                    return opc
            if len(opc) >= 2:
                if opc[0] == "-":
                    if str(j).isalpha() and str(j) == "-":
                        if opc[1] == j[1]:
                            print(opc[1],j[1])
                    else:
                        print("error1")
                else:
                    print("error2")

        else:
            print("error3")


opc = getOpt(textopts="1)Login\n2)Create user\n3)Show Adventures\n4)Exit",inputOptText="\nElige tu opción:",rangeList=[1,2,3,4],exceptions=["w","e",-1])
print(opc)