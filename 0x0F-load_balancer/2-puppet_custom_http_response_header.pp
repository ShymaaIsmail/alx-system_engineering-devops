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

# Execute hostname command to get the hostname
exec { 'get_hostname':
  command     => '/bin/hostname',
  logoutput   => true,
  refreshonly => true,
  unless      => "/bin/grep -q '^X-Served-By' /etc/nginx/sites-available/default",
  notify      => File['/etc/nginx/sites-available/default'],
}

# Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.conf.erb'),
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
