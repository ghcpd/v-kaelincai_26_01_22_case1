"""Simplified UserAgent class for demo"""
from __future__ import absolute_import, unicode_literals

import random


class UserAgent(object):
    """Simplified UserAgent class for demonstration"""
    
    def __init__(self):
        self.data = {
            'chrome': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/91.0',
            ],
            'firefox': [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Firefox/89.0',
                'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Firefox/89.0',
            ],
        }
    
    @property
    def chrome(self):
        """Return a random Chrome user agent"""
        return random.choice(self.data['chrome'])
    
    @property
    def firefox(self):
        """Return a random Firefox user agent"""
        return random.choice(self.data['firefox'])
    
    @property
    def random(self):
        """Return a random user agent"""
        all_agents = []
        for agents in self.data.values():
            all_agents.extend(agents)
        return random.choice(all_agents)
