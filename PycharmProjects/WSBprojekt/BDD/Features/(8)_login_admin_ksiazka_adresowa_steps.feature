Feature: login
    Scenario: Zakladka tworzenie nowego pacjenta


      Given Uzytkownik wchodzi na strone administratora NP
      When  Uzytkownik wchodzi do zakladki KA
      When  Uzytkownik wchodzi do NP
      Then  Uzytkownik widzi formularz NP

