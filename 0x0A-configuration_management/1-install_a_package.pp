# Installs flask from pip3

package { 'flask':
  ensure  => '2.1.0',
  command => '/usr/bin/pip3 install flask',
  path    => '/usr/bin',
}
