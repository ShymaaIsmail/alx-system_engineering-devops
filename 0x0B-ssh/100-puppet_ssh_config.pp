# configure some ssh options using puppet
class { 'ssh::server':
  options           => {
    'IdentityFile'             => '~/.ssh/school',
    'PasswordAuthentication'   =>  'no'
  },
}
