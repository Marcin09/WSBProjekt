Feature: login
    Scenario: Logowanie na konto administracyjne, z uzyciem ENTER


      Given Uzytkownik wchodzi na strone logowania enter
      When  Uzytkownik wypelnia prawidlowo pola log i pass enter
      When  Uzytkownik wciska klawisz ENTER
      Then  Uzytkownik loguje sie na strone administratora

