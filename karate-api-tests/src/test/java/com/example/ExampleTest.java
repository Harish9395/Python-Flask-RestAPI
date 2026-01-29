package com.example;

import com.intuit.karate.junit5.Karate;

class ExampleTest {

    @Karate.Test
    Karate testAll() {
        // Use feature path relative to this class
        return Karate.run("features/hello-api.feature").relativeTo(getClass());
    }

}
