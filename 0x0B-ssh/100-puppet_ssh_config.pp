#!/usr/bin/env bash


file { '/home/jba/alx-system_engineering-devops/0x0B-ssh/sh_config':
  ensure  => 'file',
  mode    => '0600',
  content => "#!/usr/bin/env bash
  # SSH configuration file

  HostName 52.91.168.145
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no",
}
