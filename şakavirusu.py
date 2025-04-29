import os
import webbrowser
import time

# 1. Başlangıç mesajı
print("Sistemin ele geçirildi! ")

# 2. Tarayıcıda evcil hayvan (kedi) aç
time.sleep(2)
webbrowser.open("")  # Sevimli kedi resmi

# 3. Eğlenceli döngüyle ekranı doldur
for i in range(5):
    os.system("start https://github.com/HamzaAlkan55")
    time.sleep(1)
