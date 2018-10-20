from core.models import *
class Broker(AbstractBroker):
    def __str__(self):
        return self.endereco
    def save(self, *args, **kwargs):
        self.estado=0
        super(Broker, self).save()

    def save(self, *args, **kwargs):
        super(Broker, self).save()
        #self.reinicia_broker()

    def reinicia_broker(self):
        self.estado = 4
        import mqtt.tasks as task
        task.restart.delay()



class Mqtt(AbstractMqtt):
    broker = models.ForeignKey(Broker, on_delete=True)
    def __str__(self):
        return self.topico

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Mqtt, self).save()
        self.reinicia_broker()

    def delete(self, using=None, keep_parents=False):
        super(Mqtt, self).delete()
        self.reinicia_broker()

    def reinicia_broker(self):
        self.broker.estado = 4
        self.broker.save()
        import mqtt.tasks as task
        task.restart.delay()
