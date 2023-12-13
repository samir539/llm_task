

class eval:
    """
    A class to carry out evaluation on llm generated answers
    """
    with open(file_path, 'r') as file:
            api_key = file.read().strip()