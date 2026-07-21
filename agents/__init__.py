from agents.manager import manager

from agents.system_agent import system_agent
from agents.developer_agent import developer_agent
from agents.file_agent import file_agent

manager.register(system_agent)
manager.register(developer_agent)
manager.register(file_agent)