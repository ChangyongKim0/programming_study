class Logger:
    def __init__(self, agent_name):
        self.agent_name = agent_name
        self.selfLog(
            "Logger with agent name {} is created.".format(self.agent_name))

    def selfLog(self, msg):
        print("Logger> \033[32m" + msg + "\033[0m")

    def log(self, msg):
        print("{}> \033[32m".format(self.agent_name) + msg + "\033[0m")

    def err(self, msg):
        print("{}> \033[31m".format(self.agent_name) + msg + "\033[0m")
