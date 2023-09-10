class Phone:
    def __init__(self, phone_number, call_history = [], message = []):
        self.phone_number = phone_number
        self.call_history = call_history
        self.message = message

    def call(self, other_phone):
        isinstance(other_phone, Phone)
        print(f"{other_phone.phone_number} was call to {self.phone_number}")
        self.call_history.append(f"{other_phone.phone_number} was call to {self.phone_number}")
    
    def show_call_history(self):
        print(f"{self.call_history}")

    def send_message(self, to_phone, from_phone, content):
        self.message.append({"to":to_phone, "from": from_phone, "content": content})

    def show_outgoing_messages(self):
        for message in self.message:
            if message["from"] == self.phone_number:
                print(f"to {message['to']} : {message['content']}")

    def show_incoming_messages(self):
        for message in self.message:
            if message["to"] == self.phone_number:
                print(f"from {message['from']} : {message['content']}")

    def show_messages_from(self, other):
        for message in self.message:
            if message["from"] == other.phone_number:
                print(f"from {message['from']} : {message['content']}")

my_phone = Phone(123456)
friend_phone = Phone(654321)
my_phone.call(friend_phone)
my_phone.show_call_history()
friend_phone.show_call_history()
my_phone.send_message(friend_phone.phone_number, my_phone.phone_number, "Hi David")
my_phone.send_message(my_phone.phone_number, friend_phone.phone_number, "Hi Ron")
my_phone.show_outgoing_messages()
my_phone.show_incoming_messages()
my_phone.show_messages_from(friend_phone)