Feature: login
  Scenario: Logowanie na konto administracyjne z uzyciem prawidlowych danych logowania

    Given Uzytkownik wchodzi na strone logowania
    When  Uzytkownik wypelnia pola formularza wlasciwymi danymi i loguje sie na konto
    Then  Uzytkownik wchodzi do panelu administracyjnego
