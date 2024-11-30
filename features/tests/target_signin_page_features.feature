# Created by Davood at 2024-11-29
Feature: Target sign-in page features
  # Enter feature description here

  Scenario: verify that a logged out user can navigate to Sign In
    Given Open target main page
    When  The user click on sign-in icon
    When  Click Sign In from right side navigation menu
    Then  Verify Sign In form opened