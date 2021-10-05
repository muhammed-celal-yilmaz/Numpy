
# NUMPY ÇALIŞMALARI DÖKÜMANTASYON
#Veri analizinde kullanılan verimli kütüphanelerden biridir.
#Sayılar genel olarak baz alınır.


import numpy as np

# a=np.arange(15).reshape(3,5)
# print(a)
# print(type(a))
# print("Dimension Count:"+str(a.ndim))
# print("*********************************")
# b=np.arange(10)
# print(b.shape)
# print("Dimension"+str(b.ndim))
#c=np.arange(1,10)

#**************************************************

# a=np.array([1,2,5,4,7,8,12,14])
# print(a)
# print(a.reshape(2,4)) #2 satır 4 sütun eleman sayısına dikkat.
# b=np.array([1,3.5,8,9])
# c=np.array([4,"5",6])
# print(a.dtype)
# print(b.dtype)
# print(c.dtype)

# print(a.ndim)
# d=np.array([[3,5],[2,6],[8,9]])
# print(d.ndim)

#*************************************************
#istatiksel olarak kullanılır.
# a=np.linspace(1,10) #default eşit aralıklarla 50 sayı
# print(a)
# b=np.linspace(1,10,10) #1 ila 10 dahil
# print(b)
# c=np.linspace(1,10,4) 
# print(c)
# from numpy import pi
# q=np.linspace(0,2*pi,10) # 0 ila 2*pi araası değerler
# print(q)
# print(np.sin(q))# bunların sinüs değerleri

#*************************************************
#Temel veri işlemleri
# a=np.array([10,20,30,40])
# b=np.arange(4)
# c=a-b
# print(c)#Eleman sayıları aynı olmalı yoksa error!
# b=b**2
# print(b)
# x=np.array([30,60,90])
# y=10*np.sin(x)
# print(y)
# print(y<5)
# print(a*b)
# print(a@b)#Matris çarpım toplamı
# print(a.dot(b))#Yukardakiyle aynı matris çarpım

# e=np.ones((2,2))#2*2 matris
# f=np.zeros((3,3)) #3*3 0'lardan matris
# h=np.floor(np.random.random((3,3))*10)
# j=np.sum(b)
# print(e)
# print(f)
# print(h)
# print(j)
# print(b.sum())

# print(np.min(b))
# print(np.max(b))
# print(np.sqrt(b))
#**************************************

# sayilar=np.array([5,10,15,20,25,30])
# print(sayilar[5])
# print(sayilar[0:3])
# sayilar2=np.array([[5,10,15],[20,25,30]])
# print(sayilar2[1])
# print(sayilar2[1,2])
# print(sayilar2[:,2])#tüm satırlardan
# print(sayilar2[:,0]) #tüm satırlardan 0.index
# print(sayilar2[:,0:2])
# print(sayilar[::-1])#diziyi tersten yazdırma
# print(sayilar2[-1,:])#en son satırdan tüm sütunlar,tek boyut olmasın.
# print(sayilar2[:,-1])#tüm satırlardan son sütunlar

#**************************************

# h=np.floor(np.random.random((2,4))*10)
# print(h)
# print(h.shape) #Boyutu
# print(h.ravel())#Düzleştirme
# h=h.ravel()
# print(h.shape)
# print(h.reshape(2,4))#tekrar boyutlandırdık
# h=h.reshape(4,2)
# print(h)
# print(h.T) # yana yatırdık.
# print(h.reshape(2,-1)) #2 satır yap rastegel sütunlara dağıt elemanları


#**************************************
#horizontal,vertical
#Stacking
# x=np.floor(10*np.random.random((2,3)))
# y=np.floor(10*np.random.random((2,3)))
# print(x)
# print(y)
# c=np.vstack((x,y)) #alt alta birleştirir.
# print(c)
# d=np.hstack((x,y)) #yan yana birleştirir.
# print(d)
#***************************************

# a=np.arange(10)
# b=a #referans dikkat.
# print(a)
# print(b)
# b[1]=50
# print(a)
# print(b)

# c=a.copy() # değer ataması
# c[0]=100
# print(a)
# print(c)
# print("\n**********")

# d=a.view()
# d[0]=400 #her ikisinde değişir.
# d.shape=5,2
# print(a)
# print(d) #sadece d reshape edilir.


















