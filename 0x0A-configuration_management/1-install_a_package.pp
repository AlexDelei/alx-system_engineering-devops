#!/usr/bin/pup
# Installing a version of Flask

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
