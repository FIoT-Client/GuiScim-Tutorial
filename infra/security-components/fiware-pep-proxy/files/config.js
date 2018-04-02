var config = {};

// Used only if https is disabled
config.pep_port = 80;

// Set this var to undefined if you don't want the server to listen on HTTPS
config.https = {
    enabled: false,
    cert_file: 'cert/cert.crt',
    key_file: 'cert/key.key',
    port: 443
};

config.account_host = 'http://keyrock:8000';

config.keystone_host = 'keyrock';
config.keystone_port = 5000;

config.app_host = '10.7.49.180';  //config do app REST (TODO: inserir via ENV?)
config.app_port = '5056';
// Use true if the app server listens in https
config.app_ssl = false;

// Credentials obtained when registering PEP Proxy in Account Portal
config.username = 'pep_proxy_bf89166a7e7b4278a115e524e04e2c12';
config.password = '5201a5f576ff432ba8fbe52f9bfc4176';

// in seconds
config.cache_time = 300;

// if enabled PEP checks permissions with AuthZForce GE. 
// only compatible with oauth2 tokens engine
//
// you can use custom policy checks by including programatic scripts 
// in policies folder. An script template is included there
config.azf = {
    enabled: true,     //TESTES: reativar
    host: 'authzforce', //usar o nome do container (o --link cria a entrada no hosts)
    port: 8080,
    path: '/authzforce/domains/',
    custom_policy: undefined, // use undefined to default policy checks (HTTP verb + path).
    protocol: 'http'
};

// list of paths that will not check authentication/authorization
// example: ['/public/*', '/static/css/']
config.public_paths = [];

// options: oauth2/keystone
config.tokens_engine = 'oauth2';

config.magic_key = undefined;

module.exports = config;
