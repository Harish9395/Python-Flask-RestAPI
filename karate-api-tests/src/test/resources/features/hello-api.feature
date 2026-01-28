Feature: Hello API Test

  Scenario: Get Hello
    # Remove 'karate.config.' - access 'baseUrl' directly
    Given url baseUrl + "/hello"
    When method get
    Then status 200
    And match response == { message: "Hello World" }
