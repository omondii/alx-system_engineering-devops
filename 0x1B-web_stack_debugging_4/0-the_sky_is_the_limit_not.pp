# Increasing nginx requests handling using puppet
exec {'requests_capacity':
  environment => ['DIR=/etc/default/nginx', 'OLD=15', 'NEW=15000'],
  command     => "sudo sed -i 's/\$OLD/\$NEW/' \$DIR; sudo service nginx restart",
  path        => ['/usr/bin', '/bin'],
}
