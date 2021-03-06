server {
	index index.php index.html index.htm index.nginx-debian.html;
	server_name medwaste-ai.gezdev.com;
	root /home/ubuntu/MedWasteWeb/frontend;
	
	location / {
		try_files $uri$args $uri$args/ /index.html;
	}
	
	charset utf-8;

	location ~ /\.ht {
		deny all;
	}



    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/medwaste-ai.gezdev.com/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/medwaste-ai.gezdev.com/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}server {
    if ($host = medwaste-ai.gezdev.com) {
        return 301 https://$host$request_uri;
    } # managed by Certbot


	server_name medwaste-ai.gezdev.com;
    listen 80;
    return 404; # managed by Certbot


}