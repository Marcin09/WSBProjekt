Feature: login
  Scenario: Logowanie na konto administracyjne bez wypelnienia pol formularza

    Given Uzytkownik wchodzi na strone logowania negativ
    When  Uzytkownik nie wypelnia pol formularza
    Then  Uzytkownik probuje zalogowac sie do panelu

