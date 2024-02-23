# Create file using puppet
file{'tmp_school':
path    => '/tmp/school',
owner   => 'www-data',
group   => 'www-data',
content => 'I love puppet',
mode    => '0744'
}
