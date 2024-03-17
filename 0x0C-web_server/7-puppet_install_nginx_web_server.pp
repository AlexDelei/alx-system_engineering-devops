# Install Nginx
package { 'nginx':
  ensure => present,
}

# Define Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}

# Create Nginx default site
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('/usr/shared/nginx/html/index.html')
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Enable the site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

# Define the template for Nginx default site
file { '/usr/shared/nginx/html/index.html':
  ensure  => file,
  content => "server {\n  listen 80;\n  server_name localhost;\n  location / {\n    return 301 http://$host/redirect_me;\n  }\n  location /redirect_me {\n    return 200 'Hello World!';\n  }\n}\n",
  require => Package['nginx'],
  notify  => Service['nginx'],
}
