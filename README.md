#Сурагч бүртгэл

Эхлээд [python](https://python.org/downloads) суусан байх шаардлагатай. Python сангаа өөрт тохирох ҮС тааруулан татаж авна.

##Windows

- Виндөвс хувилбар татаж аваад суулгаад, My computer -> Properties -> Advanced -> Environment Variables -> System Variables -аас Path -ыг сонгоод доорхийг хуулж тавина.
```
;C\Python27;C\Python27\Scripts;
```
- Ингэснээр **CMD** ээс python болон pip ээ дуудах боломжтой болно. Одоо **CMD** гээ нээгээд **"cread"** хавтас руу `cd` командаар ороод доорхийг бичээд *Enter* дарна.
```
pip install -r requirements.txt
```
- Дээрхийг ажиллуулахаар _Django_ татаж авна. Дараа нь прожэкт маань ажиллахад бэлэн болно. Ажиллуулахдаа **"cread"** хавтасруу ороод доорх командыг **CMD** дээр бичиж ажиллуулна.
```
python manage.py runserver
```
---
##Linux

- Python угаасаа суучихсан учир татах шаардлагагүй, шууд **"cread"** хавтасруу terminal аас ороод доорхи командыг бичиж ажиллуулна. 
```
pip install -r requirements.txt //хэрэгтэй бол sudo ашиглана
```
- Ингэж _Django_ татаж авч суулгаад ажиллуулахад бэлэн болно. **"cread"** хавтасруу ороод доорхи командыг бичиж ажиллуулна. 
```
python manage.py runserver
```
---
#Өгөгдлийн санг шинээр үүсгэх
* өгөгдлийн санг шинээр үүсгэх хэрэгтэй, үүний тулд **"cread"** хавтас дотор байгаа _db.sqlite3_ файлыг, _regist_ хавтас дотор байгаа _migrations_ хавтасыг тус тус устгах хэрэгтэй. Дараа нь шинээр бааз үүсгэхийн тулд доорхи командыг бичиж ажиллуулна
```
python manage.py migrate
```
* Үүний дараа баазад хэрэглэгч үүсгэж өгөх шаардлагатай хэрэглэгч үүсгэхийн тулд доорхи командыг ажиллуулна
```
python manage.py createsuperuser
```

### Бүртгэлийн *Үдээс хойш, Үдээс өмнө* гэсэн цагыг солих бол:
- **"cread"** хавтас дотор байрлах _cread_ хавтасруу ороод `settings.py` файлыг нээж 
`TIME_ZONE = 'Asia/Seoul'` гэснийг Цагын бүсийн дагуу өөрчилнө.
