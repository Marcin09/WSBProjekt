Feature: login
    Scenario: Logowanie na konto administracyjne, wejscie do zakladki ksiazka adresowa


      Given Uzytkownik wchodzi na strone logowania KA
      When  Uzytkownik loguje sie na konto administracyjne i wchodzi do zakladki KA
      Then  Uzytkownik widzi Ksiazke Adresowa

