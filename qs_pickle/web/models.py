from django.db import models


class AbstractBasicSecretAgent(models.Model):

    name = models.CharField(max_length=42)
    age = models.IntegerField()
    is_fake = models.BooleanField(default=True)
    birthdate = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "secret agent"
        verbose_name_plural = "secret agents"


class BasicSecretAgent(AbstractBasicSecretAgent):
    """
    Basic Model whose queryset to be pickled
    """

    class Meta:
        db_table = "basic_secret"


def get_dynamic_agent_model(version=None):
    """
    Compute dynamic model whose queryset to be pickled
    """
    
    if version is None:
        return BasicSecretAgent

    cls = AbstractBasicSecretAgent
    name = 'basic_secet_' + str(version)

    class Meta:
        db_table = "basic_secret"
        app_label = cls._meta.app_label
        verbose_name = '%s for version %s' % (cls._meta.verbose_name, version)
        verbose_name_plural = '%s for version %s' % (cls._meta.verbose_name_plural, version)

    # Set up a dictionary to simulate declarations within a class
    attrs = {
        '__module__': cls.__module__,
        'Meta': Meta,
        '__str__': lambda self: 'Board var configs as of %s' % version,
        '_version_': version,
        # '__reduce__': cls.__reduce__,
        # '__setstate__': cls.__setstate__,
        # '__getstate__': cls.__getstate__,
        # '__dict__': cls.__dict__
    }

    model = type(name, (AbstractBasicSecretAgent, ), attrs)
    return model
    
