import spacewalk
import tornado.ioloop
import zerog

def make_datastore():
    return zerog.CouchbaseDatastore(
        "couchbase", "Administrator", "password", "test"
    )

def make_queue(queueName):
    return zerog.BeanstalkdQueue("beanstalkd", 11300, queueName)

def start_server():
    tree = spacewalk.auto_tree(BaseExampleJob, "") #replace BaseExampleJob with base job for business service
    struct = spacewalk.Structure(tree)
    handlers = spacewalk.make_handlers(struct)

    server = spacewalk.Server(
        struct,
        "businessVerificationServier",
        make_datastore,
        make_queue,
        [WasteTimeJob, FizzBuzzJob],
        handlers
    )
    server.listen(8888)
    tornado.ioloop.IOLoop.current().start()

start_server()
