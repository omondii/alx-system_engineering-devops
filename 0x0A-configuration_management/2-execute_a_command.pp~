# A manifest that executes a pkill command
exec {'killmenow':
  command => 'pkill -f "killmenow"',
  onlyif => 'pgep -f "killmenow"',
  path => ['/usr/bin', '/bin'],
  logoutput => true,
  refreshonly => true,
}
