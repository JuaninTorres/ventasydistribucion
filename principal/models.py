#encoding:utf-8
from django.db import models
#from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre o Razon Social')
    rut = models.TextField(verbose_name='RUT')
    giro = models.TextField(verbose_name='Giro')
    direccion = models.TextField(verbose_name='Dirección')
    telefono = models.TextField(verbose_name='Teléfono')
    contacto = models.TextField(verbose_name='Persona de Contacto')

    def __unicode__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción', help_text='Redacta las caracteristicas de la categoria')

    def __unicode__(self):
        return self.nombre


class Envase(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción', help_text='Redacta las caracteristicas del producto')

    def __unicode__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=255, verbose_name='Nombre')
    descripcion = models.TextField(verbose_name='Descripción', help_text='Redacta las caracteristicas del producto')
    imagen = models.ImageField(upload_to='productos', verbose_name='Imagen')
    envase = models.ForeignKey(Envase, verbose_name='Tipo de envase')
    categoria = models.ForeignKey(Categoria)

    def __unicode__(self):
        return self.nombre


class Despacho(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente a despachar')
    productos = models.ManyToManyField(Producto, through='Pedido', verbose_name='Productos a despachar')
    fecha = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.id


class Pedido(models.Model):
    producto = models.ForeignKey(Producto, verbose_name='Producto')
    despacho = models.ForeignKey(Despacho, verbose_name='Despacho')
    cantidad = models.IntegerField(verbose_name='Cantidad')


class Factura(models.Model):
    ESTADOS_FACTURA = (
        ('pagada', 'Pagada'),
        ('no_pagada', 'No Pagada'),
    )
    numero = models.IntegerField(unique=True)
    cliente = models.ForeignKey(Cliente)
    fecha = models.DateTimeField(auto_now=True)
    estado_pago = models.CharField(choices=ESTADOS_FACTURA, max_length=10)
    despachos = models.ManyToManyField(Despacho)


class PrestamoEnvase(models.Model):
    cliente = models.ForeignKey(Cliente, verbose_name='Cliente a quien se le ha prestado')
    envase = models.ForeignKey(Envase, verbose_name='Tipo de envases')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    fecha = models.DateTimeField(auto_now=True)
