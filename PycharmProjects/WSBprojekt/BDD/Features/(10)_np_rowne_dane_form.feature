Feature: login
    Scenario: Stworzenie nowego pacjenta ,uzycie tych samych danych w formularzu


      Given Uzytkownik wypelnia pola formularza1 form2
      When  Uzytkownik wchodzi do zakladki NP form1 form2
      When  Uzytkownik klika na dodaj form2
      Then  Uzytkownik widzi formularz NP NP1 form2

