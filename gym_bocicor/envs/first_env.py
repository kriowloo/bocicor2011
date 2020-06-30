from gym_bocicor.envs.base_env import BaseEnv 

class FirstEnv(BaseEnv):
    def __init__(self):
        reads = ['ACCGT', 'CGTGC', 'TTAC', 'TACCGT']
        super().__init__(reads)

