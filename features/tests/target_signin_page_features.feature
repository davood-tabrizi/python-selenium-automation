# Created by Davood at 2024-11-29
Feature: Target sign-in page features
  # Enter feature description here

  Scenario: verify that a logged out user can navigate to Sign In
    Given Open target main page
    When  The user click on sign-in icon
    When  Click Sign In from right side navigation menu
    Then  Verify Sign In form opened


  Scenario: User can open and close Terms and Conditions from sign in page
    Given  Open target main page
    When   The user click on sign-in icon
    When   Click Sign In from right side navigation menu
    When   Store original window
    When   Click on Target terms and conditions link
    When   Switch to the newly opened window
    Then  Verify Terms and Conditions page is opened
    Then  User can close new window and switch back to original


  Scenario: User get "We can't find your account." message when using wrong user name and password
    Given  Open target main page
    When   The user click on sign-in icon
    When   Click Sign In from right side navigation menu
    And    insert incorrect user name and password
    Then   verify user get 'Sorry, something went wrong. Please try again' message