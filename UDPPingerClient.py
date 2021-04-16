import time
from socket import *

#server는 local주소
serverIP = '127.0.0.1'
#UDPPingerServer에서 socket에 할당한 port값
serverPort = 12000
#Client socket을 Server의 socket과 같은 방식으로 만들어준다.
clientSocket = socket(AF_INET, SOCK_DGRAM)
#문제에서 reply를 1초 기다린다고 했기에 timeout은 1초로 설정
clientSocket.settimeout(1)

#문제에서 client는 10pings를 server로 보낸다고 했으므로 10번 반복
for i in range(0, 10):
    #보내기 시작하는 시간을 저장
    SendingTime = time.time()
    #message를 생성을 하고, sned를 위해 encode함
    message = ('Ping sequence_number %d %s' % (i + 1, SendingTime)).encode()
    try:
        #Server로 message를 전송
        clientSocket.sendto(message, (serverIP, serverPort))
        #Server에서의 respone과 주소를 받았습니다.
        response, serverAddress = clientSocket.recvfrom(1024)
        #RTT를 구하기 위해 현재 시간에서 보낼 때의 시간을 뺴줌
        RTT = time.time() - SendingTime

        print('Sequence_number %d: Respone from %s RTT = %.4fs' % (i + 1, serverIP, RTT))
	except Exception as e:
        print('Sequence_number %d: Request Timed Out' % (i + 1))

#Socket을 닫았습니다.
clientSocket.close()