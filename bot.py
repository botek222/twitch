# -*- coding: UTF-8 -*-

import string,socket,random,time,random,re
from Settings import HOST, PORT, CHANNEL, PAPUGA




PASS = "oauth:au71kdpo13ar6at3kvb0f0amnu4dl3"
NICK = "botek222"

delay = 5

switch = 0

wait = 3

s = socket.socket()
s.connect((HOST, PORT))
s.send(bytes("PASS " + PASS + "\r\n", "UTF-8"))
s.send(bytes("NICK " + NICK + "\r\n", "UTF-8"))
s.send(bytes("JOIN #" + CHANNEL + " \r\n", "UTF-8"))


def wyslij(message):
	s.send(bytes("PRIVMSG #" + CHANNEL + " :" + message + "\r\n", "UTF-8"))
	print(NICK + ": " + message)


while True:
	line = str(s.recv(1024))
	if "End of /NAMES list" in line:
		print("Polaczono z " + CHANNEL)
		print("Powtarzam: " + PAPUGA)
		print("--------------------------------")
		break

while True:
	for line in str(s.recv(1024).decode("utf-8", errors="ignore")).split('\r\n'):
		parts = line.split(':')

		if "PING" in line:
			print("PING")
			s.send(bytes("PONG tmi.twitch.tv\r\n", "UTF-8"))
			break

		if len(parts) < 3:
			continue

		if "QUIT" not in parts[1] and "JOIN" not in parts[1] and "PART" not in parts[1]:
			message = parts[2][:len(parts[2])]



		usernamesplit = parts[1].split("!")
		username = usernamesplit[0]
		print(username + ": " + message)

		procenty = random.randint(30, 100)
		randomowe = random.SystemRandom()
		now = time.time()

		if message == "elo":
         	 	 wyslij("@" + username + ": " + " pajalHey " )


		if message == "witam":
         	 	 wyslij("@" + username + " " + " pajalHey " )

		if message == "czesc":
         	 	 wyslij("@" + username + " " + " pajalHey " )

		if message == "siema":
         	 	 wyslij("@" + username + " " + " pajalHey " )

		if message == "pajalHey":
         	 	 wyslij("@" + username + " " + " pajalHey " )

		if message == "hej":
         	 	 wyslij("@" + username + " " + " pajalHey " )

		if message == "hey":
         	 	wyslij("@" + username + " " + " pajalHey " )

		if message == "TriHard":
				wyslij("@" + username + " " + " cmonBruh " )

		if message == "pa":
         	 	wyslij("@" + username + " " + " pajalHey " )

	



		



