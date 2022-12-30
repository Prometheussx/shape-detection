import cv2
import numpy as np
#yazı fontu
font = cv2.FONT_HERSHEY_SIMPLEX
font1= cv2.FONT_HERSHEY_COMPLEX #opencv fonts

img = cv2.imread("polygons.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,threshold = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    epsilon = 0.01*cv2.arcLength(cnt,True)
    
    #epsilon hazır bir mateaitksel bir işlem
    approx = cv2.approxPolyDP(cnt,epsilon,True)#yaklaşım demek
    
    #yaklaşımlara contur çiziyor
    cv2.drawContours(img,[approx],0,(0),5)

    x = approx.ravel()[0] #sütunları satıra çevirir ravel yapısı
    y = approx.ravel()[1]

    if len(approx)==3:
        #yazıcağımız konum xve ye oluyor
        #b u x y ler belirtilen çokgenin önceden hazırlanan
        #değerlerine göre ilk köşesine yazılmasını sağlıyor
        cv2.putText(img,"Triangle",(x+20,y-10),font,0.6,(0))
        
    elif len(approx)==4:
        cv2.putText(img,"Rectangle",(x+20,y-10),font,0.6,(0))
        
    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x+10,y-10),font,0.6,(0))
        
    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x+20,y-10),font,0.6,(0))
        
    else:
        cv2.putText(img,"Ellipse",(x+20,y+10),font,0.6,(0))

cv2.imshow("IMG",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
        

"""
Yapı şu şekildeiliyor aproxun içinde köşegene göre 
örnek: üçgence 3 adet beşgense 5 adet satır oluyor o çokgene özel 
ve o çokgenin kenarları için oluşmuş olan satırlarda iki adet değer oluşuyor
bu değerler o kenarın x ve y değerleri oluyor

"""

