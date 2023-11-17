# Change the max user limit for an OS
exec {'Os confiig for user':
  environment => ['DIR=/etc/security/limits.conf',
                  'OLD=hard nofile 5', 'NEW=hard nofile 50000',
                  'OLD1=soft nofile 4', 'NEW1=soft nofile 40000'],
  command     => 'sudo sed -i "s/$OLD/$NEW/" $DIR; sudo sed -i "s/$OLD1/$NEW1/" $DIR',
  path        => ['/usr/bin', '/bin']
}
