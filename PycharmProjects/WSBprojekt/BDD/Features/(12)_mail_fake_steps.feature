Feature: login
  Scenario: Stworzenie nowego pacjenta z niepoprawny forma mail

    Given Uzytkownik wchodzi na strone formularza NP form_12
    When  Uzytkownik wypelnia pola formularza, nieprawidlowy format email_12
    When  Uzytkownik klika na dodaj form_12
    Then  Uzytkownik widzi formularz NP form z komunikatami o putych polach_12

