---
name: ux-auditor
description: >-
  Przeprowadza kompleksowy audyt UX i dostępności cyfrowej (WCAG 2.2 AA) dla stron www, makiet UI,
  widoków e-commerce i aplikacji webowych za pomocą jednej komendy (/ux-audit). Kategoryzuje błędy wg wag (Blocker, Critical, Major, Minor) i generuje gotowy raport z fixami.
---

# 🤖 Autorski Skill: UX Auditor (/ux-audit)

Ten skill uczy agenta AI przeprowadzania ustrukturyzowanego, rygorystycznego audytu User Experience i dostępności cyfrowej (WCAG 2.2 Level AA/AAA) na podstawie 50-punktowej ujednoliconej matrycy.

---

## ⚡ Wyzwalacze (Triggers & Slash Command)

Agent powinien automatycznie aktywować ten skill, gdy:
* Użytkownik wpisze polecenie: `/ux-audit <url lub ścieżka do pliku/screena>`
* Użytkownik poprosi o audyt, np.: *"Przeprowadź audyt UX strony..."*, *"Sprawdź ten ekran pod kątem WCAG..."*, *"Oceń dostępność formularza..."*.

---

## 🛠️ Procedura Działania Krok po Kroku (Audit Protocol)

Gdy otrzymasz polecenie audytu, wykonaj następujące 5 kroków:

### Krok 1: Identyfikacja Obiektu i Definicja Persony Brzegowej
1. Jeśli podano URL: Skorzystaj z narzędzi przeglądarkowych lub inspekcji kodu, aby zbadać drzewo DOM, style i interakcje.
2. Jeśli podano plik HTML/CSS lub makietę SVG/obraz: Przeanalizuj hierarchię wizualną, kontrasty, etykiety i rozmiary kontrolek.
3. Przypisz profil **Persony Brzegowej** (np. senior ze słabszym wzrokiem i ograniczeniami motorycznymi, lub użytkownik mobile w pośpiechu), aby oceniać interfejs pod kątem realnych barier.

### Krok 2: Weryfikacja 8 Filarów Checklisty (50 Kryteriów)
Przeanalizuj interfejs przez pryzmat 8 modułów bazy wiedzy:
1. **Architektura & Nawigacja (IA):**
   * Sprawdź: liczbę elementów w menu (≤ 7 wg Prawa Hicka), obecność breadcrumbs, wyszukiwarkę z autosugestiami i fasetowanie AJAX.
2. **Dostępność WCAG 2.2 AA (A11Y):**
   * Sprawdź: kontrast tekstu (min. 4.5:1), widoczny wskaźnik fokusa (`:focus-visible`), nieprzesłonięty fokus (SC 2.4.11), minimalny cel dotykowy $24 \times 24\text{px}$ (SC 2.5.8), teksty alternatywne `alt` (SC 1.1.1).
3. **Typografia & Hierarchia (TYPO):**
   * Sprawdź: jeden tag `<h1>`, logiczną kolejność nagłówków, długość linii (45–75 znaków), wielkość fontu (min. 14px na mobile, min. 16px w polach).
4. **Formularze & Interakcje (FORM):**
   * Sprawdź: układ jednokolumnowy, trwałe etykiety nad polami (Top-aligned), atrybuty `autocomplete`, walidację inline on-blur, brak kasowania danych przy błędzie.
5. **Mobile & Touch UX (MOB):**
   * Sprawdź: strefę kciuka (Thumb Zone), cele dotykowe min. $44 \times 44\text{px}$, brak blokady zoomu (`user-scalable=no`).
6. **Wydajność & Web Vitals (PERF):**
   * Sprawdź: wymiary grafik (`width`/`height` zapobiegające CLS), obecność skeleton loaderów.
7. **Obsługa Błędów & Feedback (ERR):**
   * Sprawdź: jasne komunikaty błędu bez kodów HTTP, natychmiastową sugestię naprawy, opcję "Cofnij" (Undo).
8. **Etyka, Zaufanie & Dark Patterns (ETH):**
   * Sprawdź: brak automatycznie dodawanych produktów (*Sneak into Basket*), brak ukrytych kosztów (*Drip Pricing*), zgodność z cenami z 30 dni (Omnibus).

### Krok 3: Wyliczenie Wskaźnika UX Score (Algorytm Punktacji)
Rozpocznij z pulą **100 punktów bazowych**. Odejmuj punkty za każdą wykrytą usterkę według wag:
* 🔴 **BLOCKER:** `-15 punktów` (krytyczne bariery uniemożliwiające zakup, złamanie prawa UE, brak dostępu z klawiatury).
* 🟠 **CRITICAL:** `-8 punktów` (poważne utrudnienia, brak kontrastu tekstu, błędy formularzy).
* 🟡 **MAJOR:** `-4 punkty` (usterki ergonomiczne, brak autocomplete, mały font specyfikacji).
* 🟢 **MINOR:** `-1 punkt` (drobne nieścisłości wizualne, kosmetyka).

$$\text{Final UX Score} = \max \left( 0, 100 - \sum \text{Kary} \right)$$

* **Interpretacja wyniku:**
  * **90 – 100:** Doskonały UX i pełna dostępność (Klasa A).
  * **75 – 89:** Dobry poziom, drobne usterki do poprawy (Klasa B).
  * **50 – 74:** Wymaga pilnych poprawek w kluczowych obszarach (Klasa C).
  * **< 50:** Niedopuszczalny poziom barier; wysokie ryzyko prawne i biznesowe (Klasa F).

### Krok 4: Generowanie Ustrukturyzowanego Raportu
Sformatuj raport w Markdown z następującymi sekcjami:
1. **Podsumowanie i Wynik Punktowy (UX Score Card & Severity Counts)**
2. **Tabela Weryfikacji Kryteriów Checklisty**
3. **Katalog Znalezionych Błędów z Kodem Fix (Przed i Po)**
4. **Sprintowa Mapa Drogowa Napraw (P0 / P1 / P2)**

---

## 📋 Szablon Odpowiedzi Agenta

```markdown
# 🔍 Raport Audytu UX & WCAG 2.2: [Nazwa Widoku / URL]

## 📊 Wskaźnik Jakości: [WYNIK]/100 (Klasa: [A/B/C/F])
* 🔴 **Blocker:** [Liczba]
* 🟠 **Critical:** [Liczba]
* 🟡 **Major:** [Liczba]
* 🟢 **Minor:** [Liczba]

---

## 🚨 Wykryte Błędy i Proponowane Rozwiązania

### [IKONA WAGI] #[ID-BŁĘDU]: [Tytuł Usterki]
* **Waga:** [BLOCKER / CRITICAL / MAJOR / MINOR]
* **Kryterium:** [np. WCAG 2.2 SC 2.5.8 / Heurystyka #5 / Dyrektywa Omnibus]
* **Lokalizacja:** [Gdzie na ekranie]
* **Problem:** [Zwięzły opis z perspektywy użytkownika]
* **Proponowany FIX:**
  ```html
  <!-- Kod przed i po lub zalecenie projektowe -->
  ```

---

## 🗓️ Rekomendacja Sprintowa
* **Sprint P0 (Hotfix):** [Błędy Blocker i Critical]
* **Sprint P1 (Dostępność):** [Błędy Major]
* **Sprint P2 (Szlif UI):** [Błędy Minor]
```

---

## 📚 Źródła Referencyjne Skilla
* Baza wiedzy w repozytorium: `docs/checklist-kompletna.md`
* W3C Web Accessibility Guidelines 2.2
* Nielsen Norman Group 10 Usability Heuristics
* Baymard Institute E-Commerce Usability Research
