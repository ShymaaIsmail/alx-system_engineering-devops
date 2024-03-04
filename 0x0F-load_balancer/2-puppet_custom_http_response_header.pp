# puupet custom http response header
# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        add_header  X-Served-By ${hostname};
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 http://example.com/;
    }

    error_page 404 /404.html;
    error_page 500 502 503 504 /50x.html;
    location = /50x.html {
        root /var/www/html;
    }
}
",
  notify  => Service['nginx'],
}

# Create index.html
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

# Restart Nginx when configuration changes
exec { 'nginx-reload':
  command     => '/usr/sbin/service nginx reload',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}
