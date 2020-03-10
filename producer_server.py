from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def generate_data(self):
        with open(self.input_file) as f:
            data = json.load(f)
            for line in data:                
                message = self.dict_to_binary(line)
                self.send(self.topic, message)
                time.sleep(1)

    def dict_to_binary(self, json_dict):
        json_message = json.dumps(json_dict, indent=4).replace('\r', '').replace('\n', '')        
        print(json_message)
        return json_message.encode('utf-8')
        
