function fn() {
    var env = karate.env || 'dev'; // 'dev', 'qa', etc.
    karate.log('karate.env system property was:', env);

    var config = {};

    // Get base URL from environment variable, fallback to default
    config.baseUrl = java.lang.System.getenv('API_BASE_URL') 
                     || 'https://w54l7lppnl.execute-api.us-east-2.amazonaws.com/dev';
    karate.log('🔗 Using baseUrl:', config.baseUrl);

    // Optional auth token
    config.authToken = java.lang.System.getenv('AUTH_TOKEN') || '';

    return config;
}
