# 08. Etyka, Zaufanie i Dark Patterns (Deceptive Design)

> **Standardy bazowe:** Harry Brignull (*Deceptive Design / Dark Patterns*), Dyrektywa Parlamentu Europejskiego i Rady (UE) 2019/2161 (Dyrektywa Omnibus), Akt o Usługach Cyfrowych (DSA - Rozporządzenie UE 2022/2065), Baymard Institute (*Trust and Security in Checkout*).

---

## 1. Deceptive Design Patterns (Wzorce Zwodnicze / Dark Patterns)

Wzorce zwodnicze (wcześniej znane jako *Dark Patterns*) to techniki manipulacyjne w interfejsach cyfrowych, które skłaniają użytkownika do podjęcia działań niezgodnych z jego pierwotnym zamiarem, przynoszących korzyść wyłącznie właścicielowi serwisu:

```text
+--------------------------------------------------------------------------+
|            KLUCZOWE WZORCE ZWODNICZE WG HARRY'EGO BRIGNULLA              |
+---------------------+----------------------------------------------------+
| Wzorzec             | Mechanizm manipulacji                              |
+---------------------+----------------------------------------------------+
| Sneak into Basket   | Automatyczne dorzucanie do koszyka płatnej usługi  |
| Roach Motel         | Prosta rejestracja, skrajnie trudna rezygnacja     |
| Confirmshaming      | Wpędzanie w poczucie winy przy odrzuceniu oferty   |
| Drip Pricing        | Stopniowe ujawnianie ukrytych opłat w checkout     |
| Fake Scarcity       | Fałszywe liczniki czasu i sztuczna niska dostępność|
| Visual Interference | Maskowanie ważnych opcji za pomocą słabego kontrastu|
+---------------------+----------------------------------------------------+
```

### 1.1. Sneak into Basket (Ukradkowe dodawanie do koszyka)
* **Mechanizm:** Podczas finalizacji zakupu w koszyku automatycznie pojawia się dodatkowa pozycja (np. "Przedłużona gwarancja +19 zł", "Ubezpieczenie przesyłki +6 zł") z domyślnie zaznaczonym checkboxem.
* **Status prawny:** **NIELEGALNE w Unii Europejskiej** na mocy Dyrektywy o prawach konsumenta (2011/83/UE). Wszelkie płatne opcje dodatkowe muszą wymagać aktywnego i świadomego zaznaczenia (Opt-in) przez kupującego.

### 1.2. Roach Motel (Pułapka na karaluchy)
* **Mechanizm:** Dołączenie do usługi lub subskrypcji wymaga jednego kliknięcia (np. "Aktywuj pakiet Premium"), natomiast rezygnacja wymaga wykonania telefonu na infolinię czynną w określonych godzinach lub wysłania listu poleconego.
* **Zasada symetrii (Digital Services Act - DSA):** Proces rezygnacji z usługi musi być równie prosty, szybki i dostępny tą samą drogą, co proces jej zakupu (tzw. reguła 1-Click Cancel).

### 1.3. Confirmshaming (Szantaż emocjonalny)
* **Mechanizm:** Sformułowanie przycisku odrzucenia oferty w sposób deprecjonujący użytkownika lub wpędzający go w poczucie winy.
  * ❌ *Przykład:* Przycisk rabatu: "Chcę zniżkę 20%", przycisk odmowy: "Nie, dziękuję, wolę przepłacać i nie dbać o swoje zdrowie".
  * ✅ *Wzorzec etyczny:* "Nie, dziękuję" lub neutralny krzyżyk zamknięcia okna.

### 1.4. Drip Pricing (Kapanie ceną / Ukryte koszty)
* **Mechanizm:** Pokazywanie atrakcyjnej ceny na karcie produktu (np. 100 zł), a w ostatnim kroku płatności doliczanie niespodziewanych pozycji: opłata manipulacyjna, opłata serwisowa, obowiązkowe pakowanie, wysoki koszt dostawy.
* **Wpływ na biznes (Baymard Institute):** Aż **48% użytkowników porzuca koszyk** z powodu niespodziewanych dodatkowych kosztów ujawnionych dopiero w podsumowaniu!

---

## 2. Zgodność Prawna w UE (Compliance & Regulations)

### 2.1. Dyrektywa Omnibus (Ochrona przed fałszywymi promocjami)
* Każda informacja o obniżce ceny towaru lub usługi musi zawierać informację o **najniższej cenie tego towaru, która obowiązywała w okresie 30 dni przed wprowadzeniem obniżki** (lub od momentu rozpoczęcia sprzedaży, jeśli produkt jest oferowany krócej).
* **Wymóg UI:** Informacja o cenie z 30 dni musi być widoczna bezpośrednio przy cenie promocyjnej, czytelnym fontem (nie może być ukryta w tooltipie wymagającym hovera na mobile!).

### 2.2. Weryfikacja Opinii Konsumenckich
* Przedsiębiorca publikujący recenzje musi poinformować, czy i w jaki sposób zapewnia, aby publikowane opinie pochodziły od konsumentów, którzy rzeczywiście używali danego produktu lub go nabyli.
* Oznaczanie recenzji etykietą: "Opinia potwierdzona zakupem".

### 2.3. RODO i Zgody Marketingowe (GDPR Cookies & Consent)
* Zakaz stosowania domyślnie zaznaczonych checkboxów (pre-ticked boxes).
* Przycisk "Odrzuć wszystkie pliki cookie" w banerze zgód (Cookie Banner) musi być tak samo wyeksponowany wizualnie (ten sam rozmiar, kontrast, poziom hierarchii), jak przycisk "Zaakceptuj wszystkie".

---

## 3. Filary Budowania Zaufania w E-Commerce (Trust Signals)

Zgodnie z badaniami Baymard Institute, użytkownicy powierzający swoje dane wrażliwe (PESEL, dane karty płatniczej, historia leków) oczekują jednoznacznych sygnałów wiarygodności:

1. **Transparentność Danych Firmy:**
   * Łatwo dostępna zakładka kontaktowa zawierająca: pełną nazwę rejestrową spółki, NIP, REGON, KRS, fizyczny adres siedziby, bezpośredni telefon do biura obsługi oraz imię i nazwisko kierownika apteki / inspektora ochrony danych.
2. **Kalkulator Dostawy na Karcie Produktu:**
   * Możliwość sprawdzenia dokładnego kosztu i terminu dostawy przed dodaniem produktu do koszyka (np. "Wprowadź kod pocztowy, aby sprawdzić termin doręczenia").
3. **Bezpieczeństwo Płatności:**
   * Wyświetlanie oficjalnych logotypów zaufanych operatorów płatności (BLIK, Visa, Mastercard, Przelewy24, Apple Pay) z certyfikatem szyfrowania SSL (HTTPS).

---

## 📚 Źródła i Literatura Referencyjna
1. **Harry Brignull:** *Deceptive Design (formerly Dark Patterns)*, deceptive.design.
2. **Parlament Europejski:** *Dyrektywa (UE) 2019/2161 (Dyrektywa Omnibus)* oraz *Rozporządzenie (UE) 2022/2065 (Akt o Usługach Cyfrowych - DSA)*.
3. **Baymard Institute:** *Checkout Usability: Why Shoppers Abandon Their Carts (2024)*.
4. **European Data Protection Board (EDPB):** *Guidelines 03/2022 on Deceptive design patterns in social media platform interfaces*.
