Role Name
=========

Installs [osTicket](https://osticket.com/) Support Ticketing System

Requirements
------------

The osTicket is a web application based on the LAMP stack. It will need the following pre-requisites:

* Apache (Recommended: geerlingguy.apache)
* MySQL or similar Database server (Recommended: geerlingguy.mysql or geerlingguy.postgresql)
* PHP (Recommended: geerlingguy.php-versions, geerlingguy.php, geerlingguy.apache-php-fpm, php-mysql).


Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

Dependencies
------------

N/A

Example Playbook
----------------

The following example playbook installs osticket

```
- hosts: all
  roles:
    - geerlingguy.apache
    - geerlingguy.mysql
    - geerlingguy.php-versions
    - geerlingguy.php
    - geerlingguy.php-mysql
    - geerlingguy.apache-php-fpm
    - junaidali.osticket
```

License
-------

BSD

Author Information
------------------

This role was created in 2019 by [Junaid Ali](https://github.com/junaidali)
