server {
    server_name medwaste-api.gezdev.com;

    location / {
    add_header Access-Control-Allow-Origin *;
	proxy_set_header   X-Forwarded-For $remote_addr;
        proxy_set_header   Host $http_host;
        proxy_pass         "http://127.0.0.1:5001";
    }

}
