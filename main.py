from keep_alive import keep_alive
from instagrapi import Client
import time


# Giriş
cl = Client()
cl.login("playboicartifc31, Eghuse1978")

# Hedef kullanıcı
hedef_kullanici_adi = "_karakuzu_egemen_"  # Sadece bu kişiden gelen mesajlara cevap ver
hedef_kullanici_id = cl.user_id_from_username(hedef_kullanici_adi)

# Tek cevap atması için kontrol
yanitlandi = False

while True:
    sohbetler = cl.direct_threads(amount=5)
    for sohbet in sohbetler:
        mesajlar = sohbet.messages
        if not mesajlar:
            continue

        son_mesaj = mesajlar[0]

        if son_mesaj.user_id == hedef_kullanici_id and not son_mesaj.is_sent_by_viewer and not yanitlandi:
            cl.direct_send("WLFLALCLAKFPSKDĞÖ bendir uyuyom şu an ", [hedef_kullanici_id])
            print("Cevap gönderildi.")
            yanitlandi = True

    time.sleep(5)  # Her 5 saniyede bir kontrol eder