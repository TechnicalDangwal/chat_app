import socket
import sys
import os
if len(sys.argv)!=3:
	print("\033[1;33;40mUSAGE : python chat_app.py IP_ADDRESS PORT_NUMBER\033[0m")
	sys.exit()
def banner():
	print('''\033[1;36;40m
	..######..##.....##....###....########.......###....########..########.
	.##....##.##.....##...##.##......##.........##.##...##.....##.##.....##
	.##.......##.....##..##...##.....##........##...##..##.....##.##.....##
	.##.......#########.##.....##....##.......##.....##.########..########.
	.##.......##.....##.#########....##.......#########.##........##.......
	.##....##.##.....##.##.....##....##.......##.....##.##........##.......
	..######..##.....##.##.....##....##.......##.....##.##........##.......
	\033[0m 			\033[1;34;40mcreated by\033[0m\033[1;33;40m Technical Dangwal\033[0m''')
banner()
user=int(input("\033[1;32;40m1\033[0m\033[1;33;40m Server \n\033[1;32;40m2\033[0m \033[1;33;40mClient \033[0m \n\033[1;33;40mChoose :\033[0m \033[1;32;40m"))
if user==1:
	host=sys.argv[1]
	print(host)
	port=sys.argv[2]
	os.system("clear")
	banner()
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((host,int(port)))
	s.listen(5)
	conn,add=s.accept()
	print(f"\033[1;32;40m connected with {add}")
	while True:
		try:
			msg=conn.recv(1024).decode("utf-8")
			print(msg)
			s_msg=input("\033[1;33;40mENTER YOUR MESSAGE :\033[0m \033[1;32;40m")
			conn.send(s_msg.encode("utf-8"))
		except KeyboardInterrupt:
			print("\033[1;31;40m ctrl+c for stop\033[0m")
			break
		except:
			pass
else:
	host=sys.argv[1]
	port=sys.argv[2]
	os.system("clear")
	banner()
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,int(port)))
	while True:
		try:
			msg=input("\033[1;33;40mEnter Your Message : \033[0m \033[1;32;40m")
			s.send(msg.encode("utf-8"))
			a=s.recv(1024)
			print(a.decode("utf-8"))
		except KeyboardInterrupt :
			print("\033[1;31;40mctrl-c for stop \033[0m")
			break
		except:
			pass
