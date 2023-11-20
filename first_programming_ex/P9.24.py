## A Message that models an e-mail message. A message has a recipient, a sender, and a message text.
#
class Message:
    #class variables
    _no_messages = 0  # save the total number of messages sent
    _log = {}         # save a log of the messages sent

    ## Constructs a message with a sender and a recipient.
    # @param sender the sender of the message
    # @param recipient the recipient of the message
    #
    def __init__(self, sender, recipient):
        self._sender = sender
        self._recipient = recipient
        self._message_body = ""

    ## Appends a line of text to the message body.
    # @param text the line of text to append
    #
    def append(self, text):
        self._message_body += text + "\n"
        self.log_messages()

    ## Makes the message into one long string.
    # @return a string message
    #
    def toString(self):
        return "From: {}\nTo: {}\n{}".format(self._sender, self._recipient, self._message_body)

    ## Logs the message, append the total # of messages.
    #
    def log_messages(self):
        Message._no_messages += 1
        if self._sender not in Message._log:
            Message._log[self._sender] = {}
        Message._log[self._sender][self._recipient] = self._message_body


# Test class
if __name__ == "__main__":
    msg1 = Message("SSS", "RRR")
    msg1.append("one message to RRR")
    msg1.append("to Storo")
    print(msg1.toString())

    msg2 = Message("ss", "rr")
    msg2.append("one message to rr")
    print(msg2.toString())
    
    print(f"Total number of messages: {Message._no_messages}")
    print(f"Log of messages: {Message._log}")
 
