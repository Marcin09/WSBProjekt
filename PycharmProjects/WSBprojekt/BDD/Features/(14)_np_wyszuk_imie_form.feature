Feature: login
    Scenario: Szukanie pacjentow w KA


      Given Uzytkownik wchodzi na strone formularza NP form_14
      When  wyszukiwanie pacjenta imie NP form_14
      Then  Uzytkownik widzi formularz NP form_14

