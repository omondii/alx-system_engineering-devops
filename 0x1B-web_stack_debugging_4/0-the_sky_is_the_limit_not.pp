# Increasing nginx requests handling using puppet
exec {'requests_capacity':
  environment => ['DIR=/etc/default/nginx', 'OLD=15', 'NEW=4096'],
  command     => "sudo sed -i 's/\$OLD/\$NEW/' \$DIR",
  path        => ['/usr/bin', '/bin'],
}

exec {'limits_increase_1':
  environment => ['DIR=/etc/security/limits.conf', 'LIMITS_ENTRY=ngnix\\tsoft\\tnofile\\t30000'],
  command     => "sed -i -e '\$a\$LIMITS_ENTRY' \$DIR",
  path        => ['/usr/bin', '/bin'],
}

exec {'limits_increase_2':
  environment => ['DIR=/etc/security/limits.conf', 'LIMITS_ENRTY=nginx\\thard\\tnofile\\t50000'],
  command     => "sed -i -e '\$a\$LIMITS_ENTRY' \$DIR",
  path        => ['/usr/bin' ,'/bin'],
}
