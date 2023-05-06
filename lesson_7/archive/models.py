from django.db import models


class Material(models.Model):
    """Model representing a material."""

    name = models.CharField('Name', max_length=255, unique=True)
    created = models.DateTimeField('Creation date', auto_now_add=True)
    updated = models.DateTimeField('Date of change', auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'

    def __str__(self):
        return self.name


class Part(models.Model):
    """Model representing a part."""

    designation = models.CharField('Designation', max_length=50, unique=True)
    name = models.CharField('Name', max_length=50)
    material = models.ForeignKey(
        Material,
        on_delete=models.PROTECT,
        related_name='parts',
        verbose_name='Material'
    )
    created = models.DateTimeField('Creation date', auto_now_add=True)
    updated = models.DateTimeField('Date of change', auto_now=True)

    class Meta:
        ordering = ('designation',)
        verbose_name = 'Part'
        verbose_name_plural = 'Parts'

    def __str__(self):
        return f'{self.designation} - {self.name}'


class Assembly(models.Model):
    """Model representing an assembly."""

    designation = models.CharField('Designation', max_length=50, unique=True)
    name = models.CharField('Name', max_length=50)
    parts = models.ManyToManyField(
        Part,
        blank=True,
        verbose_name='Parts',
        through="AssemblyPart",
    )
    created = models.DateTimeField('Creation date', auto_now_add=True)
    updated = models.DateTimeField('Date of change', auto_now=True)

    class Meta:
        ordering = ('designation',)
        verbose_name = 'Assembly'
        verbose_name_plural = 'Assemblies'

    def __str__(self):
        return f'{self.designation} - {self.name}'


class AssemblyPart(models.Model):
    """Model representing intermediary table linking parts to assemblies."""

    assembly = models.ForeignKey(
        Assembly,
        on_delete=models.CASCADE,
        verbose_name='Assembly',
    )
    part = models.ForeignKey(
        Part,
        on_delete=models.PROTECT,
        verbose_name='Part',
    )
    part_count = models.PositiveIntegerField('Quantity', default=1)

    class Meta:
        verbose_name = 'Part in assembly'
        verbose_name_plural = 'Parts in assembly'
