# puppet manifest to change the limit of file descriptor

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
}

-> exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
