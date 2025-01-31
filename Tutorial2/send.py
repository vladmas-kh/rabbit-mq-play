import pika,sys
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.basic_qos(prefetch_count=1)
channel.queue_declare(queue='hello')

message = ''.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body = message)

print(f"[x] Sent {message}'")
connection.close()