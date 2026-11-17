# 02. Dostępność Cyfrowa (Web Content Accessibility Guidelines - WCAG 2.2)

> **Standardy bazowe:** W3C Recommendation (WCAG 2.2 - opublikowane 5 października 2023 r.), Europejski Akt o Dostępności (EAA / Dyrektywa 2019/882), Ustawa o dostępności cyfrowej stron internetowych i aplikacji mobilnych podmiotów publicznych.

---

## 1. Cztery Filary Dostępności (Zasady P.O.U.R.)

1. **Postrzegalność (Perceivable):** Informacje oraz elementy interfejsu użytkownika muszą być przedstawione w sposób dostępny dla zmysłów użytkownika (wzrok, słuch, dotyk).
2. **Funkcjonalność (Operable):** Elementy interfejsu i nawigacja muszą być możliwe do obsłużenia przez każdego (pełna obsługa klawiaturą, brak pułapek czasowych, ochrona przed atakami padaczkowymi).
3. **Zrozumiałość (Understandable):** Informacje oraz obsługa interfejsu muszą być jasne, logiczne i przewidywalne.
4. **Solidność (Robust):** Treść musi być wystarczająco solidna, aby mogła być interpretowana przez różnorodne technologie asystujące (screen readery, powiększalniki, oprogramowanie sterowane głosem).

---

## 2. Kluczowe Kryteria Sukcesu WCAG 2.2 (Poziom A i AA)

### 2.1. Kontrast Kolorystyczny i Wizualny
* **Kryterium 1.4.3 Kontrast (Minimalny) [Poziom AA]:**
  * Tekst standardowy (< 18pt / < 24px lub < 14pt bold): Współczynnik kontrastu pomiędzy tekstem a tłem musi wynosić minimum **4.5:1**.
  * Duży tekst ($\ge$ 18pt / $\ge$ 24px lub $\ge$ 14pt / $\ge$ 18.5px bold): Minimalny kontrast wynosi **3.0:1**.
* **Kryterium 1.4.6 Kontrast (Wzmocniony) [Poziom AAA]:**
  * Tekst standardowy: Minimum **7.0:1**.
  * Duży tekst: Minimum **4.5:1**.
* **Kryterium 1.4.11 Kontrast elementów nietekstowych [Poziom AA]:**
  * Komponenty interfejsu (ramki inputów, przyciski, ikony funkcjonalne) oraz stany wizualne (focus, hover, selection) muszą mieć kontrast minimum **3.0:1** względem przyległych kolorów.
* **Kryterium 1.4.1 Użycie koloru [Poziom A]:**
  * Kolor nie może być jedynym środkiem wizualnym przekazującym informację, wskazującym akcję lub wyróżniającym element (np. link w bloku tekstu musi mieć podkreślenie; błąd w formularzu musi posiadać ikonę lub tekst wyjaśniający, a nie tylko czerwoną ramkę).

### 2.2. Obsługa Klawiaturą i Nowości WCAG 2.2
* **Kryterium 2.1.1 Klawiatura [Poziom A]:**
  * Wszystkie funkcjonalności serwisu muszą być dostępne przy użyciu wyłącznie klawiatury (klawisze `Tab`, `Shift+Tab`, `Enter`, `Space`, strzałki, `Esc`).
* **Kryterium 2.1.2 Brak pułapki na klawiaturę [Poziom A]:**
  * Kursor klawiatury nie może zostać uwięziony wewnątrz komponentu (np. w oknie modalnym lub odtwarzaczu wideo). Klawisz `Esc` musi zawsze zamykać okno modalne i przywracać fokus na element wyzwalający.
* **Kryterium 2.4.7 Widoczny fokus [Poziom AA]:**
  * Każdy interaktywny element w stanie skupienia (focus) musi posiadać wyraźny wskaźnik wizualny. Bezwzględny zakaz stosowania reguły `outline: none;` bez zdefiniowania alternatywnego stylu skupienia!
* **Kryterium 2.4.11 Fokus nieprzesłonięty (Minimalny) [NOWOŚĆ WCAG 2.2 - Poziom AA]:**
  * Gdy element otrzymuje fokus klawiatury, nie może być całkowicie zasłonięty przez treść utworzoną przez autora (np. przez sticky header, pasek ciasteczek cookies, pływające banery czy czatbota).
* **Kryterium 2.4.13 Widoczny wygląd fokusa [NOWOŚĆ WCAG 2.2 - Poziom AAA]:**
  * Wskaźnik fokusa musi mieć powierzchnię o grubości co najmniej 2px na obwodzie oraz kontrast co najmniej 3:1 między stanem skupionym a nieskupionym.

```css
/* Wzorcowa implementacja dostępnego focus ring zgodnego z WCAG 2.2 */
:focus-visible {
  outline: 3px solid #005A9C; /* Wysoki kontrast */
  outline-offset: 3px;        /* Odsunięcie od krawędzi komponentu */
  border-radius: 2px;
}
```

### 2.3. Rozmiar Celu Dotykowego i Interaktywnego
* **Kryterium 2.5.8 Rozmiar celu (Minimalny) [NOWOŚĆ WCAG 2.2 - Poziom AA]:**
  * Wielkość celu klikalnego (link, przycisk, checkbox) musi wynosić co najmniej **$24 \times 24$ piksele CSS**, chyba że:
    * Między krawędziami sąsiadujących elementów zachowany jest bufor odległości zapewniający średnicę okręgu 24px,
    * Element znajduje się w linii tekstu (inline text link),
    * Rozmiar wynika z natywnego wyglądu kontrolki przeglądarki.
* *Dobra praktyka UX (zgodna z Apple HIG & Google Material):* Mimo wymogu prawnego 24px, dla urządzeń mobilnych zalecany rozmiar fizyczny to min. **$44 \times 44\text{px}$ (Apple)** lub **$48 \times 48\text{px}$ (Google)**.

### 2.4. Ułatwienia Kognitywne w WCAG 2.2
* **Kryterium 3.3.7 Powtórzone wprowadzanie danych (Redundant Entry) [NOWOŚĆ WCAG 2.2 - Poziom A]:**
  * Informacje wprowadzone przez użytkownika w jednym kroku procesu (np. adres do faktury w checkout) muszą być automatycznie uzupełniane w kolejnych krokach lub dostępne do wyboru (np. checkbox: "Adres dostawy taki sam jak bilingowy"), aby nie zmuszać użytkownika do ponownego wpisywania tych samych danych.
* **Kryterium 3.3.8 Dostępne uwierzytelnianie (Minimalne) [NOWOŚĆ WCAG 2.2 - Poziom AA]:**
  * Proces logowania nie może opierać się wyłącznie na kognitywnym teście sprawnościowym (np. zapamiętywanie hasła bez możliwości wklejenia go ze schowka/menedżera haseł, rozwiązywanie łamigłówek matematycznych, przepisywanie skomplikowanych kodów CAPTCHA). Dopuszczalne: logowanie jednorazowym linkiem (magic link), menedżery haseł, biometria (WebAuthn / Passkeys), kody SMS.

---

## 3. Dostępna Semantyka i WAI-ARIA

### 3.1. Złota Zasada ARIA (First Rule of ARIA)
> *"Jeśli możesz użyć natywnego elementu HTML5 o odpowiedniej semantyce i zachowaniu, zrób to zamiast dodawać `role` i atrybuty ARIA."* (W3C WAI)
* Zamiast `<div role="button" tabindex="0">` używaj `<button type="button">`.

### 3.2. Komunikacja Zmian Dynamicznych (`aria-live`)
* W przypadku dynamicznego dodawania produktów do koszyka, filtrowania listy bez przeładowania lub pojawiania się toastów:
  * `aria-live="polite"`: Czytnik ekranu dokończy czytanie bieżącej frazy, zanim ogłosi komunikat (zalecane dla powiadomień o sukcesie, filtrach).
  * `aria-live="assertive"`: Przerywa bieżące czytanie w celu natychmiastowego ogłoszenia krytycznego błędu.

```html
<!-- Dostępny kontener powiadomień (Toast notification) -->
<div class="toast-container" aria-live="polite" aria-atomic="true">
  <div class="toast success" role="status">
    <span class="icon" aria-hidden="true">✓</span>
    <p>Produkt "Ciśnieniomierz M3" został pomyślnie dodany do koszyka.</p>
  </div>
</div>
```

---

## 📚 Źródła i Literatura Referencyjna
1. **W3C WAI:** *Web Content Accessibility Guidelines (WCAG) 2.2* (W3C Recommendation 2023).
2. **WebAIM (Accessibility in Mind):** *WCAG 2.2 Checklist*, *Contrast and Color Accessibility Guide*.
3. **Deque Systems:** *The WCAG 2.2 Guide & Reference*, *Axe-core Accessibility Engine*.
4. **European Accessibility Act (EAA):** *Directive (EU) 2019/882 of the European Parliament*.
