# configure some ssh options using puppet
class { 'ssh::client':
  options           => {
    'IdentityFile'           => '~/.ssh/school',
    'PasswordAuthentication' =>  'no'
  },
}
