Feature: login
    Scenario: Dodanie kolejnego nr tel w KA pacjenta

      Given Uzytkownik wchodzi na strone formularza NPP form_13
      When  Uzytkownik wypelnia pola formularza_13
      When  Uzytkownik klika na dodaj form_13
      Then  Uzytkownik widzi dodany nr w formularzu NP form_13

