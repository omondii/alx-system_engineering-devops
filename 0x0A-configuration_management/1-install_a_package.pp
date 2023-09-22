# Install flask based on set attributes
# Flask needs py and pip3. Ensure they are already installed
package {'python3':
  ensure => installed,
}

package { 'python3-pip':
  ensure => installed,
}

# Attributes for flask installation
# set env when using package managers - common practice
exec { 'Flask':
  command     => 'pip3 install flask==2.1.0',
  path        => ['/usr/bin', '/bin'],
  logoutput   => true,
  refreshonly => true,
  environment => ['LC_ALL=C'],
  unless      => 'pip3 show flask',
}
