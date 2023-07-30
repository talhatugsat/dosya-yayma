# Ana sunucuda bulunan dosyaları diğer sunuculara dağıtma tool'u
İstediğiniz şey için kullanabilirsiniz, main.py'de ki değişkenlerden bahsedeyim:
local_dir = python scripti çalıştırdığınız sunucuda bulunan diğer sunuculara dağıtmak istediğiniz klasörün lokasyonu
remote_dir = dağıtmak istediğiniz sunuculardaki dosya lokasyonu
telegram_chat = telegram bildirimi içindir, telegram chat ID temsil eder
telegram_bot_token = telegram bot tokenidir, telegram bot tokeninizi temsil eder
sleepsecond = scriptin kendini kaç saniyede bir tekrar başlatacağını temsil eder
hosts = adından da anlaşılacağı üzere karşı sunucuları temsil eder

ek olarak yararlı fonksiyon mevcuttur:
ssh_obj.restartService("servis-adi")

nohup ile ana sunucu içinde python3 ile çalıştırabilirsiniz
