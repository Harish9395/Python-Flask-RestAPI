package com.example;

import com.intuit.karate.junit5.Karate;

class ExampleTest {

    @Karate.Test
    Karate testAll() {
        // This automatically runs all feature files in src/test/resources
        return Karate.run().relativeTo(getClass());
    }

}
