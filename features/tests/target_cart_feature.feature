# Created by Davood at 2024-11-29
Feature: target cart feature test cases


  Scenario: verifies that “Your cart is empty” message is shown when user clicks on the cart icon
    Given Open target main page
    When  Click on cart icon, on the right side of the page
    Then  Verify 'Your cart is empty' message shown