#update limits of holberton user
# Define the ULIMIT value
$ulimit_value = '100000'
# Append Define soft and hard limit for holberton user
$file_content = "
# Define soft and hard limit for holberton user
holberton hard nofile 000
holberton soft nofile 00
"

# Ensure the file /etc/security/limits.conf exists and has specific content
file { '/etc/security/limits.conf':
  ensure  => file,
  content => $file_content,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
