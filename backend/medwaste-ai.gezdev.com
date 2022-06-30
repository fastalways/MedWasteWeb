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

}