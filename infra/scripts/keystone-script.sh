ADMIN_TOKEN=$(\
curl http://192.168.99.100:5000/v3/auth/tokens \
    -s \
    -i \
    -H "Content-Type: application/json" \
    -d '
{ "auth": {
    "identity": {
      "methods": ["password"],
      "password": {
        "user": {
          "name": "idm",
          "domain": { "id": "default" },
          "password": "idm"
        }
      }
    }
  }
}' | grep ^X-Subject-Token: | awk '{print $2}' )

echo $ADMIN_TOKEN 