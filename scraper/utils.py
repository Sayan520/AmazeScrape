import random
import time
from config import SCRAPE_DELAY

# Function to get a random user agent from the list
def get_random_user_agent(user_agents):
    return random.choice(user_agents)

# Random sleep between SCRAPE_DELAY and SCRAPE_DELAY+5
def add_delay():
    time.sleep(random.uniform(SCRAPE_DELAY, SCRAPE_DELAY + 5))  
