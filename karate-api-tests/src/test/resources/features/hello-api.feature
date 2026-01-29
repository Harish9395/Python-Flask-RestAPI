@smoke @hello
Feature: Hello API Test

Background:
  * url baseUrl

@positive
Scenario: Get Hello - success
  Given path 'hello'
  When method GET
  Then status 200
  And match response.message == "Hello from Karate API"

@negative
Scenario: Get Hello - invalid endpoint
  Given path 'hello-invalid'
  When method GET
  Then status 404
