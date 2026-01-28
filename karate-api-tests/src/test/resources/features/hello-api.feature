Feature: Test API Gateway Hello Endpoint

  Background:
    * url baseUrl
    * if (authToken) header Authorization = 'Bearer ' + authToken

  Scenario: Call /hello endpoint
    Given path 'hello'
    When method get
    Then status 200
    And match response == { message: '#string' }
