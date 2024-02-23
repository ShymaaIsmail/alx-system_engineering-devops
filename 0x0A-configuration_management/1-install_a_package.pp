# Using Puppet, install flask from pip3 Install flask, Version must be 2.1.0
exec{'install flask from pip3':
  command => '/usr/bin/pip3 install Flask==2.1.0'
}
