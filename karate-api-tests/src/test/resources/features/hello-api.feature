Feature: Hello API Test

  Scenario: Get Hello
    Given url karate.config.baseUrl + "/hello"
    When method get
    Then status 200
    And match response == { message: "Hello World" }
