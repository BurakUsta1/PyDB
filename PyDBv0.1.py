#PyDBv0.1 uygulaması
import pandas as pd
import sqlite3 as sqllite
import os

# Dikdörtgen
genişlik= 60
uzunluk = 6

for i in range(uzunluk):
    if i == 0 or i == uzunluk-1:
        print('_' * genişlik)
    elif i == 2:
     	orta= int((genişlik-1)/2-len("PyDB"))
     	print("|" +" "*orta+"PyDB"+" "*orta+"    |")
    elif i == 4:
     	print("|"+" "* int(genişlik-len("v0.1")-3)+"v.0.1|")
    else:
        print('|' + ' ' * (genişlik - 2) + '|')
        
class veritabanıİşlemleri:
	def veritabanlarıListe(self):
		# Dikdörtgen2
		genişlik2= 60
		uzunluk2 = 4
		
		for i in range(uzunluk2):
		    if i == 0 or i == uzunluk2 - 1:
		        print('_' * genişlik2)
		    elif i == 1:
		     	print("Veritabanları")
		     	print('-' * genişlik)
		    elif i == 2:
		    	global veritabanları 
		    	veritabanları= []
		    	s=1
		    	for i in os.listdir("/storage/emulated/0"):
		    		if os.path.splitext(i)[1] == ".db":
		    			veritabanları.append(i)
		    			veriT="|"+"{}.{}".format(s,i)
		    			print(veriT+" "*int(genişlik2-1-len(veriT))+"|")
		    			s = s+1
		    else:
		        print('-' + ' ' * (genişlik2 - 2) + '-')
	
	def baglan(self):
				while len(veritabanları) > 0:
					veritabanı= input("Bağlanmak istediğiniz veritabanının numarasını yazınız:\n-->")
					if veritabanı == "Çıkış" :#düzelt
						break
					else:
						try:
							sqllite.connect(veritabanları[int(veritabanı) -1])
							print(veritabanları[int(veritabanı) -1],": Bağlandı")
							break
						except ValueError:
							print("Lütfen sadece sayıları kullanın")
							continue
						except Exception as e:
							print(veritabanları[int(veritabanı) -1],":Bağlanamadı",e)
							break					
				else:
					print("Bağlanılabilecek veritabanı yok.")	
			
	
	def oluştur(self):
			while True:
				yeniVeritabanı= input("Oluşturmak istediğiniz veritabanının ismini yazınız:\n-->")
				if yeniVeritabanı == "Çıkış":#düzelt
						break
				else:
					for i in veritabanları:
						if yeniVeritabanı+".db" == i:
							print("Bu veritabanı zaten mevcut")
							continue
						elif not yeniVeritabanı.endswith(".db") and "." in yeniVeritabanı:
							try:
								isim=yeniVeritabanı.split(".")[0]
								uzantı= yeniVeritabanı.split(".")[1]= ".db"
								düzenliYeniVeritabanı= isim+uzantı
								sqllite.connect(düzenliYeniVeritabanı)
								sqllite.connect(düzenliYeniVeritabanı).close()
								print("Veritabanı oluşturuldu.")
								break
							except Exception as e:
								print("Veritabanı oluşturulamadı:",e)
								continue
						else:
							try:
								yeniVeritabanı= yeniVeritabanı+".db"
								sqllite.connect(yeniVeritabanı)
								sqllite.connect(yeniVeritabanı).close()
								print("Veritabanı oluşturuldu.")
								break
							except Exception as e:
								print("Veritabanı oluşturulamadı:",e)
								continue
	def sil(self):
				while len(veritabanları) > 0:
					veritabanı= input("Silmek istediğiniz veritabanının numarasını yazınız:\n-->")
					if veritabanı == "Çıkış" :#düzelt
						break
					else:
						try:
							os.remove(veritabanları[int(veritabanı) -1])
							print("Veritanbanı silindi:",(veritabanları[int(veritabanı) -1]))
							break
						except ValueError:
							print("Lütfen sadece sayıları kullanın")
							continue
						except Exception as e:
							print(veritabanları[int(veritabanı) -1],":Silinemedi",e)
							break					
				else:
					print("Silinecek veritabanı yok.")			

vtİşlemleri= veritabanıİşlemleri()
vtİşlemleri.veritabanlarıListe()

print("1.Veritabanına Bağlan\n2.Veritabanı Oluştur\n3.Veritabanı Sil\n\nÇ.Çıkış")
while True:
		 secim= input("->")
		 if secim == "1":
		 	 vtİşlemleri.baglan()
		 elif secim == "2":
		 	vtİşlemleri.oluştur()
		 elif secim == "3":
		 	vtİşlemleri.sil()
		 elif secim == "Çıkış":#düzelt
		 	break		 	