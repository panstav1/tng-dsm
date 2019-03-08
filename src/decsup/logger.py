import logging, datetime, json, sys, traceback


class TangoLogger(object):

    @staticmethod
    def getLogger(name):
        logging.basicConfig(filename='logger',level=logging.DEBUG)
        logger = logging.getLogger("tango.{}".format(name))
        logger.propagate = False
        th = TangoJsonLogHandler('logger')
        th.setLevel(logging.DEBUG)
        logger.addHandler(th)
        return logger


class TangoJsonLogHandler(logging.FileHandler):

    def _to_tango_dict(self, record):
        d = {
            # TANGO default fields
            "type": record.levelname[0],
            "timestamp": "{} UTC".format(datetime.datetime.utcnow()),
            "start_stop": record.__dict__.get("start_stop", ""),
            "component": record.name,
            "operation": record.__dict__.get("operation", record.funcName),
            "message": str(record.msg),
            "status": record.__dict__.get("status", ""),
            "time_elapsed": record.__dict__.get("time_elapsed", "")
        }
        return d

    def emit(self, record):
        print(json.dumps(self._to_tango_dict(record)),file=sys.stdout)
        msg = json.dumps(self._to_tango_dict(record))
        stream = self.stream
        stream.write(msg)
        stream.write(self.terminator)
        # self.flush()
        sys.stdout.flush()
