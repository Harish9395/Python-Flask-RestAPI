package com.example;

import com.intuit.karate.junit5.Karate;

class ExampleTest {

    @Karate.Test
    Karate testAll() {
        return Karate.run("features/hello-api").relativeTo(getClass());
    }

}
