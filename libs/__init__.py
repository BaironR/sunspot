import logging as log

import coloredlogs
from dotenv import load_dotenv

# Configure logging
coloredlogs.install(level='INFO',
                    field_styles={
                        'asctime': {'color': 'white'},
                        'levelname': {'color': 'white', 'bold': True},
                        'name': {'color': 'blue'}})

log.debug("Initializing the application ..")

# Load environment variables
load_dotenv()

log.debug("Initialization complete.")