# 05. Mobile UX i Responsywność (Touch & Responsive Design)

> **Standardy bazowe:** Steven Hoober (*Designing for Touch* / Badania ergonomii chwytu smartfona), Apple Human Interface Guidelines (HIG), Google Material Design 3, W3C Mobile Accessibility Guidelines.

---

## 1. Ergonomia Obsługi Dotykowej (Touch Ergonomics)

### 1.1. Strefa Kciuka (The Thumb Zone)
Badania empiryczne Stevena Hoobera (obejmujące ponad 1,3 miliona obserwacji użytkowników smartfonów) wykazały, że:
* **49%** użytkowników trzyma telefon i obsługuje go **jedną dłonią** (wyłącznie kciukiem).
* **36%** trzyma telefon w jednej dłoni i obsługuje go palcem wskazującym lub kciukiem drugiej ręki (tzw. chwyt *cradled*).
* **15%** obsługuje telefon oburącz (dwoma kciukami – najczęściej podczas pisania wiadomości).

W chwycie jednoręcznym ekran smartfona dzieli się na trzy strefy:
1. **Strefa naturalna (Natural Zone - Dół i środek ekranu):** Łatwo dostępna bez zmiany chwytu. Tutaj powinny znajdować się główne przyciski nawigacyjne, filtry, przyciski "Dodaj do koszyka" oraz zatwierdzenia formularza.
2. **Strefa sięgania (Reach Zone - Górna połowa środka):** Wymaga lekkiego naciągnięcia kciuka; odpowiednia dla treści czytanych i rzadziej używanych linków.
3. **Strefa trudna (Hard-to-Reach Zone - Górne rogi ekranu):** Wymaga zmiany pozycji całej dłoni lub użycia drugiej ręki. Umieszczaj tam jedynie akcje rzadkie lub destrukcyjne (np. "Anuluj", ustawienia zaawansowane, awatar profilu).

```text
+-------------------------+
|     [ TRUDNA / HARD ]   |  <-- Górne narożniki (Menu, Profil, Cancel)
|                         |
|   [ SIĘGANIE / REACH ]  |  <-- Treści informacyjne, opisy produktów
|                         |
|  [ NATURALNA / EASY ]   |  <-- Primary CTA ("Kup teraz"), Bottom Bar,
|   (Strefa Kciuka)       |      Tabs, Filtry, Koszyk
+-------------------------+
```

---

## 2. Standardy Rozmiarów Celów Dotykowych (Touch Targets)

Zjawisko "grubego palca" (Fat Finger Problem) powoduje, że opuszka ludzkiego palca pokrywa powierzchnię o średnicy od 10 do 14 mm:

| Standard / Instytucja | Minimalny rozmiar celu | Rekomendowany odstęp (Margin) | Zastosowanie |
| :--- | :--- | :--- | :--- |
| **Apple HIG (iOS)** | **$44 \times 44\text{ pt}$** | $\ge 8\text{ pt}$ | Przyciski, ikony, nawigacja w aplikacjach i na stronach mobilnych |
| **Google Material 3 (Android)** | **$48 \times 48\text{ dp}$** | $\ge 8\text{ dp}$ | Standardowe kontrolki UI, checkboxy, switche, floating action buttons |
| **W3C WCAG 2.2 (Poziom AA - 2.5.8)** | **$24 \times 24\text{ px}$** | $\ge 24\text{ px}$ okrąg wokół środka celu | Wymóg bezwzględny prawnie (minimalny) |

```css
/* Zapewnienie dostępnego rozmiaru celu dotykowego bez zmiany wyglądu ikony */
.icon-button {
  width: 20px;          /* Wizualny rozmiar ikony */
  height: 20px;
  position: relative;
}

/* Pseudo-element powiększający strefę klikalną do standardu 48x48px */
.icon-button::after {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  width: 48px;
  height: 48px;
  transform: translate(-50%, -50%);
}
```

---

## 3. Responsywność i Pułapki Mobile UX

### 3.1. Zakaz Blokowania Powiększania (Pinch-to-Zoom)
* 🔴 **BŁĄD KRYTYCZNY:** Stosowanie w tagu `<meta name="viewport">` atrybutów:
  `user-scalable=no`, `maximum-scale=1.0` lub `user-scalable=0`.
* **Dlaczego to błąd:** Całkowicie uniemożliwia osobom słabowidzącym i seniorom powiększenie drobnego tekstu lub szczegółów zdjęcia. Jest to bezpośrednie złamanie kryterium **WCAG 2.2 - 1.4.4 Zmiana rozmiaru tekstu (Poziom AA)**.
* **Prawidłowy tag:**
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  ```

### 3.2. Zapobieganie Niechcianemu Powiększeniu na iOS (Auto-Zoom Fix)
* Przeglądarka Safari na iOS automatycznie powiększa stronę po kliknięciu w pole `<input>`, jeśli wielkość fontu wynosi mniej niż **16px**.
* Powoduje to przesunięcie widoku poza krawędź i dezorientację użytkownika.
* *Rozwiązanie:* Wszystkie pola tekstowe, selecty i textarea na urządzeniach mobilnych muszą mieć zadeklarowany styl:
  ```css
  @media (max-width: 768px) {
    input, select, textarea {
      font-size: 16px !important; /* Blokuje automatyczny zoom Safari */
    }
  }
  ```

### 3.3. Wzorce Nawigacji: Bottom Sheets zamiast Modali
* Tradycyjne okna modalne wycentrowane na środku ekranu smartfona są trudne do zamknięcia (krzyżyk `X` znajduje się w strefie trudnej w prawym górnym rogu).
* **Rekomendacja:** Zastąp modale komponentem **Bottom Sheet** wysuwanym od dołu ekranu z możliwością zamknięcia gestem przeciągnięcia w dół (swipe down) lub dużym przyciskiem w strefie kciuka.

---

## 📚 Źródła i Literatura Referencyjna
1. **Steven Hoober:** *Designing for Touch: Best Practices for Touchscreens and Mobile Devices*, A List Apart & UXmatters.
2. **Apple Inc.:** *Human Interface Guidelines (HIG): Touch Targets and Layout*.
3. **Google Design:** *Material Design 3 - Layout & Touch Guidelines*.
4. **W3C:** *Mobile Accessibility: How WCAG 2.0 and Other W3C/WAI Guidelines Apply to Mobile*.
