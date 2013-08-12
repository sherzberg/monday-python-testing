Exec['apt_update'] -> Package <| |>

exec {'apt_update':
  command => '/usr/bin/apt-get update',
}

package {'python-deps':
  name => ['python-pip', 'python3.3', 'pypy', 'jython'],
  ensure => present,
}

package {'pip-deps':
  name => ['tox', 'nose', 'coverage'],
  ensure => present,
  provider => pip,
  require => Package['python-deps'],
}
