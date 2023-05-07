1. Создать материал с названием `CuAl9`.

```bash
In [2]: Material.objects.create(name='CuAl9')
Out[2]: <Material: CuAl9>
```

2. Обновить материал с `id = 11`, изменив его имя на `CuAl9Mn2`.

```bash
In [10]: material = Material.objects.get(id=11)
In [11]: material.name = 'CuAl9Mn2'
In [12]: material.save()
```

3. Получить список материалов, в имени которых присутствует `al` без учёта
   регистра.

```bash
In [3]: Material.objects.filter(name__icontains='al')
Out[3]: <QuerySet [<Material: Aluminum>, <Material: CuAl10Fe4Ni4>, <Material: CuAl9Mn2>]>
```

4. Получить список материалов, которые были отредактированы в промежутке
   между `2023-05-06 14:05:00` и `2023-05-06 14:08:00`.

```bash
In [13]: import datetime
In [14]: start = datetime.datetime(2023, 5, 6, 14, 5, 0, tzinfo=datetime.timezone.utc)
In [15]: stop = datetime.datetime(2023, 5, 6, 14, 8, 0, tzinfo=datetime.timezone.utc)
In [16]: Material.objects.filter(updated__range=(start, stop))
Out[16]: <QuerySet [<Material: C45>, <Material: CG-14>, <Material: Fe360B>]>
```

5. Изменить материал детали `01.006 - Hull` с `C45` на `Fe360B`.

```bash
In [19]: part = Part.objects.get(designation='01.006')
In [20]: material = Material.objects.get(name='Fe360B')
In [21]: part.material = material
In [22]: part.save()
```

6. Добавить деталь `01.006 - Hull` в сборку `01.000-01 - Pump`.

```bash
In [50]: part = Part.objects.get(designation='01.006')
In [51]: assembly = Assembly.objects.get(designation='01.000-01')
In [52]: assembly.parts.add(part)
In [53]: assembly.save()
```

7. Получить список деталей, в имени которых отсутствуют буквы `s` и/или `S`.

```bash
In [66]: Part.objects.exclude(name__icontains='s')
Out[66]: <QuerySet [<Part: 01.001 - Cover>, <Part: 01.002 - Plate>, <Part: 01.006 - Hull>, <Part: 01.006-01 - Hull>, <Part: 01.007 - Rotor>, <Part: 02.001 - Valve>, <Part: 02.006 - Hull>, <Part: 03.001 - Hull>, <Part: 03.002 - Protective hood>, <Part: 03.006 - Cuff>, <Part: 03.008 - Fork>]>
```

8. Получить список имён деталей, изготовленных из материала `66Mn4`.

```bash
In [83]: material = Material.objects.get(name='66Mn4')
In [84]: Part.objects.values_list('name', flat=True).filter(material=material)
Out[84]: <QuerySet ['Spring d=1, n=10, H=30', 'Spring d=2, n=6, H=30', 'Spring d=1,5, n=6, H=40']>
```

9. Вычислить, сколько всего деталей в
   сборке `03.000 - Hydraulic brake cylinder`.

```bash
In [110]: from django.db.models import Sum
In [111]: assembly = Assembly.objects.get(designation='03.000')
In [112]: assembly.assemblypart_set.aggregate(Sum('part_count'))
Out[112]: {'part_count__sum': 13}
```

10. Получить все детали в сборке `03.000 - Hydraulic brake cylinder`,
    изготовленные из материала `Fe360B`.

```bash
In [2]: material = Material.objects.get(name='Fe360B')
In [3]: all_parts_made_of_material = material.parts.all()
In [4]: assembly = Assembly.objects.get(designation='03.000')
In [5]: part_ids_in_assembly = assembly.assemblypart_set.values_list('part', flat=True).filter(part__in=all_parts_made_of_material)
In [6]: Part.objects.filter(id__in=part_ids_in_assembly)
Out[6]: <QuerySet [<Part: 03.003 - Socket (valve)>, <Part: 03.004 - Socket>, <Part: 03.008 - Fork>]>
```
