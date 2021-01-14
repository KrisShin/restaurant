from config.manage_app import create_app


if __name__ == '__main__':
    manage = create_app()
    manage.run(host='0.0.0.0', port='9096')
