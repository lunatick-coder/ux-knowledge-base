# 03. Typografia i Hierarchia Wizualna

> **Standardy bazowe:** Robert Bringhurst (*The Elements of Typographic Style*), Matthew Butterick (*Practical Typography*), Nielsen Norman Group (NN/g - Badania Eye-tracking), Google Material Design 3.

---

## 1. Ergonomia Typografii i Czytelność Tekstu (Readability)

### 1.1. Długość Wiersza Tekstu (Measure)
* **Złota reguła czytelności:** Optymalna długość linii dla tekstu ciągłego (artykuły, opisy produktów, regulaminy) wynosi **od 45 do 75 znaków** (wliczając spacje), z idealnym punktem odniesienia wynoszącym około **65 znaków**.
  * Zbyt długa linia (> 80–90 znaków) powoduje zmęczenie wzroku i problem z odnalezieniem początku kolejnego wiersza (tzw. zjawisko *doubling*).
  * Zbyt krótka linia (< 40 znaków) zmusza oko do częstego przeskakiwania i rozbija rytm czytania.
* **Implementacja w CSS:**
  ```css
  .article-body, .product-description {
    max-width: 65ch; /* 'ch' odpowiada szerokości cyfry '0' danego fontu */
    margin-inline: auto;
  }
  ```

### 1.2. Interlinia (Line Height) i Odstępy Międzyakapitowe
* **Współczynnik interlinii:**
  * Dla tekstu akapitowego (Body): **1.4 – 1.6** (140% – 160% wielkości fontu).
  * Dla dużych nagłówków (Display / H1): **1.1 – 1.25** (zbyt duża interlinia w nagłówkach rozbija zwartą strukturę tytułu).
* **Wymogi WCAG 2.2 (Kryterium 1.4.12 Dopasowanie tekstu):**
  Użytkownik musi mieć możliwość zmiany parametrów tekstu bez utraty zawartości lub funkcjonalności:
  * Wysokość linii co najmniej $1.5 \times$ wielkość fontu.
  * Odstęp po akapicie co najmniej $2 \times$ wielkość fontu.
  * Odstępy między literami (letter-spacing) co najmniej $0.12 \times$ wielkość fontu.
  * Odstępy między słowami (word-spacing) co najmniej $0.16 \times$ wielkość fontu.

### 1.3. Skale Modularne (Modular Scales)
Hierarchia wielkości powinna opierać się na geometrycznym współczynniku proporcji (np. Major Third 1.250 lub Perfect Fourth 1.333):

| Poziom / Token | Rozmiar (px/rem) | Przeznaczenie | Waga (Font Weight) |
| :--- | :--- | :--- | :--- |
| `display-1` | 48px / 3.0rem | Nagłówki kampanii, Landing page Hero | 700 (Bold) |
| `heading-1` (`<h1>`) | 32px / 2.0rem | Tytuł widoku / Nazwa produktu | 700 (Bold) |
| `heading-2` (`<h2>`) | 24px / 1.5rem | Główne sekcje (np. "Specyfikacja", "Opinie") | 600 (Semi-Bold) |
| `heading-3` (`<h3>`) | 20px / 1.25rem | Podsekcje, nagłówki kart produktów | 600 (Semi-Bold) |
| `body-default` | 16px / 1.0rem | Główny tekst interfejsu (Body standard) | 400 (Regular) |
| `body-small` | 14px / 0.875rem | Metadane, etykiety formularzy, pomoc | 400 / 500 (Medium) |
| `caption` | 12px / 0.75rem | Prawa autorskie, disclaimer (bezwzględne minimum) | 400 (Regular) |

> ⚠️ **Uwaga dotycząca dostępności:** Nigdy nie stosuj fontu mniejszego niż 12px na desktopie i 14px na urządzeniach mobilnych!

---

## 2. Modele Skanowania Wzrokowego (Eye-tracking Patterns)

Badania eye-trackingowe Nielsen Norman Group wykazały, że użytkownicy internetu rzadko czytają strony słowo w słowo – w 79% przypadków **skanują interfejs** w poszukiwaniu kotwic wzrokowych:

### 2.1. Wzorzec F (F-Shape Pattern)
* **Charakterystyka:** Występuje na stronach nasyconych tekstem bez wyraźnej hierarchii. Wzrok porusza się poziomo po górnej linii, następnie nieco niżej po krótszej linii, po czym opada pionowo wzdłuż lewej krawędzi.
* **Rekomendacja UX:**
  * Umieszczaj najważniejsze słowa kluczowe w pierwszych 2–3 wyrazach nagłówków i akapitów (tzw. *Front-loading*).
  * Stosuj listy punktowane i wytłuszczenia (bolding) kluczowych informacji.

### 2.2. Wzorzec Z (Z-Pattern)
* **Charakterystyka:** Typowy dla stron typu Landing Page, Hero Section lub prostych ekranów ofertowych o małej ilości tekstu. Wzrok przemieszcza się od lewego górnego rogu (Logo), do prawego górnego rogu (Nawigacja/CTA), po przekątnej do lewego dolnego rogu, i w prawo do głównego przycisku CTA.

### 2.3. Wzorzec Ciasta Warstwowego (Layer-Cake Pattern)
* **Charakterystyka:** Najbardziej efektywny model czytania. Użytkownik skanuje wyłącznie nagłówki sekcji (`<h2>`, `<h3>`), a w treść zagłębia się dopiero po odnalezieniu poszukiwanego zagadnienia.
* **Rekomendacja UX:**
  * Nagłówki muszą być opisowe i informatywne (zamiast "Więcej informacji" stosuj "Parametry techniczne i zasilanie").

---

## 3. Prawa Percepcji Gestalt w Projektowaniu UI

Zasady psychologii postaci (Gestalt) tłumaczą, jak mózg ludzki automatycznie organizuje pojedyncze bodźce w uporządkowane całości:

1. **Zasada Bliskości (Law of Proximity):**
   * Elementy znajdujące się blisko siebie są postrzegane jako powiązane ze sobą.
   * *Wytyczna w formularzach:* Odstęp między etykietą a powiązanym polem input powinien być co najmniej 2–3 razy mniejszy niż odstęp do kolejnego pola formularza!
2. **Zasada Podobieństwa (Law of Similarity):**
   * Elementy o tym samym kolorze, kształcie i wielkości są odbierane jako pełniące tę samą funkcję.
   * *Wytyczna w CTA:* Wszystkie przyciski o statusie podstawowym (Primary Action) muszą mieć ten sam styl wizualny; przyciski destrukcyjne (Usuń, Anuluj) muszą odróżniać się barwą (np. czerwień) i hierarchią (Outline/Ghost).
3. **Zasada Wspólnego Obszaru (Common Region):**
   * Elementy zamknięte wewnątrz wyraźnej granicy wizualnej (ramka, karta z cieniem, odmienny kolor tła) są traktowane jako odrębna grupa.
   * *Zastosowanie:* Karty produktów (Product Cards), boksy powiadomień, sekcje koszyka.

---

## 📚 Źródła i Literatura Referencyjna
1. **Nielsen Norman Group (NN/g):** *F-Shaped Pattern of Reading on the Web: Misunderstood, But Still Relevant*, *How People Read on the Web*.
2. **Robert Bringhurst:** *The Elements of Typographic Style*, Version 4.0, Hartley & Marks Publishers.
3. **Matthew Butterick:** *Butterick's Practical Typography* (practicaltypography.com).
4. **Google Material Design 3:** *Typography System & Readability Guidelines*.
