# A manifest that executes a pkill command
exec {'killmenow':
  command  => 'pkill killmenow',
  onlyif   => 'pgep killmenow',
  provider => shell,
}
