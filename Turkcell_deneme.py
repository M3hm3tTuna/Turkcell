telefon=["Redmi Note12Pro","Nokia 3310","Samsung S6","Samsung Galaxy Note6","Huawei P-Smart"]
bilgisayar=["Dell XPS Desktop","Acer Aspire TC","Apple Mac Mini M2","Apple iMac 24-inch","Lenovo Legion Tower 5i"]
kulaklik=["Sony WH-1000XM4 Wireless","Shure Aonic 50 Gen 2","Edifier Stax Spirit S3","Sennheiser Momentum 4","Audio-Technica ATH-TWX7"]
ev_esya=["Samsung 189 L","iRobot Roomba j7+","DİJİTSU DB100 Tezgahaltı Buzdolabı","LG Smart Slide-In Double Oven","Toshiba EM131A5C-BS"]
oyun=["PS5","Logitech MX Master 3S","XBox360","Meta Quest 3","Xbox Wireless Controller"]
#ürünlerin listesi ^
fiyat_siralama=["Toshiba EM131A5C-BS(🍳)","Nokia 3310(📱)","Shure Aonic 50 Gen 2(🔊)","LG Smart Slide-In Double Oven(🍳)","Huawei P-Smart(📱)","Logitech MX Master 3S(🎮)","Audio-Technica ATH-TWX7(🔊)","XBox360(🎮)","DİJİTSU DB100 Tezgahaltı Buzdolabı(🍳)","Samsung S6(📱)","Sony WH-1000XM4 Wireless(🔊)","Redmi Note12Pro(📱)","Lenovo Legion Tower 5i(💻)","Edifier Stax Spirit S3(🔊)","iRobot Roomba j7+(🍳)","Acer Aspire TC(💻)","Sennheiser Momentum 4(🔊)","Meta Quest 3(🎮)","Xbox Wireless Controller(🎮)","Apple Mac Mini M2(💻)","PS5(🎮)","Samsung 189 L(🍳)","Apple iMac 24-inch(💻)","Samsung Galaxy Note6(📱)","Dell XPS Desktop(💻)"]
#ürünlerin küçükten büyüğe sıralanmış hali ^
itemler=[telefon,bilgisayar,kulaklik,ev_esya,oyun]
onerilenler=0
ortalama=0.0
gecmis_ad=[]
gecmis_fiyat=0.0
fiyatlar_tel=[12999,1099,11999,38400,12989]
fiyatlar_bil=[95626.91,17699.99,22310.20,49999,13999]
fiyatlar_klk=[11999,1940.53,14062.70,19999,6339.39]
fiyatlar_ev=[30499,15499,8000,2499,140.61]
fiyatlar_oyn=[27999,3799,6349,19999,3009]
sort_tel=fiyatlar_tel.sort()
sort_bil=fiyatlar_bil.sort()
sort_klk=fiyatlar_klk.sort()
sort_ev=fiyatlar_ev.sort()
sort_oyn=fiyatlar_oyn.sort()
# ^ her kategori için özel fiyat sıralaması
fiyatlar_list_tel=["Nokia 3310(📱)","Huawei P-Smart(📱)","Samsung S6(📱)","Redmi Note12Pro(📱)","Samsung Galaxy Note6(📱)"]
fiyatlar_list_bil=["Lenovo Legion Tower 5i(💻)","Acer Aspire TC(💻)","Apple Mac Mini M2(💻)","Apple iMac 24-inch(💻)","Dell XPS Desktop(💻)"]
fiyatlar_list_klk=["Shure Aonic 50 Gen 2(🔊)","Audio-Technica ATH-TWX7(🔊)","Sony WH-1000XM4 Wireless(🔊)","Edifier Stax Spirit S3(🔊)","Sennheiser Momentum 4(🔊)"]
fiyatlar_list_ev=["Toshiba EM131A5C-BS(🍳)","LG Smart Slide-In Double Oven(🍳)","DİJİTSU DB100 Tezgahaltı Buzdolabı(🍳)","iRobot Roomba j7+(🍳)","Samsung 189 L(🍳)"]
fiyatlar_list_oyn=["Logitech MX Master 3S(🎮)","XBox360(🎮)","Meta Quest 3(🎮)","Xbox Wireless Controller(🎮)","PS5(🎮)"]
#ürünler kendi içinde büyükten küçüğe sıralanmış ^
toplam=0
giris="Bu Sunum Mehmet Tuna BAŞ ve Arda MOLLA Tarafından Hazırlanmıştır (!Prototiptir!)"
print(giris+"\n"+"-"*len(giris)+"\n ")
isim=input("Adınızı Giriniz: ")
while True:
    yas=int(input("Yaşınız Giriniz: "))
    if 0<yas<18: # 18'den küçük mü?
        print("Fazla Gençsiniz!")
        devam=0
        break
    elif 17<yas: # 18'den büyük mü?
        devam=1
        break
    else: # imkansız yaş aralığı
        print("Hatalı yaş!")
if devam==0:
    print("Görüşürüz...")
else:
    print("Hoşgeldiniz",isim+"!\n ")
    while True:
        if gecmis_fiyat>0:
            ortalama=round(gecmis_fiyat,2)/len(gecmis_ad)
        yuvarlama=round(ortalama,2)
        bsort=32-len(str(yuvarlama))
        kategori_sayisi=-1
        kategoriler=["Telefon|📱","Bilgisayar|💻","Kulaklık|🔊","Ev Eşyası|🍳","Oyun|🎮","Önerilenler|👌","Geçmiş|⏱ "]
        bosluk_sayisi2=41-len(kategoriler[kategori_sayisi])
        bosluk_sayisi3=36-len(kategoriler[6])
        menu="||Kategoriler:"+" "*17+'-1 "çıkış"||'
        menu2="||Toplam: "+str(gecmis_fiyat)+" "*bsort+"||"
        menu4="||"+" "*bosluk_sayisi3+kategoriler[6]+'(6)'+"||"
        print("="*len(menu)+"\n"+menu+"\n"+menu2)
        for sayi in range(1,len(kategoriler)):
            kategori_sayisi=kategori_sayisi+1
            secim=str(kategori_sayisi)
            bosluk_sayisi2=35-len(kategoriler[kategori_sayisi])
            menu3="||"+" "*bosluk_sayisi2+kategoriler[kategori_sayisi]+'('+secim+')'+"||"
            print(menu3)
        print(menu4)
        print("="*len(menu))
        sectiniz=int(input("Bir Kategori Seçiniz: "))
        if sectiniz==-1:
            print("Kapatılıyor...")
            break
        elif sectiniz<-1:
            print("Hatalı Kategori! Tekrar Deneyin!")
            continue
        else:
            if sectiniz>len(kategoriler)-1:
                print(sectiniz,"numaralı bir kategorimiz yoktur. Lütfen tekrar deneyiniz...")
            else:
                secili_kategori=str(kategoriler[sectiniz])
                print("="*len(menu))
                lenkat=19-len(secili_kategori)
                yazi2="||Kategori: "+secili_kategori+" "*lenkat+'-1 "geri"||'
                print(yazi2+"\n||Toplam: "+str(gecmis_fiyat)+" "*bsort+"||")
                sayi2=0
                if sectiniz==0: #telefon kategrosi
                    for sayac in range(1,len(telefon)+1):
                        bs=36-len(telefon[sayi2])
                        menutek="||"+" "*bs+telefon[sayi2]+'('+str(sayi2)+')'+"||"
                        print(menutek)
                        sayi2+=1
                    print("="*len(menu))
                    satin_al=int(input("Ürün Seçiniz: "))
                    if -1<satin_al<len(kategoriler):
                        gecmis_ad.insert(1,telefon[satin_al]+"(📱)")
                        gecmis_fiyat+=(fiyatlar_tel[satin_al])
                    elif satin_al==-1:
                        continue
                elif sectiniz==1: #bilgisayar kategrosi
                    for sayac in range(1,len(bilgisayar)+1):
                        bs=36-len(bilgisayar[sayi2])
                        menutek="||"+" "*bs+bilgisayar[sayi2]+'('+str(sayi2)+')'+"||"
                        print(menutek)
                        sayi2+=1
                    print("="*len(menu))
                    satin_al=int(input("Ürün Seçiniz: "))
                    if -1<satin_al<len(kategoriler):
                        gecmis_ad.insert(1,bilgisayar[satin_al]+"(💻)")
                        gecmis_fiyat+=(fiyatlar_bil[satin_al])
                    elif satin_al==-1: #kulaklık kategrosi
                        continue
                elif sectiniz==2:
                    for sayac in range(1,len(kulaklik)+1):
                        bs=36-len(kulaklik[sayi2])
                        menutek="||"+" "*bs+kulaklik[sayi2]+'('+str(sayi2)+')'+"||"
                        print(menutek)
                        sayi2+=1
                    print("="*len(menu))
                    satin_al=int(input("Ürün Seçiniz: "))
                    if -1<satin_al<len(kategoriler):
                        gecmis_ad.insert(1,kulaklik[satin_al]+"(🔊)")
                        gecmis_fiyat+=(fiyatlar_klk[satin_al])
                    elif satin_al==-1:
                        continue
                elif sectiniz==3: #ev eşyası kategrosi
                    for sayac in range(1,len(ev_esya)+1):
                        bs=36-len(ev_esya[sayi2])
                        menutek="||"+" "*bs+ev_esya[sayi2]+'('+str(sayi2)+')'+"||"
                        print(menutek)
                        sayi2+=1
                    print("="*len(menu))
                    satin_al=int(input("Ürün Seçiniz: "))
                    if -1<satin_al<len(kategoriler):
                        gecmis_ad.insert(1,ev_esya[satin_al]+"(🍳)")
                        gecmis_fiyat+=(fiyatlar_ev[satin_al])
                    elif satin_al==-1:
                        continue
                elif sectiniz==4: #oyun kategrosi
                    for sayac in range(1,len(oyun)+1):
                        bs=36-len(oyun[sayi2])
                        menutek="||"+" "*bs+oyun[sayi2]+'('+str(sayi2)+')'+"||"
                        print(menutek)
                        sayi2+=1
                    print("="*len(menu))
                    satin_al=int(input("Ürün Seçiniz: "))
                    if -1<satin_al<len(kategoriler):
                        gecmis_ad.insert(1,oyun[satin_al]+"(🎮)")
                        gecmis_fiyat+=(fiyatlar_oyn[satin_al])
                    elif satin_al==-1:
                        continue
                elif sectiniz==5: #önerilenler kategrosi
                    if onerilenler==0: #eğer kullanıcı hiçbir şey satın almadıysa önerilecek bir şey yok
                        print("||       |Burada Hiçbir Şey Yok🦗|       ||\n||"+" "*39+"||")
                    else:
                        gecmis_tel=gecmis_ad.count("📱")
                        gecmis_bil=gecmis_ad.count("💻")
                        gecmis_klk=gecmis_ad.count("🔊")
                        gecmis_ev=gecmis_ad.count("🍳")
                        gecmis_oyn=gecmis_ad.count("🎮")
                        gecmis_ort=[gecmis_tel,gecmis_bil,gecmis_klk,gecmis_ev,gecmis_oyn]
                        urun_ort=max(gecmis_ort)
                        if urun_ort==gecmis_tel:
                            for sayac in range(0,5):
                                bs=36-len(str(fiyatlar_list_tel[sayac]))
                                menutek="||"+" "*bs+str(fiyatlar_list_tel[sayac])+'('+str(sayi2)+')'+"||"
                                print(menutek)
                                sayi2+=1
                        elif urun_ort==gecmis_bil:
                            for sayac in range(0,5):
                                bs=36-len(str(fiyatlar_list_bil[sayac]))
                                menutek="||"+" "*bs+str(fiyatlar_list_bil[sayac])+'('+str(sayi2)+')'+"||"
                                print(menutek)
                                sayi2+=1
                        elif urun_ort==gecmis_klk:
                            for sayac in range(0,5):
                                bs=36-len(str(fiyatlar_list_klk[sayac]))
                                menutek="||"+" "*bs+str(fiyatlar_list_klk[sayac])+'('+str(sayi2)+')'+"||"
                                print(menutek)
                                sayi2+=1
                        elif urun_ort==gecmis_ev:
                            for sayac in range(0,5):
                                bs=36-len(str(fiyatlar_list_ev[sayac]))
                                menutek="||"+" "*bs+str(fiyatlar_list_ev[sayac])+'('+str(sayi2)+')'+"||"
                                print(menutek)
                                sayi2+=1
                        elif urun_ort==gecmis_oyn:
                            for sayac in range(0,5):
                                bs=36-len(str(fiyatlar_list_oyn[sayac]))
                                menutek="||"+" "*bs+str(fiyatlar_list_oyn[sayac])+'('+str(sayi2)+')'+"||"
                                print(menutek)
                                sayi2+=1
                    print("="*len(menu))
                    satin_al=int(input("Ürün Seçiniz: "))
                    if -1<satin_al<len(kategoriler):
                        if satin_al<5:
                            gecmis_ad.insert(1,fiyatlar_list_tel[satin_al])
                            gecmis_fiyat+=sort_tel[satin_al]
                        else:
                            print(satin_al,"numaralı bir eşyamız yoktur. Lütfen tekrar deneyiniz...")
                            continue
                    elif satin_al==-1:
                        continue
                elif sectiniz==6: #geçmiş kategrosi
                    if len(gecmis_ad)==0: #eğer kullanıcı hiçbir şey almadısya geçmişte bir şey gözükmez
                        print("||       |Burada Hiçbir Şey Yok🦗|       ||\n||"+" "*39+"||")
                    else:
                        for sayac in gecmis_ad:
                            bs=39-len(str(gecmis_ad[sayi2]))
                            menutek="||"+" "*bs+str(gecmis_ad[sayi2])+"||"
                            print(menutek)
                            sayi2+=1
                        bsgms=29-len(str(yuvarlama))
                        print("||"+" "*bsgms+str(yuvarlama),":Ortalama||")
                    print("="*len(menu))
                    satin_al=int(input("Ürün Seçiniz: "))
                    if satin_al==-1:
                        continue
                    else:
                        print("Burada Satın Alınabilecek Bir Şey Yok😬...")
                        #geçmişten bir şey satın alamazsın ^
                else:
                    print(satin_al,"numaralı bir ürünümüz yoktur. Lütfen tekrar deneyiniz...")
                if yuvarlama==0:
                    continue
                else:
                    onerilenler=1
print(yuvarlama)