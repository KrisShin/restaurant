# -*- coding: utf-8 -*-

from config.manage_app import create_app

manage = create_app()

if __name__ == '__main__':
    manage.run(host='0.0.0.0', port='9096')
