import pikepdf
import time

pdf_file = input("PDF Fayl: ")
password_list = input("Parollar Listi: ")
passwords = open(password_list)

i = 0
start_time = time.time()
for password in passwords:
	password = password.strip("\n")

	i += 1
	print("\r {} ta Parollar Sinab Ko'rildi ".format(i), end="")
	try:
		pikepdf.open(pdf_file, password=password)

		print("\n" + "* " * 20)

		end_time =  time.time()
		print("PAROL: {} ".format(password))
		print("[{}] ta Parollar {} Sekundda Tekshirildi! ".format(i, str(end_time - start_time)[:4]))

		print("\n" + "* " * 20)

		passwords.close()
		break
	except:
		pass
		
input("")
input("")
