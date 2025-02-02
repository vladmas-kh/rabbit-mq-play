import pika,sys,os

def callback(ch,method,properties,body):
    print(f"[x] Received {body}")

def main():
    #Recieving
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello',
                        auto_ack=True,
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


