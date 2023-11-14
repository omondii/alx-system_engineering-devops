# Fix typo in wordpress settings file
exec { 'fix wordpres extension':
  environment => ['DIR=/var/www/html/wp-settings.php', 'OLD=phpp', 'NEW=php'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR',
  path        => ['/usr/bin', '/bin'],
}
