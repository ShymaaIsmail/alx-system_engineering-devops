# Using Puppet, install flask from pip3 Install flask, Version must be 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
