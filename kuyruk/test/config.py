KUYRUK_RABBIT_HOST = 'localhost'
KUYRUK_RABBIT_PORT = 5672
KUYRUK_RABBIT_USER = 'guest'
KUYRUK_RABBIT_PASSWORD = 'guest'
KUYRUK_IMPORT_PATH = None
KUYRUK_EAGER = False
KUYRUK_MAX_LOAD = 20
KUYRUK_MAX_RUN_TIME = None
KUYRUK_SAVE_FAILED_TASKS = False
KUYRUK_WORKERS = {}
KUYRUK_MANAGER_HOST = 'localhost'
KUYRUK_MANAGER_PORT = 16501
KUYRUK_MANAGER_HTTP_PORT = 16500
KUYRUK_WORKERS = {
    'aslan.local': 'a, 2*b, c*3, @d'
}
KUYRUK_IMPORTS = [
    'kuyruk.test.config',
    'kuyruk',
]
