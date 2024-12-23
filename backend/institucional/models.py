from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Home(models.Model):
    titulo  = 'Elementos da seção Início'
    frase   = models.CharField(max_length = 250, verbose_name = 'Frase da seção Início')
    imagem  = models.ImageField(
        upload_to = 'background/%Y',
        null = True, blank = True,
        verbose_name = 'Imagem de fundo da seção Início')

    class Meta:
        verbose_name = 'Elementos da seção Início'
        verbose_name_plural = '01 - Elementos da seção Início'

    def __str__(self):
        return self.titulo

class Fluxo(models.Model):
    titulo      = 'Conteúdo do Fluxo de Trabalho'
    titulo1     = models.CharField(max_length = 30, verbose_name = 'Título da  primeira etapa do fluxo de trabalho')
    descricao1  = models.TextField(max_length = 100,  verbose_name = 'Descrição da primeira etapa do fluxo de trabalho')
    imagem1     = models.ImageField(upload_to = 'institucional/fluxo/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')
    titulo2     = models.CharField(max_length = 30, verbose_name = 'Título da segunda etapa do fluxo de trabalho')
    descricao2  = models.TextField(max_length = 100,  verbose_name = 'Descrição da segunda etapa do fluxo de trabalho')
    imagem2     = models.ImageField(upload_to = 'institucional/fluxo/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')
    titulo3     = models.CharField(max_length = 30, verbose_name = 'Título da terceira etapa do fluxo de trabalho')
    descricao3  = models.TextField(max_length = 100,  verbose_name = 'Descrição da terceira etapa do fluxo de trabalho')
    imagem3     = models.ImageField(upload_to = 'institucional/fluxo/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')
    titulo4     = models.CharField(max_length = 30,  verbose_name = 'Título da quarta etapa do fluxo de trabalho')
    descricao4  = models.TextField(max_length = 100, verbose_name = 'Descrição da quarta etapa do fluxo de trabalho')
    imagem4     = models.ImageField(upload_to = 'institucional/fluxo/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')

    class Meta:
        verbose_name = 'Etapas'
        verbose_name_plural = '02 - Fluxo de Trabalho'

    def __str__(self):
        return self.titulo

class Feature(models.Model):
    titulo      = 'Conteúdo das Features'
    titulo1     = models.CharField(max_length = 20,verbose_name = 'Título da primeira Feature')
    descricao1  = models.TextField(max_length = 85,verbose_name = 'Descrição da primeira Feature')
    imagem1     = models.ImageField(upload_to = 'institucional/features/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')
    titulo2     = models.CharField(max_length = 20,verbose_name = 'Título da segunda Feature')
    descricao2  = models.TextField(max_length = 85,verbose_name = 'Descrição da segunda Feature')
    imagem2     = models.ImageField(upload_to = 'institucional/features/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')
    titulo3     = models.CharField(max_length = 20,verbose_name = 'Título da terceira Feature')
    descricao3  = models.TextField(max_length = 85,verbose_name = 'Descrição da terceira Feature')
    imagem3     = models.ImageField(upload_to = 'institucional/features/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')
    titulo4     = models.CharField(max_length = 20,verbose_name = 'Título da quarta Feature')
    descricao4  = models.TextField(max_length = 85,verbose_name = 'Descrição da quarta Feature')
    imagem4     = models.ImageField(upload_to = 'institucional/features/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')
    titulo5     = models.CharField(max_length = 20,verbose_name = 'Título da quinta Feature')
    descricao5  = models.TextField(max_length = 85,verbose_name = 'Descrição da quinta Feature')
    imagem5     = models.ImageField(upload_to = 'institucional/features/%Y',null = True, blank = True,verbose_name = 'Imagem da feature')

    class Meta:
        verbose_name = 'Cards'
        verbose_name_plural = '03 - Features'

    def __str__(self):
        return self.titulo

class Depoimento(models.Model):
    nome        = models.CharField(max_length = 50,null=True,blank=True, verbose_name = 'Nome da pessoa (este nome não aparecerá no site)')
    depoimento  = models.TextField(max_length = 250, verbose_name = 'Depoimento da pessoa')
    imagem      = models.ImageField(
        upload_to = 'depoimento/%Y',
        null = True, blank = True,
        verbose_name = 'Imagem da pessoa')

    class Meta:
        verbose_name        = 'Depoimento'
        verbose_name_plural = '04 - Depoimentos'

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome                = models.CharField(max_length = 50, verbose_name = 'Nome')
    telefone            = models.CharField(max_length = 20, verbose_name = 'Telefone')
    email               = models.EmailField(verbose_name = 'E-mail')
    mensagem            = models.TextField(max_length = 1000, verbose_name = 'Mensagem')
    respondido          = models.BooleanField(default = False, verbose_name = 'Mensagem respondida')
    stringrespondido    = '[RESPONDIDO] '
    stringpendente      = '[PENDENTE] '
    envio_data          = models.DateField(auto_now_add=True)
    respondido_data     = models.DateField(null=True)

    class Meta:
        verbose_name        = 'Mensagem'
        verbose_name_plural = '05 - Mensagens'

    def __str__(self):
        if self.respondido == True:
            situacaomensagem = self.stringrespondido
        else:
            situacaomensagem = self.stringpendente

        return (situacaomensagem + self.email)