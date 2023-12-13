import os
from handling import LLM_Agent

prompts = {"overall_intructions":"If you do not know the answer state I do not know. Do NOT add factual information beyond what is given to you in the prompt. The text to analyse is :","base_line":"""Please extract the following fields:
■ Plant-Disease / Activity: Identify which plants are used to treat or
manage which specific diseases or activities.
● Example:
○ Plant: Papaver Somniferum
○ Disease / activity: Analgesic
■ Plant-Compound: Extract information about specific compounds
found in these plants/
● Examples:
○ Plant: Papaver Somniferum
○ Compounds: Morphine, Codeine
■ Plant-Location of origin: Determine the geographical locations
where these plants traditionally used.
● Examples:
○ Plant: Papaver Somniferum
○ Location of Origin: China, Europe, Greek, Roman, etc
■ *Note: While not all "locations" are written in a
consistent fashion, for now, feel free to simplify
by referencing relevant locations regardless of
how it is structured""","chain_of_thought": "", "chain_of_verification": "", "focused_extraction_prompting":"",
           "iterative_refinement":[]}



class prompting:
    """
    class to carry out bespoke prompting methods
    0. baseline 
    1. chain of thought
    2. chain of verification 
    3. Focused extraction prompting 

    attributes:

    methods:

    """
    def __init__(self, base_prompts, text,support_text,llm_agent):
        self.base_prompts = base_prompts
        self.text = text
        self.support_text = support_text
        self.llm_agent = llm_agent()
        self.llm_agent.openai_verify()
        self.responses = {"base_line_response":"","CoFt_response":"","CoFv_response":""}

    def __repr__(self):
        return (f'{self.__class__.__name__}')
    
    def baseline(self):
        """
        carry out baseline prompting 
        """
        full_prompt = self.base_prompts["overall_instructions"] + self.text + self.base_prompts["base_line"]
        baseline_repsonse = self.llm_agent.query(full_prompt)
        self.responses["base_line_response"] = baseline_repsonse

    def CoFt(self):
        """
        carry out chain of thought prompting 
        """
        full_prompt = self.base_prompts["overall_intructions"] + self.support_text + self.text
        CoFt_response = self.llm_agent.query(full_prompt)
        self.responses["CoFt_response"] = CoFt_response

    def CoFv(self,style,one_shot):
        """
        carry out chain of verification prompting
        param: style - indicates the style of CoFv prompting. 
               style=1 is Joint prompting
               style=2 is 2-Step prompting
               style=3 is Cross Checking
        param: one_shot (bool) use one shot example or not 
        """
        #generate questions on text 

        #joint 

        #2 step 

        #cross checking 





        
        



