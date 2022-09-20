# IPython log file

from web.models import BasicSecretAgent, get_dynamic_agent_model_v1, get_dynamic_agent_model_v2
from django.core.cache import cache

bs = BasicSecretAgent.objects.all()
cache.set("cielcio", bs)

m = get_dynamic_agent_model_v1(42)
print(f"--- ORA PROVO CON IL NUOVO MODELLO {m.__name__}")
try:
    cache.set("cielcio42", m.objects.all())
except Exception as e:
    print(f"Non sono riuscito a salvarlo in cache {e.__class__.__name__}")

m = get_dynamic_agent_model_v2(42)
print(f"--- ORA PROVO CON IL NUOVO MODELLO FIXATO {m.__name__}")
cache.set("cielcio42", m.objects.all())
