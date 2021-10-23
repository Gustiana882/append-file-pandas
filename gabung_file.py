import pandas as pd
import os

def creat_list(path):
	list = os.listdir(str(path))
	if(len(list) <1):
		print("list file kosong")
	else:
		D_list = ""
		for N_list in list:
			D_list += N_list+"\n"
		file = open("list_file.txt", "w")
		file.writelines(D_list)
		print("list_file.txt berhasil di buat...")
		
		
def join_file(path):
	list = open("list_file.txt", "r")
	list = list.readlines()
	
	# Membuat file main list ke 0
	df = pd.read_csv(str(path+list[0].replace("\n","")))
	df.to_csv("join_file.csv", index=False)
	print("membuat file main join_file.csv")

	print("----------------------------------------")
	print("1. data "+str(list[0].replace("\n",""))+" berhasil di tambahkan")
	print("----------------------------------------")
	
	# Mulai loop dari index ke 1
	i = 1
	new_file = "join_file.csv"
	data = pd.read_csv(str(new_file))
	mainData = pd.DataFrame(data)

	while(i < len(list)):
		
		# Baca file index ke i
		seconData = pd.read_csv(str(path+list[i].replace("\n","")))

		add = mainData.append(seconData, ignore_index=True)

		# Update variabel data main
		mainData = pd.DataFrame(add)
		print(str(str(i+1)+". data "+list[i].replace("\n",""))+" berhasil di tambahkan")
		print("----------------------------------------")
		i +=1
	print(mainData)
	mainData.to_csv("join_file.csv", index=False)
	
	
	
if __name__ == "__main__":
	path = input("path folder csv :")
	print("----------------------------------------")

	# membuat list nama file
	creat_list(path)
	list = open("list_file.txt","r")
	list = list.readlines()
	print(list)

	a = str(input("lanjutkan y/n : "))
	if(a == "y"):
		join_file(path)
	else:
		print("aplikasi berhenti")
