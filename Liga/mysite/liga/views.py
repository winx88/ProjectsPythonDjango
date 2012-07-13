#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from mysite.liga.models import Player, TableResults, Team, MatchesResults
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.core.exceptions import *
from django import forms
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
MEDIA_URL = '/site_media/static/img/'

class ProfilForm(ModelForm):
        #loginPlayer = forms.CharField(label='Login',required=True,)
        name = forms.CharField(label='Imię', max_length=15,required=True,)
        surname = forms.CharField(label='Nazwisko',max_length=30,required=True)
        pesel = forms.CharField(label='PESEL',max_length=11, required=True)
        dateOfBrith = forms.DateField(label='Data urodzenia',required=True)
        address = forms.CharField(label='Adres',max_length=50,required=False)
        city = forms.CharField(label='Miasto',max_length=30,required=False)
        iscaptain = forms.BooleanField(label='Kapitan drużyny',required=False)
        #imgPlayer = forms.ImageField()

        class Meta:
                model = Player
                fields = ('pesel','name','surname','dateOfBrith','address','city','iscaptain')


def manage_profil(request,tag):
    UserObj =  User.objects.get(username=tag)
    filePath = ''

    try:
        p = Player.objects.get(loginPlayer=UserObj.id)
    except ObjectDoesNotExist:
        p = Player()
        p.loginPlayer_id=UserObj.id

    try:
        filePath = str(p.imgPlayer).split('/')[1]
    except IndexError:
        filePath = 'd.jpg'


    if request.method == "POST":
        form = ProfilForm(request.POST,request.FILES,instance=p)
        if form.is_valid():
            form.save()
    else:
        form = ProfilForm(instance=p)
    return render_to_response("profil.html", {
        "form": form,'filePath':filePath,'MEDIA_URL' : MEDIA_URL,},context_instance=RequestContext(request))

def create_pdf(request):

        response=HttpResponse(mimetype='application/pdf')
        response['Content-Disposition']='attachment; filename=tabela_wynikow.pdf'
        mypdf=SimpleDocTemplate(response,rightMargin=72,leftMargin=72,topMargin=72,bottomMargin=18,title="TABELA WYNIKÓW")
        styles=getSampleStyleSheet()
        pdfmetrics.registerFont(TTFont('Dejavu-Italic','DejaVuSerif-Bold.ttf'))
        pdfmetrics.registerFont(TTFont('Dejavu','DejaVuSerif.ttf'))


        styleN = styles["Heading2"]
        styleN.fontName = 'Dejavu-Italic'

        data = []
        headTable = ["lp","Drużyna","Mecze","Punkty","Zwycięstwa","Remisy","Porażki","Strzelone bramki", "Stracone bramki"]
        data.append(headTable)
       
        t =  TableResults.objects.order_by('possition')
        elements=[]

        for e in t:
                temp = [str(e.possition),Team.objects.get(pk=e.teamid.id).nameOfTeam,
                        str(e.matches),str(e.points),str(e.winMatches),
                        str(e.drawMatches),str(e.failMaches),str(e.scoredGoals),str(e.lostGoals)]
                data.append(temp)
        t = Table(data)
        t.setStyle(TableStyle([('FONT',(0,0),(-1,0),'Dejavu-Italic',9),
                               ('BACKGROUND',(0,0),(-1,0),colors.gray),
                               ('FONT',(0,1),(-1,-1),'Dejavu',9),
                               ('ALIGN',(0,0),(-1,-1), 'CENTER')]))

        elements.append(t)
        mypdf.build(elements)
        return response


def manage_team(request):
        t1 = []
        t2 = []
        t3 = []
        count = Team.objects.count()
        player = Player.objects.all()
        for i in range(1,count+1):
                if i%3 == 1:
                        t1.append(Team.objects.get(id=i))
                if i%3 == 2:
                        t2.append(Team.objects.get(id=i))
                if i%3 == 0:
                        t3.append(Team.objects.get(id=i))
        return render_to_response("team.html", {
               "player" : player,"team1": t1,"team2" : t2, "team3": t3,},context_instance=RequestContext(request))

def manage_match(request,tag):
        UserObj =  User.objects.get(username=tag)

        try:
            p = Player.objects.get(loginPlayer=UserObj.id)
        except ObjectDoesNotExist:
            msg = 'Nie masz zadnych meczy!'
            return render_to_response("mecze.html",{"msg":msg,},context_instance=RequestContext(request))
