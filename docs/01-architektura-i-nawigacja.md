# 01. Architektura Informacji i Nawigacja

> **Standardy bazowe:** ISO 9241-110:2020 (Ergonomia interakcji człowiek-system), Nielsen Norman Group (NN/g), Rosenfeld & Morville (*Information Architecture for the World Wide Web*).

---

## 1. Architektura Informacji (Information Architecture - IA)

### 1.1. Modele Mentalne a Koncepcyjne
* **Zasada dopasowania do świata rzeczywistego (Jakob Nielsen, Heurystyka #2):** Struktura kategorii, nazewnictwo i relacje między obiektami muszą odzwierciedlać słownik użytkownika, a nie wewnętrzną strukturę organizacyjną firmy (unikanie tzw. *Org-Chart Navigation*).
* **Card Sorting & Tree Testing:**
  * **Otwarty Card Sorting:** Użytkownicy sami grupują karty i nadają nazwy kategoriom – stosowany we wczesnej fazie eksploracji.
  * **Zamknięty Card Sorting:** Użytkownicy przypisują elementy do zdefiniowanych z góry kategorii – służy do walidacji.
  * **Tree Testing:** Testowanie architektury bez szaty graficznej, z pomiarem wskaźnika sukcesu (Task Success Rate) i czasu na zadanie (Time on Task). Benchmark rynkowy: Task Success Rate $\ge 80\%$.

### 1.2. Prawa Kognitywne w Projektowaniu Nawigacji
* **Prawo Hicka-Hymana ($RT = b \cdot \log_2(n + 1)$):** Czas potrzebny na podjęcie decyzji rośnie logarytmicznie wraz z liczbą i złożonością dostępnych wyborów.
  * *Wytyczna:* Ogranicz liczbę elementów pierwszego rzędu w menu głównym do maksymalnie 5–7 pozycji.
  * *Zastosowanie:* W przypadku sklepów wielobranżowych stosuj tzw. *Progressive Disclosure* (stopniowe ujawnianie) za pomocą przemyślanych Mega Menu.
* **Prawo Millera ($7 \pm 2$):** Pamięć robocza człowieka mieści ograniczoną liczbę "porcji" (chunks) informacji.
  * *Wytyczna:* Grupuj pokrewne opcje logicznie za pomocą separatorów, nagłówków sekcji i kontrastów tła.
* **Prawo Jakoba (Jakob Nielsen):** Użytkownicy spędzają większość czasu na innych stronach internetowych, co oznacza, że oczekują od Twojej witryny działania zgodnego ze standardami, które już znają.
  * *Wytyczna:* Logo w lewym górnym rogu z linkiem do strony głównej, koszyk i profil w prawym górnym rogu, stopka z danymi kontaktowymi i prawnymi na dole.

---

## 2. Wzorce Projektowe Nawigacji (Navigation Patterns)

### 2.1. Nawigacja Główna (Primary / Global Navigation)
* **Widoczność (Visibility):**
  * Na desktopie kluczowe kategorie powinny być zawsze widoczne (unikać ukrywania nawigacji desktopowej pod ikoną hamburgera – wg badań NN/g zmniejsza to zaangażowanie w przeglądanie treści o ponad 40%).
* **Wskaźnik bieżącej lokalizacji (Current Location Indicator):**
  * Aktywna zakładka musi posiadać wyraźny wyróżnik wizualny (np. pogrubienie, zmiana koloru i podkreślenie min. 3px) oraz atrybut semantyczny dla technologii asystujących: `aria-current="page"`.
* **Sticky Header:**
  * W przypadku stron o długim przewijaniu (long-scroll), nagłówek powinien być przypięty do górnej krawędzi okna, redukując swoją wysokość o 20–30% podczas przewijania (tzw. slim sticky header).

### 2.2. Nawigacja Okruszkowa (Breadcrumbs)
* **Kiedy stosować:** Na wszystkich podstronach głębszych niż 1. poziom hierarchii.
* **Zasady implementacji:**
  * Umieszczenie: Bezpośrednio pod nagłówkiem głównym, a nad tytułem strony `<h1>`.
  * Ostatni element (bieżąca strona): Zwykły tekst, nieklikalny, wyróżniony lub oznaczony `aria-current="page"`.
  * Separator: Znak jednoznaczny wizualnie (np. `/` lub `›`), ukryty przed czytnikami ekranu za pomocą `aria-hidden="true"`.
  * Dane strukturalne: Wdrożenie mikrodanych Schema.org (`BreadcrumbList`) w formacie JSON-LD w celu optymalizacji widoczności w wynikach wyszukiwania Google (Rich Snippets).

```html
<!-- Przykład poprawnej implementacji Breadcrumbs (WCAG 2.2 & Schema.org) -->
<nav aria-label="Ścieżka powrotu (Breadcrumbs)">
  <ol class="breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/"><span itemprop="name">Strona główna</span></a>
      <span aria-hidden="true" class="separator">›</span>
      <meta itemprop="position" content="1" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <a itemprop="item" href="/zdrowie"><span itemprop="name">Zdrowie</span></a>
      <span aria-hidden="true" class="separator">›</span>
      <meta itemprop="position" content="2" />
    </li>
    <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
      <span itemprop="name" aria-current="page">Ciśnieniomierze</span>
      <meta itemprop="position" content="3" />
    </li>
  </ol>
</nav>
```

---

## 3. Wyszukiwarka i Nawigacja Fasetowa (Faceted Search)

### 3.1. Projekt Pola Wyszukiwarki (Search Box)
* **Widoczność i rozmiar:** Zgodnie z badaniami Baymard Institute, pole wyszukiwania powinno mieć szerokość umożliwiającą wprowadzenie co najmniej 27–30 znaków bez ukrywania tekstu.
* **Przycisk Submit:** Zawsze stosuj wyraźny przycisk tekstowy "Szukaj" lub ikonę lupy z alternatywnym tekstem dostępności (`aria-label="Szukaj w sklepie"`).
* **Autosugestie (Autocomplete / Search Suggestions):**
  * Uruchamianie po wpisaniu min. 2–3 znaków.
  * Grupowanie wyników: Podpowiedzi haseł, bezpośrednie produkty oraz powiązane kategorie.
  * Wyróżnienie wpisanej frazy (np. pogrubienie pasujących liter).
  * Tolerancja błędów (Typo-tolerance): Algorytm odległości Levenshteina obsługujący popularne literówki (np. "cisnieniomież" $\rightarrow$ "ciśnieniomierz").

### 3.2. Filtrowanie i Fasetowanie (Filtering & Facets)
* **Wybór wielokrotny (Multi-select):** Użytkownik musi mieć możliwość zaznaczenia kilku filtrów w ramach jednej grupy cech (np. producent A i producent B) bez natychmiastowego przeładowywania całej strony.
* **Licznik wyników:** Przy każdym parametrze filtra powinna znajdować się liczba pasujących produktów, dynamicznie aktualizowana (np. `Omron (14)`).
* **Zarządzanie stanem aktywnych filtrów:**
  * Sekcja "Wybrane filtry" (Active Filters Chips) umieszczona nad listingiem z opcją usunięcia pojedynczego filtra oraz przyciskiem "Wyczyść wszystkie".
  * Zachowanie filtrów w adresie URL jako parametrów zapytania (Query Params) – umożliwia dodanie do zakładek i powrót przyciskiem "Wstecz" przeglądarki.

---

## 📚 Źródła i Literatura Referencyjna
1. **Nielsen Norman Group (NN/g):** *Menu Design: Checklist of 15 UX Guidelines*, *Breadcrumbs: 11 Design Guidelines for Desktop and Mobile*.
2. **Baymard Institute:** *E-Commerce Search UX: 466 Usability Guidelines*, *Faceted Search Best Practices*.
3. **Peter Morville, Louis Rosenfeld:** *Information Architecture for the World Wide Web: Designing for the Web and Beyond*, O'Reilly Media.
4. **ISO 9241-110:2020:** *Ergonomics of human-system interaction — Part 110: Interaction principles*.
