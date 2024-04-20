# Debug nginx part 4
exec { 'web debug':
    command => 'sed -i s/15/4096/g /etc/default/nginx; service nginx restart',
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
