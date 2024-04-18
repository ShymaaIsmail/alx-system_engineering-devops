#update limit of etc default nginx 
exec { 'update-limit-of-etc-default-nginx ':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
# Restart Nginx when configuration changes
exec { 'nginx-reload':
  command     => '/usr/sbin/service nginx reload'
  }
