from anthropic import Anthropic

class Claude:
    def __init__(self, api_key):
        """
        Initializes the Claude model from the Anthropic API.

        ARGS
        ----
        None

        RETURNS
        -------
        None
        """
        
        self.client = Anthropic(api_key=api_key)

    def generate(self, message, prompt):
        """
        Generates a response to the given message using the Claude model.

        ARGS
        ----
        message : str
            The message to respond to.
        prompt : str
            The prompt to use for the response.

        RETURNS
        -------
        str
            The response to the given message.
        """
        
        message = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1000,
            system=prompt,
            messages=[
                {"role": "user", "content": message}
            ]
        )
        
        return message.content