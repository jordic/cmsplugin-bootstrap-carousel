#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# -------------------------------------------------------------------
'''
'''
# coding: utf-8
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

from cms.models.pluginmodel import CMSPlugin
from PIL import Image
from cStringIO import StringIO


class Carousel(CMSPlugin):
    domid = models.CharField(max_length=50, verbose_name=_('Name'))
    interval = models.IntegerField(
        default=5000,
        help_text="The amount of time in"
        " milliseconds to delay cycling items."
        " If zero carousel will not automatically"
        " cycle.")

    show_title = models.BooleanField(
        help_text="Display image titles, if true.",
        default=False)

    show_caption = models.BooleanField(
        help_text="Display image captions, if true.",
        default=False)

    show_controls = models.BooleanField(
        help_text="Display carousel controls, if true.",
        default=True)

    show_indicator = models.BooleanField(
        help_text="Display slide indicator, if true.",
        default=True)

    title = models.CharField(
    	help_text="If contains something, no text for slides..", 
    	blank=True, null=True, 
    	max_length=255)


    def size(self):
        return (self.width, self.height)

    def copy_relations(self, oldinstance):
        for item in oldinstance.carouselitem_set.all():
            item.pk = None
            item.carousel = self
            item.save()

    def __unicode__(self):
        return self.domid


class CarouselItem(models.Model):
    carousel = models.ForeignKey(Carousel)
    caption_title = models.CharField(max_length=100, blank=True, null=True)
    caption_content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="uploads/", blank=True, null=True)
    url = models.CharField(max_length=256, blank=True, default=None)






