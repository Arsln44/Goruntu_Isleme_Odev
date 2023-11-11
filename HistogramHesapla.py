import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü oku
image = cv.imread("https://github.com/Arsln44/HistogramHesaplama/blob/main/atam.jpg")
hist = cv.calcHist([image],[0],None,[256],[0,256])


if image is not None:
    # Görüntü başarıyla yüklendi, ekranda göster
    cv.imshow("Örnek Görüntü", image)

    # Kullanıcının bir tuşa basmasını bekleyin ve pencereyi kapatın
    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Görüntü yüklenemedi veya bulunamadı.")

plt.hist(image.ravel(),256,[0,256])
plt.xlabel("Piksel değeri :")
plt.ylabel("Piksel sayısı :")
plt.show()
    
