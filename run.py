from app import create_app
import os

port = int(os.environ.get('PORT', 5000))
app = create_app(env='prod') #Or pass 'live' to NOT be in debug mode
app.run(host='0.0.0.0', port=port)