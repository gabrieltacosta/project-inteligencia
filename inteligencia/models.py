from django.db import models
from django.template.defaultfilters import truncatechars


class PostGrad(models.Model):
    title = models.CharField(max_length=10, verbose_name="Posto/Graduação")

    class Meta:
        ordering = ["id"]
        verbose_name = "Post/Grad"
        verbose_name_plural = "Post/Grad"

    def __str__(self):
        return self.title
    

class NadaCosta(models.Model):
    SUBUNIDADE_CHOICES = (
        ("EM", "Estado Maior"),
        ("1CIA", "1ª Cia"),
        ("2CIA", "2ª Cia"),
        ("3CIA", "3ª Cia"),
        ("4CIA", "4ª Cia"),
        ("OUTRA", "Outra"),
    )

    CONDUTA_CHOICES = (
        ("SN", "Sem Novidade"),
        ("CN", "Com Novidade"),
        ("PN", "Possível Novidade"),
    )

    conduta = models.CharField(max_length=2, choices=CONDUTA_CHOICES, blank=True, null=True, verbose_name="Conduta")
    post_grad = models.ForeignKey(PostGrad, on_delete=models.PROTECT, verbose_name="Post/Grad")
    re =models.CharField(max_length=9, unique=True, null=False, blank=False, verbose_name="R.E.")
    nome_guerra = models.CharField(max_length=50, verbose_name="Nome de Guerra",)
    nome_completo = models.CharField(max_length=100, verbose_name="Nome Completo")
    opm = models.CharField(max_length=50, null=True, blank=True, verbose_name="OPM")
    subunidade = models.CharField(max_length=5, choices=SUBUNIDADE_CHOICES, blank=True, null=True, verbose_name="Subunidade")
    situacao = models.CharField(max_length=50, blank=True, null=True, verbose_name="Situação")
    consulta = models.TextField(blank=True, null=True, verbose_name="Consulta")
    p2 = models.TextField(blank=True, null=True, verbose_name="P2")
    jd = models.TextField(blank=True, null=True, verbose_name="JD")
    observacao = models.TextField(blank=True, null=True, verbose_name="Observações")
    imagem = models.ImageField(upload_to="nada-consta/%Y/%m/%d/", null=True, blank=True, verbose_name="Foto")
    created_at = models.DateField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateField(auto_now=True, verbose_name="Atualizado em")

    @property
    def Consulta(self):
        return truncatechars(self.consulta, 30)
    
    @property
    def P2(self):
        return truncatechars(self.p2, 30)
    
    @property
    def JD(self):
        return truncatechars(self.jd, 30)
    
    @property
    def Observação(self):
        return truncatechars(self.observacao, 30)
    
    class Meta():
        ordering = ["post_grad__id"]
        verbose_name = "Nada Costa"
        verbose_name_plural = "Nada Costa"

    def __str__(self):
        return self.nome_guerra
    



class PlanoChamada(models.Model):

    UF_CHOICES = (
        ("SP", "São Paulo"),
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso	"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais	"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )

    SUBUNIDADE_CHOICES = (
        ("EM", "Estado Maior"),
        ("1CIA", "1ª Cia"),
        ("2CIA", "2ª Cia"),
        ("3CIA", "3ª Cia"),
        ("4CIA", "4ª Cia"),
        ("OUTRA", "Outra"),
    )

    post_grad = models.ForeignKey(PostGrad, on_delete=models.PROTECT, verbose_name="Post/Grad")
    re =models.CharField(max_length=9, unique=True, null=False, blank=False, verbose_name="R.E.")
    nome_guerra = models.CharField(max_length=50, verbose_name="Nome de Guerra")
    nome_completo = models.CharField(max_length=100, verbose_name="Nome Completo")
    subunidade = models.CharField(max_length=5, choices=SUBUNIDADE_CHOICES, verbose_name="Subunidade")
    situacao = models.CharField(max_length=50, blank=True, null=True, verbose_name="Situação")
    logradouro = models.CharField(max_length=100, verbose_name="Logradouro")
    numero = models.IntegerField(verbose_name="Número")
    complemento = models.CharField(max_length=50, null=True, blank=True, verbose_name="Complemento")
    bairro = models.CharField(max_length=100, verbose_name="Bairro")
    municipio = models.CharField(max_length=100, verbose_name="Município")
    uf = models.CharField(max_length=2, choices=UF_CHOICES ,verbose_name="UF")
    celulares = models.CharField(max_length=50, verbose_name="Celulares")
    telefone = models.CharField(max_length=50, null=True, blank=True, verbose_name="Telefone Residencial")
    recado = models.CharField(max_length=50, null=True, blank=True, verbose_name="Telefones para Recado")
    imagem = models.ImageField(upload_to="plano_chamada/%Y/%m/%d/", null=True, blank=True, verbose_name="Foto")
    created_at = models.DateField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateField(auto_now=True, verbose_name="Atualizado em")

    class Meta():
        ordering = ["post_grad__id"]
        verbose_name = "Plano de Chamada"
        verbose_name_plural = "Plano de Chamada"

    def __str__(self):
        return f"{self.post_grad} {self.nome_guerra}"