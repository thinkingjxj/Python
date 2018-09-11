# 创建socket对象
# 绑定IP和port，  bind()方法
# 传输数据
    # 接收 socket.recvfrom(bufsize[,flag]),获得(string, address)
    # 发送 socket.sendto(string, address)
# 释放

import socket

s = socket.socket(type=socket.SOCK_DGRAM)
addr = ('127.0.0.1', 8080)
s.bind(addr)

data, clientaddr = s.recvfrom(1024)
print(clientaddr)
msg = 'hello {}'.format(data.decode())

s.sendto(msg)
s.close()

