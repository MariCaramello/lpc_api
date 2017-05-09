from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields, utils
from evento.models import *
from django.contrib.auth.models import User
#Resource
class PessoaResource(ModelResource):
    class Meta:
        queryset = Pessoa.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class EventoResource(ModelResource):
    #realizador = models.ForeignKey('Pessoa')
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = Evento.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class EventoCientificoResource(ModelResource):
    realizador = fields.ToOneField(PessoaResource, 'realizador')
    class Meta:
        queryset = EventoCientifico.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }



class PessoaFisicaResource(ModelResource):

    class Meta:
        queryset = PessoaFisica.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class PessoaJuridicaResource(ModelResource):
    class Meta:
        queryset = PessoaJuridica.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class ArtigoCientificoResource(ModelResource):
    evento = fields.ToOneField(EventoCientificoResource, 'evento')
    class Meta:
        queryset = ArtigoCientifico.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class TipoInscricaoResource(ModelResource):
    class Meta:
        queryset = TipoInscricao.objects.all()
        allowed_methods = ['get','post', 'put', 'delete']
        authorization = Authorization()
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class InscricaoResource(ModelResource):
    #evento = models.ForeignKey('Evento')
    #tipoInscricao = models.ForeignKey('TipoInscricao')
    pessoa = fields.ToOneField(PessoaFisicaResource, 'pessoa')
    evento = fields.ToOneField(EventoResource, 'evento')
    tipoInscricao = fields.ToOneField(TipoInscricaoResource, 'tipoInscricao')

    class Meta:
        queryset = Inscricoes.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }

class ArtigoAutorResource(ModelResource):
    #artigoCientifico = models.ForeignKey('ArtigoCientifico')
    artigoCientifico = fields.ToOneField(ArtigoCientificoResource, 'artigoCientifico')
    #autor = models.ForeignKey('Autor')
    autor = fields.ToOneField(AutorResource, 'autor')
    class Meta:
        queryset = ArtigoAutor.objects.all()
        authorization = Authorization()
        allowed_methods = ['get','post', 'put', 'delete']
        filtering = {
            "descricao": ('exact', 'startswith',)
        }


#isso seria o get?
#http://localhost:8000/api/v1/tipoinscricao/?descricao=web
#http://localhost:8000/api/v1/tipoinscricao/?descricao__startswith=est


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        excludes = ['password', 'is_active']
