package com.example;

import com.intuit.karate.junit5.Karate;

class ExampleTest {

    @Karate.Test
    Karate testAll() {
        // use "classpath:" to look in src/test/resources
        return Karate.run("classpath:features/hello-api.feature");
    }

}
