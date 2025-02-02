# Web Otomasyon Test Framework'u

Bu proje, web uygulamaları için kapsamlı bir test otomasyon framework'üdür. Selenium ve gauge kullanarak yapılmıştır. 🚀

## Özellikler

•⁠  ⁠Fonksiyonel test otomasyonu
•⁠  ⁠BDD yaklaşımı (Gauge)
•⁠  ⁠Json yapısı ile elementleri isimlendirme

## 📋 Ön Gereksinimler

•⁠  ⁠Java JDK 11 veya üzeri
•⁠  ⁠Maven 3.7.0 veya üzeri
•⁠  ⁠Chrome/Firefox/Safari tarayıcı
•⁠  ⁠Gauge CLI
•⁠  ⁠Allure CLI

## Kurulum

1.⁠ ⁠Depoyu Klonlayın:
```
git clone https://github.com/ulascamli/QEDegerlendirme.git
```

2.⁠ ⁠Proje Dizini:
```
cd QEDegerlendirme
```
3.⁠ ⁠Bağımlılıkları Yükleyin:
```
mvn clean install
```

# Uygulamayı Başlatın
```
mvn clean test
```

## 📁 Proje Yapısı
```
src/
├── test/
│   ├── java/
│   │   └── com/
│   │       └── testinium/
│   │           ├── base/
│   │           │   ├── BasePage.java
│   │           │   └── BaseTest.java
│   │           ├── pages/
│   │           │   ├── LoginPage.java
│   │           │   └── ...
│   │           ├── step/
│   │           │   ├── LoginSteps.java
│   │           │   └── ...
│   │           └── utils/
│   │               ├── PerformanceUtil.java
│   │               ├── VisualUtil.java
│   │               └── AccessibilityUtil.java
│   └── resources/
│       ├── allure.properties
│       ├── environment.properties
│       └── categories.json
└── specs/
    └── example.spec
```

## 🔍 Test Yazma Rehberi

### Yeni bir test senaryosu ekleme:
specs klasöründe yeni bir .spec dosyası oluşturun

## 📝 Test Yazım Kuralları
- Her test için açıklayıcı isim kullanın
- Test metodlarına uygun annotation'ları ekleyin
- Allure için gerekli etiketleri ekleyin
- Her testin bağımsız çalışabildiğinden emin olun

## 📞 Destek
Sorularınız için:
- Issue açın
- Pull request gönderin
- Wiki sayfasını ziyaret edin

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.
