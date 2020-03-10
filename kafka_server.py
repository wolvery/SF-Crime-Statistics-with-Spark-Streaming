import producer_server

TOPIC_NAME = "udacity.police.department.calls.v1"
SERVER = "localhost:9092"
CLIENT = "police.department"

def run_kafka_server():
    input_file = "police-department-calls-for-service.json"

    producer = producer_server.ProducerServer(
        input_file = input_file,
        topic = TOPIC_NAME,
        bootstrap_servers = SERVER,
        client_id = CLIENT
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
