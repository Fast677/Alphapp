# cloud-services/scripts/utils/__init__.py

from .config_utils import load_config
from .api_utils import make_api_request
from .error_handling import handle_error
En este caso, el archivo __init__.py importa las funciones load_config de config_utils.py, make_api_request de api_utils.py, y handle_error de error_handling.py. Esto permitiría a otros scripts importar estas funciones directamente desde el paquete utils:
from cloud_services.scripts.utils import load_config, make_api_request, handle_error

config = load_config()
response = make_api_request(url, data)
if response.status_code != 200:
    handle_error(response)
