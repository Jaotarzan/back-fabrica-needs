from waitress import serve
from config import wsgi

serve(wsgi, host='0.0.0.0', port=8000)