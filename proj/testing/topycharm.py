import EnvManager
import AppConfig



x = EnvManager.force_get_env("PYTHONPATH")
print(x)

