import os
from handling import LLM_Agent
from handling import PaperHandling

prompts = {"overall_instructions":" Do NOT add factual information beyond what is given to you in the prompt. The text to analyse is :","base_line":"""Please extract the following fields:
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
how it is structured""","chain_of_thought": "","generate_questions":"Based on the following text generate 10 questions AND answers based on the content (NOT details like DOI and ISSN) which can be answered using ONLY information in the following text. Only output the questions", "chain_of_verification": "based on the following generated questions and answers use them to refine the generated output", 
"focused_extraction_prompting":"", "":"",
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
        self.llm_agent = llm_agent
        self.llm_agent.openai_verify()
        self.responses = {"base_line_response":"","CoFt_response":"","CoFv_response_joint":"", "CoFv_response_two_step":"", "CoFv_cross_check":""}

    def __repr__(self):
        return (f'{self.__class__.__name__}')
    
    def baseline(self):
        """
        carry out baseline prompting 
        """
        full_prompt = self.base_prompts["overall_instructions"] + self.text + self.base_prompts["base_line"]
        baseline_repsonse = self.llm_agent.query(full_prompt)
        self.responses["base_line_response"] = baseline_repsonse
        return self.responses

    def CoFt(self):
        """
        carry out chain of thought prompting 
        """
        full_prompt = self.base_prompts["overall_instructions"] + "the following is an example of how to do this:"+ self.support_text + self.base_prompts["base_line"]+ self.text
        CoFt_response = self.llm_agent.query(full_prompt)
        self.responses["CoFt_response"] = CoFt_response
        return self.responses

    def CoFv(self,style,one_shot=False):
        """
        carry out chain of verification prompting
        param: style - indicates the style of CoFv prompting. 
               style=1 is Joint prompting
               style=2 is 2-Step prompting
               style=3 is Cross Checking
        param: one_shot (bool) use one shot example or not 
        """
        #generate questions on text 
        question_gen_prompt = self.base_prompts["generate_questions"] + self.text
        generated_questions = self.llm_agent.query(question_gen_prompt)
        print("These are the generated questions", generated_questions)
        if style==1:
            full_prompt = self.base_prompts["overall_instructions"] + self.text + self.base_prompts["base_line"] + self.base_prompts["chain_of_verification"] + generated_questions
            CoFt_response_joint = self.llm_agent.query(full_prompt)
            self.responses["CoFv_response_joint"] = CoFt_response_joint

        elif style==2:
            first_prompt = self.base_prompts["overall_instructions"] + self.text + self.base_prompts["base_line"]
            first_response = self.llm_agent.query(first_prompt)
            print(first_response)
            second_prompt = "answer the following questions based on the following text:" + self.text + "and subsequently ammend the following based the answers:" + first_response
            second_response = self.llm_agent.query(second_prompt)
            self.responses["CoFv_response_two_step"] = second_response
            return self.responses
        elif style==3:
            pass

        return self.responses

        #joint 

        #2 step 

        #cross checking 


if __name__ == "__main__":
    #import support text
    with open("./prompts/chain_of_thought.txt", 'r') as file:
                support_text = file.read()

    #run inference 
    paper = PaperHandling("UJPR-4-1-RW1")
    context = paper.unwrap_pdf()
    llm = LLM_Agent()
    prompting_instance = prompting(prompts,context,support_text,llm)
    output = prompting_instance.CoFv(style=1)
    print(output)


        
        



