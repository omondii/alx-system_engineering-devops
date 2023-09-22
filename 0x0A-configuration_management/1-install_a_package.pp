# Install flask based on set attributes
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
