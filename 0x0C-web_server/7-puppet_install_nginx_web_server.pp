# install nginx web server using puppet
# Define package and service for nginx
package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Enable and allow Nginx HTTP in UFW
class { 'ufw':
  before => Class['nginx'],
}

ufw::allow { 'Nginx HTTP':
  port   => 80,
  proto  => 'tcp',
  before => Service['nginx'],
}

# Create index.html and 404.html
file { '/var/www/html/index.html':
  content => 'Hello World!',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

file { '/var/www/html/404.html':
  content => "Ceci n'est pas une page",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html;
        server_name _;
        # Custom error pages
        error_page 404 /404.html;
        location / {
                try_files \$uri \$uri/ =404;
                rewrite ^/redirect_me/?$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
        }
        location = /404.html {
            internal;
        }
}",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}
