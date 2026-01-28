function fn() {
    var config = {};
    config.baseUrl = java.lang.System.getenv('API_BASE_URL');
    if (!config.baseUrl) {
        karate.log('❌ API_BASE_URL not set!');
        throw 'API_BASE_URL environment variable is required';
    }
    config.authToken = java.lang.System.getenv('AUTH_TOKEN') || '';
    return config;
}
