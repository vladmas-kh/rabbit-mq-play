import pika,sys,os,time

def callback(ch,method,properties,body):
    print(f"[x] Received: {body}")
    print(f"[x] Received decoded: {body.decode()}")
    print("Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    #Recieving
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
    channel = connection.channel()
    channel.basic_qos(prefetch_count=1)
    channel.queue_declare(queue='hello')
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='hello',
                        auto_ack=False,
                        on_message_callback=callback)
    print("[*] Waiting for messages.")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


