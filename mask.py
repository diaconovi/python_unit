def cidrConvertion(mask):
    maskList = mask.split('.')
    binMask = ''
    for oct in maskList:
        binNumber = bin(int(oct))
        binNumber = binNumber[2:]
        binMask = binMask + binNumber
        if len(binNumber) > 8:
            return -1

    binMask = binMask.replace('0','')
    cidr = len(binMask)
    return int(cidr)

def quickUnittest():
    assert cidrConvertion('255.255.255.0') == 24, "should be 24"
    assert cidrConvertion('255.255.256.0') == -1, "should be not exceed 255"
    #assert cidrConvertion('255.255.129.0') == -1, "should a valid octet"

quickUnittest()

print(cidrConvertion('255.255.255.0'))
