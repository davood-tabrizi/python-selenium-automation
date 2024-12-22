# Created by Davood at 2024-12-12
Feature: target search feature

  Scenario: user can search for tea
    Given  Open target main page
     When   Input tea into the search field
     When   Click on the search icon
     Then   Results for tea are shown


  Scenario Outline: user can search for a product in target search feature
     Given  Open target main page
     When   Input <product> into the search field
     When   Click on the search icon
     Then   Results for <expected_product> are shown
    Examples:
    |product     |expected_product   |
    |tea         |tea                |
    |coffee      |coffee             |
    |pen         |pen                |


