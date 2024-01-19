# Fixes an error in a PHP conf file

exec { 'replace_text_php':
	command => "sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
	path    => ['/bin/', '/usr/bin/']
}
