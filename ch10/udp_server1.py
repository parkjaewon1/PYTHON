from socket import *
svrsock = socket(AF_INET, SOCK_DGRAM) # ipv4, udp방식
svrsock.bind(('172.30.1.44', 7003)) # 원격 127.0.0.1
while True:
    print("서버 대기중....")
    s, addr = svrsock.recvfrom(1024)
    print(f"client ip : {addr}, 메세지 : {s.decode()}")
    svrsock.sendto(s, addr)