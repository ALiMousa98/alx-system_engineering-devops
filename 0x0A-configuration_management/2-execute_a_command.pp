# This is a puppet manifest to kill a running process

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  refreshonly => true,
}
