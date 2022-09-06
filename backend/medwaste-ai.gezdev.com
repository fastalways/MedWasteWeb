server {
	index index.php index.html index.htm index.nginx-debian.html;
	server_name medwaste-ai.gezdev.com;
	root /var/www/MedWasteWeb/frontend;
	
	location / {
		try_files $uri$args $uri$args/ /index.html;
	}
	
	charset utf-8;

	location ~ /\.ht {
		deny all;
	}

}
