# 06. Wydajność i Core Web Vitals (Performance UX)

> **Standardy bazowe:** Google Core Web Vitals (Oficjalne progi 2024+), Addy Osmani (*Patterns for Perceived Performance*), Nielsen Norman Group (NN/g - Tolerancja czasu oczekiwania użytkowników).

---

## 1. Wskaźniki Core Web Vitals (Google 2024+)

Doświadczenie wydajnościowe (Performance UX) jest kluczowym filarem zadowolenia użytkowników oraz pozycjonowania SEO. Od marca 2024 roku Google definiuje 3 oficjalne metryki Core Web Vitals:

```text
+--------------------------------------------------------------------------+
|                     CORE WEB VITALS BENCHMARKS (2024+)                   |
+---------------------+---------------------+------------------------------+
| Wskaźnik            | Dobry (Good)        | Wymaga poprawy / Słaby       |
+---------------------+---------------------+------------------------------+
| LCP (Ładowanie)     | ≤ 2.5 sekundy       | 2.5s – 4.0s  |  > 4.0s       |
| INP (Responsywność) | ≤ 200 milisekund    | 200ms – 500ms|  > 500ms      |
| CLS (Stabilność)    | ≤ 0.1               | 0.1 – 0.25   |  > 0.25       |
+---------------------+---------------------+------------------------------+
```

### 1.1. LCP (Largest Contentful Paint) – Szybkość Ładowania Treści Głównej
* Mierzy czas renderowania największego widocznego bloku treści (zazwyczaj zdjęcie w sekcji Hero na Landing Page lub zdjęcie produktu na karcie e-commerce).
* **Najczęstsze przyczyny słabego LCP:**
  * Niezoptymalizowane grafiki o wadze kilku megabajtów.
  * Blokowanie renderowania przez zewnętrzne skrypty JS i arkusze CSS.
  * Powolny czas odpowiedzi serwera (TTFB > 800ms).
* **Optymalizacje UX:**
  * Stosowanie nowoczesnych formatów kompresji: **AVIF** lub **WebP**.
  * Priorytetyzacja ładowania głównego zdjęcia (`fetchpriority="high"`):
    ```html
    <img src="cisnieniomierz-hero.webp" fetchpriority="high" alt="Ciśnieniomierz M3" width="800" height="600">
    ```

### 1.2. INP (Interaction to Next Paint) – Płynność Interakcji
* **Zastąpił metrykę FID (First Input Delay) w marcu 2024 r.**
* Mierzy całościowe opóźnienie reakcji interfejsu na dowolne działanie użytkownika (kliknięcie, stuknięcie, naciśnięcie klawisza) przez cały cykl życia sesji.
* **Cel UX:** Każda interakcja użytkownika musi dać natychmiastową wizualną odpowiedź w czasie **poniżej 200 ms** (np. zmiana stanu przycisku, animacja ripple, otwarcie szuflady).
* **Najczęstsze przyczyny słabego INP:**
  * Długie zadania JavaScript blokujące główny wątek (Long Tasks > 50ms).
  * Złożone ponowne obliczanie stylów (Recalculate Style) przy dużych drzewach DOM.

### 1.3. CLS (Cumulative Layout Shift) – Stabilność Wizualna
* Mierzy niespodziewane przesunięcia elementów strony podczas jej czytania lub klikania (np. nagłe pojawienie się banera reklamowego lub powolne załadowanie czcionki przesuwające przycisk pod palcem użytkownika).
* **Zasady eliminacji skoków układu:**
  1. Zawsze deklaruj atrybuty `width` i `height` lub właściwość CSS `aspect-ratio` dla wszystkich obrazów i wideo.
  2. Rezerwuj stałą przestrzeń (min-height) dla dynamicznych banerów, reklam i elementów powiadomień.
  3. Używaj właściwości `font-display: swap` z dopasowaniem metryk czcionki zastępczej (Font Fallback Matching) za pomocą narzędzi takich jak `@next/font` lub CSS `size-adjust`.

```css
/* Zapobieganie CLS dla dynamicznie ładowanych kontenerów */
.banner-slot {
  min-height: 250px;
  background-color: #f1f5f9;
  contain: layout;
}

img {
  aspect-ratio: 16 / 9;
  width: 100%;
  height: auto;
}
```

---

## 2. Perceived Performance (Postrzegana Wydajność)

Fizyczny czas ładowania strony różni się od tego, jak ten czas odczuwa człowiek:

### 2.1. Skeleton Screens vs Tradycyjne Spinnery
* Badania Nielsen Norman Group oraz Luke'a Wroblewskiego dowodzą, że:
  * Tradycyjny wirujący spinner (kręcące się kółko) skupia uwagę użytkownika na samym fakcie oczekiwania i sprawia, że proces wydaje się **o 30–40% dłuższy**.
  * **Ekrany szkieletowe (Skeleton Loaders):** Szare atrapy układu z delikatną animacją fali świetlnej (shimmer effect) symulują natychmiastowe załadowanie struktury strony, skupiając uwagę na nadchodzącej treści.

### 2.2. Optimistic UI (Optymistyczny Interfejs)
* Wzorzec projektowy polegający na natychmiastowym zaktualizowaniu interfejsu użytkownika (np. zmiana ikony serca na "ulubione", dodanie produktu do koszyka w liczniku nagłówka), **zanim serwer odeśle odpowiedź HTTP 200 OK**.
* W rzadkim przypadku błędu sieciowego (np. brak połączenia) stan interfejsu powraca do poprzedniego z dyskretnym powiadomieniem typu Toast ("Nie udało się zapisać zmian, spróbuj ponownie").

---

## 📚 Źródła i Literatura Referencyjna
1. **Google Web.dev:** *Core Web Vitals Guide (LCP, INP, CLS)*, Chrome Speed Team.
2. **Addy Osmani:** *Image Optimization*, *Patterns for Perceived Performance*, Google Chrome.
3. **Nielsen Norman Group (NN/g):** *Powers of 10: Time Scales in UX*, *Skeleton Screens vs. Loading Spinners*.
4. **W3C Web Performance Working Group:** *Navigation Timing & Paint Timing APIs*.
