Install mod_wsgi
Installation of the mod_wsgi model and its configuration using Apache's WSGIDaemonProcess method available on Linux is not compatible with Windows. Windows expects mod_wsgi to be compiled using Microsoft Build Tools.

Because of this it is necessary to follow these steps from a CMD:

Set MOD_WSGI_APACHE_ROOTDIR as environment variable
set "MOD_WSGI_APACHE_ROOTDIR=C:\Apache24"
Activate python virtual environment
"D:path\to\project-root\venv\Scripts\activate"
Install mod_wsgi module into the virtual environment
pip install mod_wsgi
Copy the output to get the configuration required by Apache
mod_wsgi-express module-config
Install all the library dependencies of the Django project
pip install module-name
Or get a requirements file with pip freeze > requirements.txt and then install it with
pip install -r requirements.txt
Deactivate the virtual environment
deactivate
Configuration
Edit the host file at C:\Windows\System32\drivers\etc by adding this line to the bottom
127.0.0.2    www.app-name.com    app-name.com
Update the list of allowed hosts for the application in settings.py.
ALLOWED_HOSTS = ['www.app-name.com', 'app-name.com']
Update the Django projects wsgi.py file to look like the following.
import os
import sys
from django.core.wsgi import get_wsgi_application
from pathlib import Path

# Add project directory to the sys.path
path_home = str(Path(__file__).parents[1])
if path_home not in sys.path:
	sys.path.append(path_home)

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

application = get_wsgi_application()


Fix a Python bug that causes an error 500 every time a query is made to the database.
Edit the __init__.py file in project-root\venv\Lib\site-packages\asgiref by adding the following.
# PATCH that fix a Python Bug:
import sys
import asyncio

if sys.platform == "win32" and sys.version_info >= (3, 8, 0):
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


Set up Apache by modifying the httpd.conf file at C:\Apache24\conf, adding at the end everything that follows but replacing the directories with those on your system.
LoadFile "S:/path/to/project-root/venv/Scripts/python38.dll"
LoadModule wsgi_module "S:/path/to/project-root/venv/lib/site-packages/mod_wsgi/server/mod_wsgi.cp38-win_amd64.pyd"
WSGIPythonHome "C:/Users/User-name/AppData/Local/Programs/Python/Python38"
WSGIPythonPath "S:/path/to/project-root/venv/Lib/site-packages"

<VirtualHost *:80>
ServerAlias www.app-name.com
ServerName app-name.com
ServerAdmin info@admin.com
WSGIScriptAlias / "S:/path/to/project-root/project-name/wsgi.py"
  <Directory "S:/path/to/project-root/project-name">
    <Files wsgi.py>
      Require all granted
    </Files>
  </Directory>

Alias /static/ "S:/path/to/project-root/static/"
  <Directory "S:/path/to/project-root/static">
    Require all granted
  </Directory>

ErrorLog "S:/path/to/project-root/logs/apache.error.log"
CustomLog "S:/path/to/project-root/logs/apache.custom.log" common
</VirtualHost>


Check the syntax of the apache configuration files.
"C:\Apache24\bin\httpd.exe" -t
Run the Apache server.
"C:\Apache24\bin\httpd.exe" -k start
Check the Django application from the browser by visiting app-name.com.
If any module is missing, it is recommended to use this command to make sure it is installed in the Python home given to Apache.
pip install --target="C:/Users/User-name/AppData/Local/Programs/Python/Python38" library-name
