# Using Puppet, create a manifest that kills a process named killmenow. Must use the exec and pkill
exec{'pkill':
command  => '/usr/bin/pkill killmenow'
}
