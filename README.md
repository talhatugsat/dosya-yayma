# Ana sunucuda bulunan dosyaları diğer sunuculara dağıtma tool'u
İstediğiniz şey için kullanabilirsiniz, main.py'de ki değişkenlerden bahsedeyim:<br>
local_dir = python scripti çalıştırdığınız sunucuda bulunan diğer sunuculara dağıtmak istediğiniz klasörün lokasyonu<br>
remote_dir = dağıtmak istediğiniz sunuculardaki dosya lokasyonu<br>
telegram_chat = telegram bildirimi içindir, telegram chat ID temsil eder<br>
telegram_bot_token = telegram bot tokenidir, telegram bot tokeninizi temsil eder<br>
sleepsecond = scriptin kendini kaç saniyede bir tekrar başlatacağını temsil eder<br>
hosts = adından da anlaşılacağı üzere karşı sunucuları temsil eder<br>

ek olarak yararlı fonksiyon mevcuttur:<br>
ssh_obj.restartService("servis-adi")<br>

nohup ile ana sunucu içinde python3 ile çalıştırabilirsiniz
