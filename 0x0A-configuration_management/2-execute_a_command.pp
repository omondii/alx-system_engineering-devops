# A manifest that executes a pkill command
exec { 'killmenow':
  command  => 'pkill killmenow',
  onlyif   => 'pgrep killmenow',
  provider => shell,
}
