# OS configuration so that it is possible to be  logined  with the holberton user and open a file without any error message.
exec { 'change-os-configuration-for-holberton-user':
  command => 'sed -i "s/holberton.*/holberton nofile unlimited/g" /etc/security/limits.conf',
  path    => ['/bin', 'usr/bin', 'usr/sbin']
}
