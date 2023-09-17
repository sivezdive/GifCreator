from PIL import Image
import os
import glob

# Yeniden boyutlandırmak istediğiniz hedef boyut (genişlik x yükseklik)
hedef_genislik = 480
hedef_yukseklik = 480

# Boyutlandırmak istediğiniz resim dosyalarının listesi
resimler = [
    "C:/Users/MustafaAtalar/Pictures/Saved Pictures/image.jpg",
    "C:/Users/MustafaAtalar/Pictures/Saved Pictures/image1.jpg",
    "C:/Users/MustafaAtalar/Pictures/Saved Pictures/image2.jpg",
    "C:/Users/MustafaAtalar/Pictures/Saved Pictures/image3.jpg",
    "C:/Users/MustafaAtalar/Pictures/Saved Pictures/image4.jpg"
]

# Yeniden boyutlandırılmış resimleri saklayacak bir klasör oluşturun
yeniden_boyutlandirilmis_klasor = "yeniden_boyutlandirilmis_resimler"
if not os.path.exists(yeniden_boyutlandirilmis_klasor):
    os.mkdir(yeniden_boyutlandirilmis_klasor)

# Resimleri yeniden boyutlandırın ve yeni klasöre kaydedin
for resim_adi in resimler:
    try:
        # Görüntüyü aç
        image = Image.open(resim_adi)

        # Yeniden boyutlandır
        yeniden_boyutlandirilmis = image.resize((hedef_genislik, hedef_yukseklik), Image.LANCZOS)

        # Orijinal dosya adını al
        dosya_adi = os.path.basename(resim_adi)

        # Yeniden boyutlandırılmış görüntüyü kaydet
        yeni_resim_adi = os.path.join(yeniden_boyutlandirilmis_klasor, "yeniden_boyutlandirilmis_" + dosya_adi)
        yeniden_boyutlandirilmis.save(yeni_resim_adi)

        # Görüntüyü kapat
        image.close()

        print(f"{resim_adi} başarıyla yeniden boyutlandırıldı ve kaydedildi: {yeni_resim_adi}")

    except Exception as e:
        print(f"{resim_adi} yeniden boyutlandırılırken bir hata oluştu: {str(e)}")

# Yeniden boyutlandırılmış resimleri kullanarak bir GIF oluşturun
fp_in = os.path.join(yeniden_boyutlandirilmis_klasor, "*.jpg")
fp_out = "C:/Users/MustafaAtalar/Pictures/Saved Pictures/output.gif"

# Görüntüleri yükle
image_list = []
for filename in sorted(glob.glob(fp_in)):
    img = Image.open(filename)
    image_list.append(img)

# İlk görüntüyü al
first_image = image_list[0]

# Diğer görüntüleri ekleyerek GIF'i kaydet
first_image.save(
    fp=fp_out,
    format='GIF',
    append_images=image_list[1:],
    save_all=True,
    duration=400,
    loop=7
)

print(f"GIF dosyası başarıyla oluşturuldu: {fp_out}")
