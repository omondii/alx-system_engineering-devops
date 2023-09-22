# A manifest that executes a pkill command
exec {'killmenow':
  command     => 'pkill killmenow',
  onlyif      => 'pgep killmenow',
  provider    => shell,
  path        => ['/usr/bin', '/bin'],
  logoutput   => true,
  refreshonly => true,
}
