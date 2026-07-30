import json
from datetime import datetime

print("Güncelleme betiği çalıştı:", datetime.now())

# Şimdilik örnek CubeCraft/oyuncu verilerini güncelleyen bir yapı
yeni_veriler = [
    {"sira": 1, "isim": "ProMinecraftci", "skor": 99000, "seviye": 76, "mac": 1260},
    {"sira": 2, "isim": "KralOuncu", "skor": 88000, "seviye": 69, "mac": 990},
    {"sira": 3, "isim": "BlokUstasi", "skor": 76000, "seviye": 55, "mac": 730}
]

# oyuncular.json dosyasına bu verileri yazıyoruz
with open('oyuncular.json', 'w', encoding='utf-8') as f:
    json.dump(yeni_veriler, f, ensure_ascii=False, indent=4)

print("oyuncular.json başarıyla güncellendi!")
