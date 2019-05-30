Feature: login
    Scenario: Logowanie na konto administracyjne, z pustym logiem


      Given Uzytkownik wchodzi na strone logowania negativ log
      When  Uzytkownik pole log pozostawia puste, w pole pass wpisuje poprawne haslo
      Then  Uzytkownik probuje zalogowac sie do panelu neg log

