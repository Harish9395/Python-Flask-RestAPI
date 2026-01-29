package com.example;

import com.intuit.karate.junit5.Karate;

class ExampleTest {

    @Karate.Test
    Karate runAll() {
        return Karate.run()
                     .relativeTo(getClass())
                     .parallel(5);
    }
}
