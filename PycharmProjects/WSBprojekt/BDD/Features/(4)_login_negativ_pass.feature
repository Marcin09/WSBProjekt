Feature: login
    Scenario: Logowanie na konto administracyjne, z pustym pass


      Given Uzytkownik wchodzi na strone logowania negativ pass
      When  Uzytkownik wypelnia pole login, pole pass pozostaje puste
      Then  Uzytkownik probuje zalogowac sie do panelu neg pass

