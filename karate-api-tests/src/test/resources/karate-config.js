function fn() {
  // Base URL from environment (set by GitHub Actions or locally)
  var baseUrl = java.lang.System.getenv('API_BASE_URL') || 'https://<API_ID>.execute-api.us-east-1.amazonaws.com/dev';

  // Optional auth token (for secured APIs)
  var authToken = java.lang.System.getenv('AUTH_TOKEN') || null;

  karate.log('🟢 Karate config loaded. Base URL:', baseUrl);
  if (authToken) karate.log('🔑 Auth token detected');

  return {
    baseUrl: baseUrl,
    authToken: authToken
  };
}
