#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models

from fias.fields import UUIDField
from .ifns import IFNS
from .addrobj import AddrObj, AddrObjFuture
from .normdoc import NormDoc

__all__ = ['House', 'HouseFuture']


class HouseBase(IFNS):

    class Meta:
        abstract = True

    postalcode = models.PositiveIntegerField(blank=True, null=True)

    housenum = models.CharField(max_length=20, blank=True, null=True)
    eststatus = models.BooleanField()
    buildnum = models.CharField(max_length=10, blank=True, null=True)
    strucnum = models.CharField(max_length=10, blank=True, null=True)
    strstatus = models.PositiveSmallIntegerField()
    houseguid = UUIDField()
    houseid = UUIDField(primary_key=True)

    startdate = models.DateField()
    enddate = models.DateField()

    statstatus = models.PositiveSmallIntegerField()
    normdoc = models.ForeignKey(NormDoc, blank=True, null=True)

    counter = models.IntegerField()


class HouseFuture(HouseBase):

    class Meta:
        app_label = 'fias'

    aoguid = models.ForeignKey(AddrObjFuture)

class House(HouseBase):

    class Meta:
        app_label = 'fias'

    aoguid = models.ForeignKey(AddrObj)