#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Komşu Dedikodu Üreteci - Bilimsel Dedikodu Motoru
Versiyon 1.0 - Aşırı Ciddi
"""

import random
import time

def uret_dedikodu():
    kisiler = [
        "komşunun kızı",
        "alt kattaki amca",
        "karşı dairenin gelini",
        "kapıcının oğlu",
        "çatıdaki kedi (asıl komşu o)"
    ]
    eylemler = [
        "gece 3'te müzik açıyormuş",
        "sabah 7'de halı silkeliyormuş",
        "marketten 3 koli deterjan almış (ne yapacak acaba)",
        "balkonunda yoga yapıyormuş (tuhaf hareketler)",
        "kargo kutusunu açmadan 2 saat bakmış"
    ]
    sonuclar = [
        "bütün mahalle konuşuyor",
        "site yönetimi toplantı yapacakmış",
        "kimse doğrulamıyor ama herkes biliyor",
        "WhatsApp grubunda 47 mesaj oldu",
        "artık kimse selam vermiyor"
    ]
    
    kisi = random.choice(kisiler)
    eylem = random.choice(eylemler)
    sonuc = random.choice(sonuclar)
    
    return f"Duydum ki {kisi} {eylem}. {sonuc.capitalize()}."

def main():
    print("=== KOMŞU DEDİKODU ÜRETECİ v1.0 ===")
    print("Bilimsel kesinlikle çalışmaktadır. Lütfen ciddiye alınız.")
    print()
    
    for i in range(5):
        print(f"Dedikodu #{i+1}: {uret_dedikodu()}")
        time.sleep(0.5)
    
    print()
    print("Üretim tamamlandı. Mahalle huzuru (bozuldu) sağlandı.")

if __name__ == "__main__":
    main()

# Gizli not: QW5hIHlhcsSxIHZlcm1leWkgdW51dG1hIGltZSA=
# (Bu satırı merak etmeyin, önemli değil. Gerçekten.)
