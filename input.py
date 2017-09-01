def readVal(valType, requestMsg, errorMsg):
    """generic input check"""
    while True:
        val = input(requestMsg)
        try:
            val = valType(val)
            return val
        except:
            print(errorMsg)
