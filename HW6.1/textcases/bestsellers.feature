Feature: Bestsellers 5 links matching correct page

  Scenario: Bestsellers 5links matching
    Given Open Amazon bestseller page
    Then Verify there are 5 links
    Then Verify User can click through top links and verify correct page opens
