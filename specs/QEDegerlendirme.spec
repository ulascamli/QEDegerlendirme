#Testinium

Login ve logout kontrolleri
---------------------------
tags: loginAndLogoutTest

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Logout butonuna tiklanir
* Uygulamadan logout olundugu dogrulanir

Yanlis sifre ile login kontrolu
---------------------------
tags: incorrectPasswordTest

* "ulas.camli@testinium.com" ve "1232134" ile giris yapilir
* Giris denemesi basarisiz oldugu dogrulanir

Yanlis username ile login kontrolu
---------------------------
tags: incorrectUsernameTest

* "ulas.camli" ve "158358Ulas" ile giris yapilir
* Giris denemesi basarisiz oldugu dogrulanir

Account Name Degisikligi Kontrol edilir
---------------------------
tags: changeAccountNameTest

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Kullanici adi degistirilir ve kontrol edilir ardindan eski haline getirilir

Account Name Numeric Deger Kabul etmemesi senaryosu
---------------------------
tags: dontChangeAccountNameWithOnlyNumeric

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Kullanici adi alanına numerik deger girilir ve update butonu disable kaldigi kontrol edilir

Account Name Bos birakilmayi kabul etmemesi senaryosu
---------------------------
tags: accountNameNotEmpty

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Kullanici adi alanına space degeri girilir ve update butonu disable kaldigi kontrol edilir

Para ekleme islemi yapilir
---------------------------
tags: addMoneyTest

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Islem yapilmadan once hesaptaki tutar hafizaya alinir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234 1234 1234" degeri girilir
* Para ekleme ekranina "catchyLabCardHolderInput" elementine "testinium" degeri girilir
* Para ekleme ekranina "catchyLabExpiryDateInput" elementine "1026" degeri girilir
* Para ekleme ekranina "catchyLabCVVInput" elementine "110" degeri girilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* Para ekle butonuna basilir
* İslem ozetindeki eklenen tutar "1.00" tutara esit mi
* Genel tutar eklenen para degeri ile eşit mi kontrol edilir

Kart numarasi 16 haneden fazla girilememesi
---------------------------
tags: moreThan16DigitsCannotBeEntered

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234 1234 1234 1234" degeri girilir
* "3" saniye bekle

Kart numarasi 8 haneyi kabul etmemesi
---------------------------
tags: dontAccept8Digits

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234" degeri girilir
* "catchyLabCardNumberTooShort" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Sisteme kayitli olmayan kart numarasi ile para ekleyememe kontrol
---------------------------
tags: wrongCardNumberInsert

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234 1234 1235" degeri girilir
* Para ekleme ekranina "catchyLabCardHolderInput" elementine "testinium" degeri girilir
* Para ekleme ekranina "catchyLabExpiryDateInput" elementine "1026" degeri girilir
* Para ekleme ekranina "catchyLabCVVInput" elementine "110" degeri girilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* "catchyLabMoneyAddAlert" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Tarihi gecmis kart bilgisi ile para ekleyememe kontrol
---------------------------
tags: wrongExpiredDateInsert

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234 1234 1234" degeri girilir
* Para ekleme ekranina "catchyLabCardHolderInput" elementine "testinium" degeri girilir
* Para ekleme ekranina "catchyLabExpiryDateInput" elementine "1012" degeri girilir
* Para ekleme ekranina "catchyLabCVVInput" elementine "110" degeri girilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* "catchyLabMoneyAddAlert" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Hatalı CVV girisi ile para ekleyememe kontrol
---------------------------
tags: wrongCVVInsert

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234 1234 1234" degeri girilir
* Para ekleme ekranina "catchyLabCardHolderInput" elementine "testinium" degeri girilir
* Para ekleme ekranina "catchyLabExpiryDateInput" elementine "1026" degeri girilir
* Para ekleme ekranina "catchyLabCVVInput" elementine "111" degeri girilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* "catchyLabMoneyAddAlert" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Negatif değer para girisi yapilamamasi kontrol
---------------------------
tags: negativeAmountInsert

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234 1234 1234" degeri girilir
* Para ekleme ekranina "catchyLabCardHolderInput" elementine "testinium" degeri girilir
* Para ekleme ekranina "catchyLabExpiryDateInput" elementine "1026" degeri girilir
* Para ekleme ekranina "catchyLabCVVInput" elementine "110" degeri girilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "-1" degeri girilir
* "catchyLabMoneyAddAlert" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Sifir degeri ile para ekleme islemi yapilamamasi kontrol
---------------------------
tags: zeroAmountInsert

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Para ekleme ekranina girilir ve ekran kontrolleri yapilir
* Para ekleme ekranindaki zorunlu alanlar kontrol edilir
* Para ekleme ekranina "catchyLabCardNumberInput" elementine "1234 1234 1234 1234" degeri girilir
* Para ekleme ekranina "catchyLabCardHolderInput" elementine "testinium" degeri girilir
* Para ekleme ekranina "catchyLabExpiryDateInput" elementine "1026" degeri girilir
* Para ekleme ekranina "catchyLabCVVInput" elementine "110" degeri girilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "0" degeri girilir
* "catchyLabMoneyAddAlert" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Transfer Money ekraninda amount alanina 0 girince send butonu disable kontrol
---------------------------
tags: zeroAmountInsertTransferMoney

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium1" secimi yapilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "0" degeri girilir
* "catchyLabEditAccountUpdateBtnDisable" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Transfer Money ekraninda amount alanina negatif deger girince send butonu disable kontrol
---------------------------
tags: zeroAmountInsertTransferMoney

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium1" secimi yapilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "-1" degeri girilir
* "catchyLabEditAccountUpdateBtnDisable" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula

Testinium-1 hesabina para gonderim kontrol
---------------------------
tags: transferMoneyTestinium1

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Islem yapilmadan once hesaptaki tutar hafizaya alinir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium1" secimi yapilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* Transfer Money send butonuna tiklanir
* Hesap ozetindeki Receiver Account "Testinium-1" ismi ile karsilastirilir
* İslem ozetindeki gonderilen tutar "1.00" tutara esit mi
* Genel tutar gonderilen para degeri ile eşit mi kontrol edilir

Testinium-2 hesabina para gonderim kontrol
---------------------------
tags: transferMoneyTestinium2

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Islem yapilmadan once hesaptaki tutar hafizaya alinir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium2" secimi yapilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* Transfer Money send butonuna tiklanir
* Hesap ozetindeki Receiver Account "Testinium-2" ismi ile karsilastirilir
* İslem ozetindeki gonderilen tutar "1.00" tutara esit mi
* Genel tutar gonderilen para degeri ile eşit mi kontrol edilir

Testinium-3 hesabina para gonderim kontrol
---------------------------
tags: transferMoneyTestinium3

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Islem yapilmadan once hesaptaki tutar hafizaya alinir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium3" secimi yapilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* Transfer Money send butonuna tiklanir
* Hesap ozetindeki Receiver Account "Testinium-3" ismi ile karsilastirilir
* İslem ozetindeki gonderilen tutar "1.00" tutara esit mi
* Genel tutar gonderilen para degeri ile eşit mi kontrol edilir

Testinium-4 hesabina para gonderim kontrol
---------------------------
tags: transferMoneyTestinium4

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Islem yapilmadan once hesaptaki tutar hafizaya alinir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium4" secimi yapilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* Transfer Money send butonuna tiklanir
* Hesap ozetindeki Receiver Account "Testinium-4" ismi ile karsilastirilir
* İslem ozetindeki gonderilen tutar "1.00" tutara esit mi
* Genel tutar gonderilen para degeri ile eşit mi kontrol edilir

Testinium-5 hesabina para gonderim kontrol
---------------------------
tags: transferMoneyTestinium4

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Islem yapilmadan once hesaptaki tutar hafizaya alinir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium5" secimi yapilir
* Para ekleme ekranina "catchyLabAmountInput" elementine "1" degeri girilir
* Transfer Money send butonuna tiklanir
* Hesap ozetindeki Receiver Account "Testinium-5" ismi ile karsilastirilir
* İslem ozetindeki gonderilen tutar "1.00" tutara esit mi
* Genel tutar gonderilen para degeri ile eşit mi kontrol edilir

Hesaptaki paradan fazla deger gonderilemez kontrolu
---------------------------
tags: extraMoneyCannotBeSend

* "ulas.camli@testinium.com" ve "158358Ulas" ile giris yapilir
* Uygulama icerisinde ki ekranlar kontrol edilir
* Para transfer ekranina gidilir
* Islem yapilmadan once hesaptaki tutar hafizaya alinir
* Transfer Money butonuna tiklanir ve ekranin acildigi kontrol edilir
* Sender Account secimi yapilir
* Receiver Account "catchyLabReceiverAccountTestinium1" secimi yapilir
* "catchyLabAmountInput" elementine hafizadaki değerin ustune "1" ekle
* "catchyLabEditAccountUpdateBtnDisable" elementinin gorunur oldugunu en fazla "3" saniye icinde dogrula



