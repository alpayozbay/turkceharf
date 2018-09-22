def trlower(metin):
    """
        Türkçe küçük harfe çevirir

        Python da katar veri tipi ile yüklü gelen küçük harfe çevirici lower fonksyionu I ve İ harflerini
        doğru çevrimez. trlower fonksiyonu bu hatayı çözmektedir.

        Parametre:
            metin: Küçük harfe çevrilecek metin

        Döndürdüğü Sonuç:
            Türkçe küçük harf hali

    """

    def trlower_(harf):
        if harf=='I': sonuç = 'ı'
        elif harf=='İ': sonuç = 'i'
        else: sonuç = harf.lower()
        return sonuç

    sonuç = ''
    for i in metin:
        sonuç += trlower_(i)

    return sonuç

def trupper(metin):
    """
        Türkçe büyük harfe çevirir

        Python da katar veri tipi ile yüklü gelen büyük harfe çevirici upper fonksyionu I ve İ harflerini
        doğru çevrimez. trupper fonksiyonu bu hatayı çözmektedir.

        Parametre:
            metin: Büyük harfe çevrilecek metin

        Döndürdüğü Sonuç:
            Türkçe büyük harf hali

    """

    def trupper_(harf):
        if harf=='ı': sonuç = 'I'
        elif harf=='i': sonuç = 'İ'
        else: sonuç = harf.upper()
        return sonuç

    sonuç = ''
    for i in metin:
        sonuç += trupper_(i)

    return sonuç
