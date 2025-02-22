Ampache - Web based audio/video streaming
=========================================

`Ampache`_ is a web based audio/video streaming application and file manager.
It allows you to access your music & videos from anywhere, using almost
any internet enabled device - hardware or software.

Browse and manage your music collection through a simple web interface.
Synchronize local and remote catalogs to curate an unique and consistent
collection. Stream your music to your preferred player or directly listen on
the web based HTML5 player. Listen from your phone, tablet or television; at
home, at work or anywhere you can access your Ampache server.

See the `Ampache documentation`_ for more usage and administration details.
The online `User Manual`_ is a great place to start.

This TurnKey appliance also includes all the standard features in
`TurnKey Core`_, and on top of that:

- SSL support out of the box.
- `Adminer`_ administration frontend for MySQL (MariaDB) (listening on port
  12322 - uses SSL).
- `Postfix`_ MTA (bound to localhost) to allow sending of email.
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL: username **root**

-  Adminer: username **adminer**

- Snipe-IT: username **admin**

.. _Ampache: https://ampache.org
.. _Ampache documentation: https://github.com/ampache/ampache/wiki
.. _User Manual: https://github.com/ampache/ampache/wiki/ampache7-for-users
.. _TurnKey Core: https://www.turnkeylinux.org/core
.. _Adminer: https://www.adminer.org/
.. _Postfix: https://www.postfix.org/
