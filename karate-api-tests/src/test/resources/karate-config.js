function fn() {
    var env = karate.env; // 'dev', 'qa', etc.
    karate.log('karate.env system property was:', env);

    var config = {};

    // Base URL from GitHub Actions
    config.baseUrl = java.lang.System.getenv('API_BASE_URL');
    if (!config.baseUrl) {
        karate.log('❌ API_BASE_URL not set!');
        throw 'API_BASE_URL environment variable is required';
    }

    // Optional auth token
    config.authToken = java.lang.System.getenv('AUTH_TOKEN') || '';

    return config;
}
