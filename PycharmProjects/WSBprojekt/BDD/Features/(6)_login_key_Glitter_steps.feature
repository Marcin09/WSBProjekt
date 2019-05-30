Feature: login
    Scenario: Logowanie na konto administracyjne, z uzyciem duzych liter shift


      Given Uzytkownik wchodzi na strone logowania shift
      When  Uzytkownik wypelnia prawidlowo pola log i pass z wcisnietym shift
      When  Uzytkownik wciska klawisz ENTER, shift
      Then  Uzytkownik loguje sie na strone administratora shift

