## Load mdoels

```python
from <App>.models import <Model>
from Digimon.models import Digimon
```

## Query models

```python
Digimon.objects.all()
```

## Show data from query models

```code
print(Digimon.objects.all().values())
```

## Load data from json

```bash
python manage.py loaddata <App_name>/fixtures/<file>.json
```
