from http.client import NETWORK_AUTHENTICATION_REQUIRED
import ipaddress
cli1 = input("Please eneter ip or subnet address: ")
try:
    subnet1 = ipaddress.IPv4Network(cli1, strict=False)
except:
    print("blogas adresas")

cli2 = input("Please enter second ip or subnet address, to check if it enters first subnet :")
try:
    subnet2 = ipaddress.IPv4Network(cli2, strict=False)
except:
    print("blogas adresas")

atsakymas = subnet2.network_address >= subnet1.network_address and subnet2.broadcast_address <= subnet1.broadcast_address
print("atsakymas :", atsakymas)