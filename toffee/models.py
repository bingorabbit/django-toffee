from django.db import models
from django.db.models.query import QuerySet


class Countries(models.Model):
    country_code = models.CharField(max_length=2)
    country = models.CharField(max_length=100)

    def get_absolute_url(self):
        return None


class MobilesQuerySet(QuerySet):
    pass
    # def _clone(self):
    #     query_set = super(MobilesQuerySet, self)._clone()
    #     for qs_object in query_set:
    #         qs_object.__dict__['mobile_model'] = qs_object.__dict__['mobile_model']+'b'
    #         print qs_object.__dict__['mobile_model']
    #     return query_set


class MobilesManager(models.Manager):

    # def get_queryset(self):
    #     #import ipdb; ipdb.set_trace()
    #     return MobilesQuerySet(self.model).linked_values_queryset()
    #     # query_set = super(MobilesManager, self).get_query_set()
    #     # for qs_object in query_set:
    #     #     #qs_object.mobile_model = "<a href='%s' class='datatable_row_link'>%s</a>" % ("mobiles/"+str(qs_object.id), qs_object.mobile_model)
    #     #     qs_object.mobile_model = "bingo"
    #     #     print qs_object.__dict__['mobile_model']
    #     # for qs_object in query_set:
    #     #     print qs_object.__dict__['mobile_model']
    #     # return query_set
    #
    # def all(self):
    #     return MobilesQuerySet(self.model).linked_values_queryset()
    #
    # def filter(self, *args, **kwargs):
    #     return MobilesQuerySet(self.model).linked_values_queryset()
    #
    # def order_by(self, *args, **kwargs):
    #     return MobilesQuerySet(self.model).linked_values_queryset()
    # def _clone(self):
    #     query_set = super(MobilesManager, self)._clone()
    #     for qs_object in query_set:
    #         qs_object.__dict__['mobile_model'] = qs_object.__dict__['mobile_model']+'b'
    #         print qs_object.__dict__['mobile_model']
    #     return query_set
    #
    # def all(self):
    #     query_set = super(MobilesManager, self).all()
    #     for qs_object in query_set:
    #         qs_object.__dict__['mobile_model'] = qs_object.__dict__['mobile_model']+'b'
    #         print qs_object.__dict__['mobile_model']
    #     return query_set
    #
    # def get_queryset(self):
    #     query_set = super(MobilesManager, self).get_queryset()
    #     for qs_object in query_set:
    #         qs_object.__dict__['mobile_model'] = qs_object.__dict__['mobile_model']+'b'
    #         print qs_object.__dict__['mobile_model']
    #     return query_set.filter(mobile_model='D821')
    pass


class Mobiles(models.Model):
    mobile_model = models.CharField(max_length=5)
    mobile_name = models.CharField(max_length=100)
    country = models.ForeignKey(Countries)
    objects = MobilesManager()


class Countries2(models.Model):
    country_code = models.CharField(max_length=2)
    country = models.CharField(max_length=100)

    def __unicode__(self):
        return self.country