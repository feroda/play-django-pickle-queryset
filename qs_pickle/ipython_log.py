# IPython log file

from web.models import BasicSecretAgent, get_dynamic_agent_model
from django.core.cache import cache

bs = BasicSecretAgent.objects.all()
cache.set("cielcio", bs)

m = get_dynamic_agent_model(007)
cache.set("cielcio52", m.objects.all())
