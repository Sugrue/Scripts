import math

def subnet_size(masklen):
    masklen = masklen % 8
    subnet_len = 8 - masklen
    return math.pow(2, subnet_len)

def checkifinsubnet(prefix, ip):
    print("checking " + prefix + " : " + ip)
    prefix, mask = prefix.split('/')
    subnetsize = int(subnet_size(int(mask)))

    prefix = prefix.split('.')
    ip = ip.split('.')

    mask_oct = int(int(mask)/8)
    for i in range(mask_oct):
        if prefix[i] != ip[i]:
            return False
    prefix_result = int(prefix[mask_oct])/subnetsize
    ip_result = int(int(ip[mask_oct])/subnetsize)
    if prefix_result == ip_result or subnetsize == 256:
        return True
    return False


print(checkifinsubnet('10.0.0.0/24', '10.0.0.1'))
print(checkifinsubnet('10.0.0.0/8', '10.0.0.1'))
print(checkifinsubnet('10.0.0.0/30', '10.0.0.1'))
print(checkifinsubnet('10.0.0.0/16', '10.0.0.50'))
print(checkifinsubnet('10.1.0.0/16', '10.0.0.50'))
print(checkifinsubnet('10.0.0.25/16', '10.0.0.50'))
print(checkifinsubnet('10.0.0.0/8', '1.0.0.1'))