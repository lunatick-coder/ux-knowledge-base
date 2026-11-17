# Kompleksowa Checklista Audytowa UX & Dostępności Cyfrowej (50 Kryteriów)

> **Zastosowanie:** Praktyczna matryca weryfikacyjna dla audytorów UX, testerów QA, projektantów UI oraz automatycznych agentów AI.  
> **Klasyfikacja Wag (Severity):** 🔴 **BLOCKER** (Krytyczny) | 🟠 **CRITICAL** (Poważny) | 🟡 **MAJOR** (Średni) | 🟢 **MINOR** (Niski)

---

## 1. Architektura Informacji i Nawigacja (IA)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **IA-01** | Hierarchia Menu | Liczba głównych kategorii w menu desktopowym nie przekracza 7 elementów. | Prawo Hicka / Miller | 🟡 MAJOR | Manualna |
| **IA-02** | Lokalizacja | Użytkownik widzi wyraźny wskaźnik bieżącej strony (`aria-current="page"` + wizualny indykator). | NN/g / ISO 9241 | 🟠 CRITICAL | Manualna / DOM |
| **IA-03** | Okruszki | Breadcrumbs obecne na podstronach głębszych niż poziom 1, zgodne z mikrodanymi Schema.org. | NN/g / Google SEO | 🟡 MAJOR | Weryfikacja kodu |
| **IA-04** | Wyszukiwarka | Pole wyszukiwania mieści min. 27 znaków, obsługuje autosugestie i toleruje literówki (Levenshtein). | Baymard Institute | 🟠 CRITICAL | Test funkcjonalny |
| **IA-05** | Fasetowanie | Filtry umożliwiają wybór wielokrotny bez natychmiastowego przeładowania całej strony (AJAX/Fetch). | Baymard Institute | 🟠 CRITICAL | Test funkcjonalny |
| **IA-06** | Reset Filtrów | Dostępny przycisk "Wyczyść wszystkie filtry" oraz usuwanie pojedynczych chipsów. | Baymard Institute | 🟡 MAJOR | Manualna |
| **IA-07** | Powrót Home | Logo w lewym górnym rogu jest linkiem prowadzącym do strony głównej z atrybutem `alt`. | Prawo Jakoba / NN/g | 🔴 BLOCKER | Manualna |

---

## 2. Dostępność Cyfrowa (WCAG 2.2 AA / AAA)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A11Y-01** | Kontrast Tekstu | Kontrast tekstu do tła wynosi min. 4.5:1 (tekst zwykły) i 3.0:1 (tekst duży $\ge 24\text{px}$). | WCAG 2.2 SC 1.4.3 (AA) | 🔴 BLOCKER | Automatyczna (Axe) |
| **A11Y-02** | Kontrast UI | Kontrast elementów interfejsu (ramki inputów, ikony funkcyjne) wynosi min. 3.0:1. | WCAG 2.2 SC 1.4.11 (AA) | 🟠 CRITICAL | Analizator kontrastu |
| **A11Y-03** | Obsługa Klawiaturą | Wszystkie interaktywne komponenty są w pełni obsługiwane klawiszem `Tab`, `Enter`, `Space`, `Esc`. | WCAG 2.2 SC 2.1.1 (A) | 🔴 BLOCKER | Klawiatura manualna |
| **A11Y-04** | Brak Pułapki | Kursor klawiatury nie zostaje uwięziony wewnątrz komponentu (np. modal, wideo, menu). | WCAG 2.2 SC 2.1.2 (A) | 🔴 BLOCKER | Klawiatura manualna |
| **A11Y-05** | Widoczny Fokus | Element skupiony posiada wyraźną ramkę o wysokim kontraście (brak `outline: none`). | WCAG 2.2 SC 2.4.7 (AA) | 🔴 BLOCKER | Klawiatura manualna |
| **A11Y-06** | Fokus Nieprzesłonięty | Fokus klawiatury nie jest zasłonięty przez sticky header, pasek cookies czy modale. | WCAG 2.2 SC 2.4.11 (AA) | 🟠 CRITICAL | Klawiatura manualna |
| **A11Y-07** | Rozmiar Celu | Wielkość celu klikalnego wynosi co najmniej $24 \times 24\text{px}$ (z buforem odstępu). | WCAG 2.2 SC 2.5.8 (AA) | 🟠 CRITICAL | Inspekcja CSS |
| **A11Y-08** | Teksty Alternatywne | Wszystkie obrazy informacyjne posiadają precyzyjny `alt`, a ozdobne mają pusty `alt=""`. | WCAG 2.2 SC 1.1.1 (A) | 🟠 CRITICAL | Czytnik ekranu / DOM |
| **A11Y-09** | Zależność od Koloru | Informacje, błędy i statusy nie są sygnalizowane wyłącznie kolorem (wymagana ikona/tekst). | WCAG 2.2 SC 1.4.1 (A) | 🟠 CRITICAL | Test w skali szarości |
| **A11Y-10** | Unikanie Redundancji | Dane wpisane w jednym kroku (np. adres) są automatycznie przenoszone lub powielane na życzenie. | WCAG 2.2 SC 3.3.7 (A) | 🟡 MAJOR | Test procesu checkout |
| **A11Y-11** | Łatwe Logowanie | Logowanie nie wymaga pamięciowych testów kognitywnych; wspiera menedżery haseł i wklejanie. | WCAG 2.2 SC 3.3.8 (AA) | 🟠 CRITICAL | Test schowka / passkey |

---

## 3. Typografia i Hierarchia Wizualna (TYPO)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TYPO-01** | Hierarchia H1-H6 | Dokładnie jeden znacznik `<h1>` na widok; brak pomijania poziomów (np. H2 $\rightarrow$ H4). | W3C / SEO Best Practice | 🟡 MAJOR | Inspekcja DOM |
| **TYPO-02** | Długość Wiersza | Szerokość kolumny tekstu ciągłego mieści się w przedziale 45–75 znaków (`max-width: 65ch`). | Robert Bringhurst / NN/g | 🟡 MAJOR | Inspekcja CSS |
| **TYPO-03** | Interlinia | Wysokość linii (`line-height`) tekstu akapitowego wynosi od 1.4 do 1.6 wielkości czcionki. | WCAG 1.4.12 / Bringhurst | 🟡 MAJOR | Inspekcja CSS |
| **TYPO-04** | Minimalny Font | Rozmiar czcionki tekstu głównego wynosi min. 16px na desktopie i min. 16px w polach na mobile. | Apple HIG / Material 3 | 🟠 CRITICAL | Inspekcja CSS |
| **TYPO-05** | Prawo Bliskości | Odstęp etykiety do powiązanego pola jest mniejszy niż dystans do kolejnego modułu (Gestalt). | Gestalt Psychology | 🟢 MINOR | Weryfikacja wizualna |
| **TYPO-06** | Wyrównanie | Tekst ciągły wyrównany do lewej krawędzi (unikać justowania obustronnego tworzącego "rzeki"). | WCAG 1.4.8 / Butterick | 🟡 MAJOR | Weryfikacja wizualna |

---

## 4. Formularze i Interakcje (FORM)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **FORM-01** | Układ Jednokolumnowy | Pola formularza ułożone w jednej pionowej linii (z wyjątkiem pól ściśle skojarzonych). | Luke Wroblewski / Baymard | 🟠 CRITICAL | Weryfikacja układu |
| **FORM-02** | Etykiety Trwałe | Etykiety umieszczone trwale nad polami (Top-aligned); unikanie znikających placeholderów. | Baymard Institute / NN/g | 🟠 CRITICAL | Weryfikacja UX |
| **FORM-03** | Powiązanie Semantyczne | Każdy `<input>` posiada bezpośrednio powiązany znacznik `<label for="...">`. | WCAG 2.2 SC 1.3.1 (A) | 🔴 BLOCKER | Inspekcja kodu |
| **FORM-04** | Inline Walidacja | Sprawdzenie poprawności następuje po opuszczeniu pola (`on blur`), nie w trakcie pisania. | Luke Wroblewski | 🟡 MAJOR | Test interakcji |
| **FORM-05** | Autouzupełnianie | Wszystkie pola danych osobowych i adresowych posiadają atrybuty `autocomplete`. | WCAG 2.2 SC 1.3.5 (AA) | 🟠 CRITICAL | Inspekcja kodu |
| **FORM-06** | Typy Klawiatury | Prawidłowe atrybuty `inputmode="numeric"`, `type="email"`, `type="tel"` na urządzeniach mobile. | Apple HIG / Material 3 | 🟡 MAJOR | Test mobilny |
| **FORM-07** | Ochrona Danych | W przypadku błędu walidacji wprowadzone wcześniej dane w innych polach NIE są kasowane. | Jakob Nielsen (Heurystyka #5)| 🔴 BLOCKER | Test negatywny |
| **FORM-08** | Stany Przycisków | Przyciski posiadają stany: default, hover, focus, active, loading oraz disabled. | Design System Best Practice| 🟡 MAJOR | Weryfikacja CSS |

---

## 5. Mobile & Touch Ergonomics (MOB)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **MOB-01** | Strefa Kciuka | Główne przyciski akcji (Primary CTA) umieszczone w dolnej połowie ekranu w zasięgu kciuka. | Steven Hoober | 🟠 CRITICAL | Test na smartfonie |
| **MOB-02** | Rozmiar Celu Touch | Przyciski dotykowe mają fizyczny wymiar min. $44 \times 44\text{pt}$ (iOS) / $48 \times 48\text{dp}$ (Android). | Apple HIG / Google M3 | 🟠 CRITICAL | Pomiar w DevTools |
| **MOB-03** | Zoom Odblokowany | Brak atrybutów `user-scalable=no` i `maximum-scale=1.0` w znaczniku `<meta name="viewport">`. | WCAG 2.2 SC 1.4.4 (AA) | 🔴 BLOCKER | Inspekcja kodu |
| **MOB-04** | Przewijanie Poziome | Brak niepożądanego poziomego paska przewijania (horizontal scroll) przy szerokości 360–390px. | Google Mobile-Friendly | 🔴 BLOCKER | DevTools Device Mode |
| **MOB-05** | Zastąpienie Modali | Zastosowanie Bottom Sheets zamiast centrowanych okienek modalnych z małym krzyżykiem. | Mobile UX Patterns | 🟡 MAJOR | Weryfikacja UX |

---

## 6. Wydajność i Core Web Vitals (PERF)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PERF-01** | Szybkość LCP | Largest Contentful Paint osiągany w czasie poniżej 2.5 sekundy na łączu 4G. | Google Core Web Vitals | 🟠 CRITICAL | Lighthouse / PageSpeed |
| **PERF-02** | Czas Reakcji INP | Interaction to Next Paint nie przekracza 200 ms przy kluczowych interakcjach. | Google Core Web Vitals | 🟠 CRITICAL | Chrome DevTools INP |
| **PERF-03** | Skoki Układu CLS | Cumulative Layout Shift wynosi mniej niż 0.1 w trakcie całego cyklu ładowania i nawigacji. | Google Core Web Vitals | 🟠 CRITICAL | DevTools Layout Shifts |
| **PERF-04** | Wymiary Grafik | Wszystkie elementy `<img>` posiadają jawnie zadeklarowane atrybuty `width` i `height`. | Google Performance | 🟡 MAJOR | Inspekcja kodu |
| **PERF-05** | Perceived Performance | Użycie skeleton loaderów zamiast pustych ekranów lub agresywnych spinnerów. | NN/g / Addy Osmani | 🟡 MAJOR | Weryfikacja UX |

---

## 7. Obsługa Błędów i Feedback (ERR)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ERR-01** | Język Komunikatów | Komunikaty wyjaśniają przyczynę bez żargonu programistycznego i kodów błędów serwera. | Jakob Nielsen (Heurystyka #9)| 🟠 CRITICAL | Przegląd treści (Copy) |
| **ERR-02** | Akcja Naprawcza | Każdy komunikat błędu zawiera konkretną instrukcję lub przycisk natychmiastowej naprawy. | Don Norman / NN/g | 🟠 CRITICAL | Test scenariusza błędu |
| **ERR-03** | Odwracalność Akcji | Dostępna opcja "Cofnij" (Undo) po usunięciu pozycji z koszyka lub listy ulubionych. | Alan Cooper (About Face) | 🟡 MAJOR | Test funkcjonalny |
| **ERR-04** | Strona Błędu 404 | Strona 404 zawiera wyszukiwarkę, linki do kluczowych kategorii i poprawny nagłówek HTTP. | Google Search Central | 🟡 MAJOR | Test adresu URL |
| **ERR-05** | Komunikacja Sukcesu | Użytkownik otrzymuje jednoznaczne potwierdzenie wykonania akcji (Toast z `aria-live`). | Jakob Nielsen (Heurystyka #1)| 🟡 MAJOR | Test interakcji |

---

## 8. Etyka, Zaufanie i Dark Patterns (ETH)

| ID | Obszar | Kryterium Weryfikacyjne | Źródło Referencyjne | Waga Błędu | Metoda Testowa |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **ETH-01** | Brak Ukrytych Opłat | Pełny koszt zamówienia (wraz z dostawą) prezentowany przed przejściem do płatności. | Baymard / Dyrektywa UE | 🔴 BLOCKER | Test ścieżki checkout |
| **ETH-02** | Brak Sneak-in | Brak automatycznie zaznaczonych płatnych dodatków lub ubezpieczeń w koszyku. | Dyrektywa 2011/83/UE | 🔴 BLOCKER | Weryfikacja koszyka |
| **ETH-03** | Zgodność Omnibus | Wyświetlanie najniższej ceny z 30 dni przed wprowadzeniem promocji przy każdym produkcie. | Dyrektywa Omnibus (UE) | 🔴 BLOCKER | Inspekcja cen promo |
| **ETH-04** | Transparentność Firmy | Dane rejestrowe (NIP, adres, telefon, e-mail) łatwo dostępne w stopce lub zakładce kontakt. | EAA / Zaufanie konsumenckie| 🟠 CRITICAL | Weryfikacja stopki |
| **ETH-05** | Symetria Rezygnacji | Rezygnacja z subskrypcji/newslettera jest równie prosta jak zapis (brak Roach Motel). | Digital Services Act (DSA) | 🟠 CRITICAL | Weryfikacja konta |
| **ETH-06** | Neutralność Zgód | W banerze cookies przycisk "Odrzuć" ma taki sam rozmiar i kontrast jak "Akceptuj". | RODO / Wytyczne EDPB | 🟠 CRITICAL | Weryfikacja banera |
