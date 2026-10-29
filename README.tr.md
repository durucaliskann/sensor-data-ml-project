# Sentetik Sensör Verileriyle Aşırı Yük Sınıflandırması

[English](README.md)

## Proje Hakkında

Türkiye Yapay Zeka Akademisi makine öğrenmesi eğitimi kapsamında tamamlanan final projesidir. Sentetik gerilim, akım ve sıcaklık verileriyle aşırı yük sınıflandırması ele alınır.

Veri kümesi deney amacıyla üretilmiştir; sahada çalışan fiziksel sensörlerden toplanmamıştır.

## Katkım

Bu teknik projeyi takım arkadaşımla birlikte tamamladım. Geliştirme ve değerlendirme çalışmalarını kendimiz gerçekleştirdik.

## İş Akışı

1. Eksik ve aykırı değerler içeren sentetik sensör verilerinin üretilmesi.
2. Verilerin temizlenmesi ve özniteliklerin hazırlanması.
3. Lojistik Regresyon, Random Forest ve Gradient Boosting modellerinin eğitilmesi ve karşılaştırılması.
4. Recall ve ROC-AUC ile sınıflandırma performansının değerlendirilmesi.

## Çalıştırma

Python kurulu bir ortamda, depo klasöründe:

```bash
python -m pip install -r requirements.txt
python veri_uret.py
python model_egit.py
```

Veri üretimi mevcut üretilmiş veri kümesinin üzerine yazabilir.

## Sınırlamalar

Değerlendirme sentetik veriyle sınırlıdır. Gerçek donanımdaki performansı veya gelecekteki aşırı yükün önceden tahmin edildiğini kanıtlamaz. Sonuçlar model, test örneği sayısı ve veri bölme yöntemiyle birlikte raporlanmalıdır.

## Durum

Tamamlanmış eğitim projesi.

