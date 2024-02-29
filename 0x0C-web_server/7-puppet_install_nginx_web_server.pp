# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Configure Nginx to listen on port 80 and return "Hello World!" at the root
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
server {
    listen 80;
    server_name _;
    root /var/www/html;
    index index.html;
    location / {
        echo 'Hello World!';
    }
    location /redirect_me {
        return 301 https://www.example.com;
    }
}
",
  notify  => Service['nginx'],
}

# Enable the default site by creating a symbolic link
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
