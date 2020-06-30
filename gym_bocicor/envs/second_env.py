from gym_bocicor.envs.base_env import BaseEnv 

class SecondEnv(BaseEnv):
    def __init__(self):
        reads = ['ACGCTTGC', 'TTGCGTTC', 'ACTAGCAA', 'CGTTCGGT', 'AGCAATAC', 'TACTAGCA', 'AATACGCT', 'CTTGCGTT', 'ATACGCTT', 'CTAGCAAT']
        super().__init__(reads)

