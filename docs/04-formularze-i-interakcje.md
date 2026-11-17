# 04. Formularze i Mikrointerakcje

> **Standardy bazowe:** Luke Wroblewski (*Web Form Design: Filling in the Blanks*), Baymard Institute (*Checkout Usability & Form Field Usability*), Caroline Jarrett & Gerry Gaffney (*Forms that Work*), Prawo Fittsa.

---

## 1. Ergonomia Układu Formularza (Form Layout)

### 1.1. Układ Jednokolumnowy vs Wielokolumnowy
* **Zasada pojedynczej ścieżki ukończenia (Single-column layout):**
  * Zgodnie z badaniami eye-trackingowymi Luke'a Wroblewskiego i Baymard Institute, formularze ułożone w **jednej pionowej kolumnie** są wypełniane średnio o **40% szybciej** i powodują o **30% mniej błędów** niż formularze wielokolumnowe.
  * Formularze wielokolumnowe zmuszają oko do zygzakowatego ruchu (Z-path), co zwiększa obciążenie poznawcze i prowadzi do przypadkowego pomijania pól.
  * *Wyjątek dopuszczalny:* Ściśle powiązane pola na jednej linii (np. "Imię" i "Nazwisko", "Kod pocztowy" i "Miejscowość", "Data ważności" i "CVV").

### 1.2. Umieszczenie Etykiet (Label Placement)
* **Etykiety nad polem (Top-aligned Labels) – ZŁOTY STANDARD:**
  * Wymagają tylko jednego ruchu gałek ocznych na pole (skanowanie z góry w dół w jednej pionowej linii).
  * Idealne na urządzenia mobilne, gdzie szerokość ekranu jest ograniczona.
* **Floating Labels (Pływające etykiety) – DLACZEGO ICH UNIKAĆ:**
  * Choć estetyczne, tworzą poważne bariery UX i dostępności:
    * Zmniejszają wielkość tekstu po kliknięciu do nieczytelnych 10–11px.
    * Często mają niski kontrast w stanie początkowym (< 3:1).
    * Użytkownik traci kontekst i pewność co do tego, co wpisuje.
    * Czytniki ekranu i automatyczne wypełniacze przeglądarek często generują błędy nakładania się tekstu na etykietę.
* **Placeholder nie zastępuje etykiety:**
  * Tekst zastępczy (`placeholder`) znika w momencie wpisywania pierwszego znaku. Jeśli użytkownik zapomni, co wpisywał, musi skasować całą zawartość pola, aby ponownie zobaczyć podpowiedź.

```html
<!-- Wzorcowa struktura pola formularza z pełną dostępnością -->
<div class="form-group">
  <label for="shipping-address" class="form-label">
    Ulica i numer domu <span class="required" aria-hidden="true">*</span>
  </label>
  <span id="shipping-address-hint" class="form-hint">Np. ul. Marszałkowska 10/12</span>
  <input 
    type="text" 
    id="shipping-address" 
    name="shipping_address" 
    class="form-input" 
    autocomplete="street-address" 
    required 
    aria-required="true"
    aria-describedby="shipping-address-hint" 
  />
  <div id="shipping-address-error" class="form-error" role="alert" aria-live="assertive" hidden>
    <span class="error-icon" aria-hidden="true">⚠️</span>
    <span class="error-text">Proszę podać prawidłowy adres wraz z numerem budynku.</span>
  </div>
</div>
```

---

## 2. Walidacja Danych i Konstrukcja Komunikatów Błędów

### 2.1. Moment Wyzwalania Walidacji (Timing)
* ❌ **Przedwczesna walidacja (Immediate on Keystroke):** Wyświetlanie błędu "Nieprawidłowy e-mail" w trakcie wpisywania pierwszych trzech liter wywołuje u użytkownika irytację i poczucie presji.
* ❌ **Spóźniona walidacja (Only on Submit):** Wyświetlanie listy 10 błędów na samej górze strony dopiero po kliknięciu "Kupuję i płacę", zmuszające do przewijania i ponownego szukania czerwonych pól.
* ✅ **Inline Validation on Blur (Złoty Standard):**
  * Sprawdzenie poprawności następuje w momencie, gdy użytkownik **opuszcza pole (zdarzenie `blur`)**.
  * Po pojawieniu się błędu, usunięcie komunikatu powinno nastąpić natychmiast (`on input`), gdy format stanie się poprawny, aby natychmiast nagrodzić użytkownika za naprawę błędu.

### 2.2. Automatyzacja i Redukcja Wysiłku (Autocomplete & Smart Defaults)
* **Atrybuty `autocomplete` (Kryterium WCAG 2.2 - 1.3.5 Identyfikacja celu wprowadzania):**
  * Zawsze deklaruj standardowe wartości autouzupełniania przeglądarek:
    * `autocomplete="name"` (Imię i nazwisko)
    * `autocomplete="email"` (Adres e-mail)
    * `autocomplete="tel"` (Numer telefonu)
    * `autocomplete="postal-code"` (Kod pocztowy)
* **Klawiatury wirtualne na urządzeniach mobilnych:**
  * `type="tel"` lub `inputmode="numeric"` dla numerów telefonów i kodów BLIK.
  * `type="email"` dla adresu e-mail.
  * `inputmode="decimal"` dla kwot pieniężnych i wag.

---

## 3. Prawo Fittsa i Przyciski CTA (Call to Action)

### 3.1. Równanie Fittsa
$$T = a + b \log_2 \left( \frac{2D}{W} \right)$$
Gdzie:
* $T$ = Czas potrzebny na naciśnięcie celu,
* $D$ = Dystans (Distance) kursora/palca do przycisku,
* $W$ = Szerokość (Width) celu klikalnego.

* **Wnioski dla projektantów:**
  1. Zwiększenie rozmiaru przycisku kluczowego (Primary CTA) skraca czas reakcji.
  2. Umieszczenie przycisku w łatwo dostępnym miejscu (np. Sticky CTA na dole ekranu smartfona) minimalizuje dystans $D$.
  3. Krawędzie ekranu mają "nieskończoną szerokość" na desktopie, co czyni rogi i brzegi naturalnymi kotwicami kliknięcia.

### 3.2. Stany Interaktywne Komponentów (Button States)
Każdy interaktywny przycisk musi posiadać 6 zdefiniowanych stanów wizualnych:
1. **Default:** Wyraźny kontrast z tłem (min. 3:1 dla obrysu, 4.5:1 dla etykiety).
2. **Hover:** Zmiana jasności o 10–15% po najechaniu kursorem + kursor `cursor: pointer`.
3. **Focus:** Wyraźna ramka fokusowa (outline min. 2–3px o wysokim kontraście).
4. **Active (Pressed):** Efekt wciśnięcia (skala 0.98 lub ciemniejsze wypełnienie).
5. **Loading:** Spinner zastępujący ikonę/tekst + `aria-busy="true"` + zablokowanie wielokrotnego kliknięcia.
6. **Disabled:** Wyblakły styl; *Uwaga UX:* Unikaj wygaszania przycisków submit bez wyjaśnienia, dlaczego przycisk jest nieaktywny! Lepszą praktyką jest aktywny przycisk, który po kliknięciu wskazuje brakujące pola.

---

## 📚 Źródła i Literatura Referencyjna
1. **Luke Wroblewski:** *Web Form Design: Filling in the Blanks*, Rosenfeld Media.
2. **Baymard Institute:** *Mobile & Desktop Checkout Usability Report (2024)*.
3. **Caroline Jarrett, Gerry Gaffney:** *Forms that Work: Designing Web Forms for Usability*, Morgan Kaufmann.
4. **Paul M. Fitts:** *The information capacity of the human motor system in controlling the amplitude of movement*, Journal of Experimental Psychology.
