from allinone import app
from allinone import db 

import sys
#debug

if sys.argv[1] == "debug":
    app.run(debug=True,host='0.0.0.0', port=4444)
# migrate

# run