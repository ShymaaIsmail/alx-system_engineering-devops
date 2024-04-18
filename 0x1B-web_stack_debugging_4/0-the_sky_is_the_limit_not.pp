#update limit of etc default nginx 
# Define the ULIMIT value
$ulimit_value = '100000'
# Generate the content for the nginx default configuration file
$file_content = "
# Additional options to pass to nginx
ULIMIT=\"-n ${ulimit_value}\"
"

# Ensure the file /etc/default/nginx exists and has specific content
file { '/etc/default/nginx':
  ensure  => file,
  content => $file_content,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
# Restart Nginx when configuration changes
exec { 'nginx-reload':
  command     => '/usr/sbin/service nginx reload'
  }
