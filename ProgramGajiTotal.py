#!/usr/bin/env python3


# ---PROGRAM GAJI TOTAL---


# Dibuat Oleh: Ruben Leonardo Sigalingging.
# Dibuat Pada: Jumat, 17 Juni, 2022, Pukul 03:40 AM.
# Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10
# ---SOAL INFORMATIKA LKS---


# ---MENULIS PROGRAM GAJI TOTAL MENGGUNAKAN PYTHON 3.8.10---
def program_gaji_total(created_by="Ruben Leonardo Sigalingging."):
	from os import system
	system("clear")
	system("chmod 777 ProgramGajiTotal.py")
	from pyfiglet import figlet_format
	from time import time, sleep
	from sys import exit


	# Buat judul program, menggunakan pyfiglet
	judul = figlet_format("GajiTotal",font="slant")
	print(judul)
	print("\033[91m[\033[94m!\033[91m] \033[94mDibuat Oleh: \033[91mRuben Leonardo Sigalingging.")
	print("\033[91m[\033[94m!\033[91m] \033[94mDibuat Pada: \033[91mJumat, 17 Juni, 2022, Pukul 03:40 AM.")
	print("\033[91m[\033[94m!\033[91m] \033[94mMenggunakan: \033[91mBahasa Pemrogramman Python Versi 3.8.10")
	print("\033[91m[\033[94m!\033[91m] \033[94m---\033[91mSOAL INFORMATIKA LKS\033[94m---")
	print("\n")


	nama_anda = input("\033[91m[\033[94m!\033[91m] \033[94mNama Anda: \033[91m")
	alamat_anda = input("\033[91m[\033[94m!\033[91m] \033[94mAlamat Anda: \033[91m")
	golongan = input("\033[91m[\033[94m!\033[91m] \033[94mGolongan (A / B)\n\033[91m(A) Belum Menikah \033[94m(B) Sudah Menikah\n\033[91m[\033[94m!\033[91m] \033[94mPilih: \033[91m")
	if golongan == "A" or golongan == "a":
		print(f"\033[91m[\033[94m!\033[91m] \033[94mNama Anda \033[91m{nama_anda}")
		print(f"\033[91m[\033[94m!\033[91m] \033[94mAlamat Anda \033[91m{alamat_anda}")
		print("\033[91m[\033[94m!\033[91m] \033[94mStatus Anda Saat Ini \033[91mBelum Menikah.")
		print("\033[91m[\033[94m!\033[91m] \033[94mGaji Pokok Anda \033[91mRp. 1.500.000")
		print("\033[91m[\033[94m!\033[91m] \033[94mMohon Maaf, Anda Tidak Bisa \033[91mMendapatkan Tunjangan!")
		print("\033[91m[\033[94m!\033[91m] \033[94mTotal Gaji Bersih Anda: \033[91mRp. 1.500.000")
		exit()


	elif golongan == "B" or golongan == "b":
		print(f"\033[91m[\033[94m!\033[91m] \033[94mNama Anda \033[91m{nama_anda}")
		print(f"\033[91m[\033[94m!\033[91m] \033[94mAlamat Anda \033[91m{alamat_anda}")
		print("\033[91m[\033[94m!\033[91m] \033[94mStatus Anda Saat Ini \033[91mSudah Menikah!")
		print("\033[91m[\033[94m!\033[91m] \033[94mGaji Pokok Anda \033[91mRp. 1.000.000")
		print("\033[91m[\033[94m!\033[91m] \033[94mAnda Mendapatkan \033[91mTunjangan Sebesar 5%")
		gaji_sudah_menikah = (5/100)*1000000+1000000
		print(f"\033[91m[\033[94m!\033[91m] \033[94mTotal Gaji Bersih Anda: \033[91m{gaji_sudah_menikah}")
		exit()


	else:
		print("\033[91m[\033[94m!\033[91m] \033[94mPilih Dengan Benar!")
		program_gaji_total()
program_gaji_total()