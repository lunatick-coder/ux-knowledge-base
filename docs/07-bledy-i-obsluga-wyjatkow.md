# 07. Obsługa Błędów i Informacja Zwrotna (Error Handling & Feedback)

> **Standardy bazowe:** Jakob Nielsen (*10 Usability Heuristics for User Interface Design*), Don Norman (*The Design of Everyday Things*), Alan Cooper (*About Face: The Essentials of Interaction Design*).

---

## 1. Heurystyki Nielsena w Kontekście Błędów

Trzy z dziesięciu heurystyk Jakoba Nielsena odnoszą się bezpośrednio do komunikacji stanu systemu i obsługi sytuacji awaryjnych:

### 1.1. Heurystyka #1: Widoczność Stanu Systemu (Visibility of System Status)
* System powinien zawsze informować użytkowników o tym, co się dzieje, poprzez odpowiednią i terminową informację zwrotną.
* **Przykłady implementacji:**
  * Wskaźnik postępu (Progress Bar) w wielokrokowym formularzu zamówienia (np. "Krok 2 z 4: Dostawa i płatność").
  * Stan ładowania na przycisku CTA po kliknięciu ("Trwa przetwarzanie płatności...").
  * Powiadomienie o automatycznym zapisaniu wersji roboczej (Auto-save draft).

### 1.2. Heurystyka #5: Zapobieganie Błędom (Error Prevention)
* Znacznie lepsze od najlepszych komunikatów o błędach jest staranne zaprojektowanie interfejsu tak, aby błąd w ogóle nie mógł wystąpić.
* **Rozróżnienie wg Dona Normana:**
  * **Pomyłki (Slips):** Błędy wykonawcze wynikające z nieuwagi (np. literówka w numerze telefonu, przypadkowe kliknięcie obok przycisku).
    * *Zapobieganie:* Formatowanie pól w locie (maski wprowadzania dla numeru PESEL, kodu pocztowego, karty płatniczej), podpowiedzi w czasie rzeczywistym.
  * **Błędy merytoryczne (Mistakes):** Błędy wynikające z błędnego modelu mentalnego użytkownika (np. próba zamówienia leku na receptę bez załączenia kodu e-recepty).
    * *Zapobieganie:* Wyjaśnienie wymagań przed rozpoczęciem akcji, czytelne etykiety i ograniczenia wyboru (np. zablokowanie wyboru niedostępnych dat w kalendarzu).

### 1.3. Heurystyka #9: Pomagaj w Rozpoznawaniu i Naprawianiu Błędów
* Komunikaty o błędach powinny być formułowane w prostym języku (bez tajemniczych kodów programistycznych), precyzyjnie wskazywać problem i konstruktywnie sugerować rozwiązanie.

---

## 2. Anatomia Skutecznego Komunikatu Błędu

Każdy profesjonalny komunikat błędu musi składać się z 4 kluczowych elementów:

```text
+--------------------------------------------------------------------------+
| ⚠️  ANATOMIA KOMUNIKATU BŁĘDU (WZORZEC NN/g)                             |
+--------------------------------------------------------------------------+
| 1. Ikona & Kolor:         Wizualne ostrzeżenie (nie tylko sam kolor czerwony) |
| 2. Jasna przyczyna:       Zrozumiały język bez technicznego żargonu       |
| 3. Konstruktywny fix:     Precyzyjna instrukcja, jak naprawić błąd        |
| 4. Działanie 1-kliknięciem: Przycisk akcji naprawczej lub powrót         |
+--------------------------------------------------------------------------+
```

| Element | ❌ Zły przykład (Antywzorzec) | ✅ Dobry przykład (Wzorzec UX) |
| :--- | :--- | :--- |
| **Język / Ton** | `Błąd krytyczny: NullPointerException w polu 4.` | `Nie udało się przetworzyć numeru telefonu.` |
| **Konstruktywność** | `Niepoprawny format danych.` | `Numer telefonu powinien składać się z 9 cyfr, np. 500 123 456.` |
| **Ton emocjonalny** | `Podałeś zły kod pocztowy!` (obwinianie użytkownika) | `Kod pocztowy powinien mieć format XX-XXX (np. 00-950).` |
| **Dostępność** | Samodzielna czerwona ramka wokół inputu | Czerwona ramka (kontrast 3:1) + ikona ⚠️ + tekst błędu powiązany `aria-describedby` |

---

## 3. Odwracalność Akcji (Undo vs Potwierdzenia Modalne)

Alan Cooper w książce *About Face* zwraca uwagę, że ciągłe wyświetlanie modalnych okien dialogowych z pytaniem *"Czy na pewno chcesz to zrobić?"* uczy użytkowników bezrefleksyjnego klikania "Tak" (tzw. ślepota dialogowa):

* **Wzorzec "Undo" (Cofnij akcję):**
  * Zamiast blokować użytkownika oknem modalnym przy usuwaniu pozycji z koszyka lub listy ulubionych, usuń element natychmiast i wyświetl pasek informacyjny typu Snack/Toast:
    `"Produkt usunięty z koszyka. [ Cofnij ]"` (dostępny przez 8–10 sekund).
* **Kiedy okno modalne jest konieczne:**
  * Wyłącznie w przypadku akcji bezpowrotnie niszczących dane (np. trwałe usunięcie konta pacjenta, rezygnacja z opłaconego zamówienia) – z wyraźnym czerwonym przyciskiem destrukcyjnym i bezpiecznym przyciskiem "Anuluj" jako opcją domyślną (Escape).

---

## 4. Projektowanie Dostępnych Stron 404 i 500

Strona błędu 404 (Nie znaleziono strony) nie powinna być ślepym zaułkiem:
1. **Wyjaśnienie:** Poinformuj użytkownika przyjaznym tonem, że szukana strona zmieniła adres lub została usunięta.
2. **Wyszukiwarka:** Umieść aktywne pole wyszukiwarki bezpośrednio na środku strony 404.
3. **Pomocne linki:** Wyświetl 4–5 najpopularniejszych kategorii lub bezpośredni link do strony głównej.
4. **Kod stanu HTTP:** Upewnij się, że serwer zwraca rzeczywisty nagłówek `404 Not Found` (a nie `200 OK` z treścią błędu - tzw. Soft 404).

---

## 📚 Źródła i Literatura Referencyjna
1. **Jakob Nielsen:** *10 Usability Heuristics for User Interface Design*, Nielsen Norman Group.
2. **Don Norman:** *The Design of Everyday Things*, Revised and Expanded Edition, Basic Books.
3. **Alan Cooper, Robert Reimann, David Cronin:** *About Face: The Essentials of Interaction Design*, Wiley.
4. **Jennifer Tidwell, Charles Brewer, Aynne Valencia:** *Designing Interfaces: Patterns for Effective Interaction Design*, O'Reilly.
