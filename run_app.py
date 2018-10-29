from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/restaurantnlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-461470969715-461397092756-467620665030-f12a19dd46b7cc1d37201ead967d2510', #app verification token
							'xoxb-461470969715-466049008180-6kV3jP1XSOcT6HFhEvudLaLJ', # bot verification token
							'dtT4Dz31FoIhh5pGkTCQgZjr', # slack verification token
							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))