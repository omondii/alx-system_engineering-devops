# Ensure Nginx is installed and running
class { 'nginx':
  ensure => 'installed',
  enable => true,
}

# Define a custom Nginx configuration file for the custom header
file { '/etc/nginx/conf.d/custom_headers.conf':
  ensure  => 'present',
  content => "location / {
    add_header X-Served-By $hostname;
  }",
  notify  => Service['nginx'],
}

# Notify Nginx service to reload its configuration
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File['/etc/nginx/conf.d/custom_headers.conf'],
}
