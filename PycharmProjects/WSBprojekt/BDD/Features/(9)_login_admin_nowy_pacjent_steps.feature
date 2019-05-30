Feature: login
    Scenario: Stworzenie nowego pacjenta


      Given Uzytkownik wypelnia pola formularza1
      When  Uzytkownik wchodzi do zakladki NP form1
      When  Uzytkownik klika na dodaj
      Then  Uzytkownik widzi formularz NP NP1

