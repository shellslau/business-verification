import time

def datastore_health():
    try:
        make_datastore()
        log.info("datastore is healthy")
        return True
    except BaseException:
        log.info("waiting for datastore")
        return False

def main():
    startTime = time.time()
    while time.time() < startTime + MAX_TIME:
        time.sleep(INTERVAL)

        if datastore_health():
            start_server()

    sys.exit(1)


if __name__ == '__main__':
    main()
