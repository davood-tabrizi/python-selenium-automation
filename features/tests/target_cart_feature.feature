# Created by Davood at 2024-11-29
Feature: target cart feature test cases


  Scenario: verifies that “Your cart is empty” message is shown when user clicks on the cart icon
    Given Open target main page
    When  Click on cart icon, on the right side of the page
    Then  Verify 'Your cart is empty' message shown


  Scenario: verifies that user can add any Target’s product into the cart
    Given Open target main page
    When  Input tea into the search field
    When  Click on the search icon
    When  add an item of results to cart by Clicking on Add to cart button
    Then  verify the cart is not empty
