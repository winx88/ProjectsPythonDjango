#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
## @package models
# @author: winx
# @note: Klasy do mapowania na tabele bazy danych

## Klasa do przechowywania danych o drużynie
# @param imgTeam: logo drużyny
# @param nameOfTeam: nazwa drużyny
# @param phoneNumber: numer do kapitana drużyny

class Team(models.Model):
    imgTeam = models.FileField(upload_to="images/",null=True) 
    nameOfTeam = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15,null=True)
    def get_absolute_url(self):
                return "/druzyny/" 

## Klasa do przechowywania danych o zawodnikach
# @param pesel: pesel zawodnika
# @param name: imię zawodnika
# @param surname: nazwisko zawodnika
# @param email: emial zawodnika
# @param imgPlayer: zdjecię zawodnika
# @param teamid: referencja do drużyny
# @param dateOfBrith: data urodzin zawodnika
# @param city: miasto adresowe zawodnika
# @param address: adres zawodnika
# @param iscaptain: jest kapitanem

class Player(models.Model):
    pesel = models.CharField(max_length=11)
    loginPlayer = models.ForeignKey(User)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=30,null=True)
    imgPlayer=models.FileField(upload_to="images/",null=True)
    teamid = models.ForeignKey(Team,null=True)
    dateOfBrith = models.DateField()
    city = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=50,null=True)
    iscaptain = models.BooleanField()
    def get_absolute_url(self):
                return "/profil/" 

## Klasa do przechowywania danych o rozegranych meczach
# @param teamid: referencja do drużyny
# @param points: punkty w tabeli wyników
# @param matches: ilość rozegranych meczy
# @param lostGoals: ilość straconych goli
# @param scoredGoals: ilość strzelonych bramek
# @param failMaches: ilość przegranych meczy
# @param winMatches: ilość wygranych meczy
# @param drawMatches: ilość zremisowanych meczy
# @param possition: pozycja w tabeli wyników
   
class TableResults(models.Model):
    teamid = models.ForeignKey(Team)
    points = models.IntegerField()
    matches = models.IntegerField()
    lostGoals = models.IntegerField()
    scoredGoals = models.IntegerField()
    failMaches = models.IntegerField()
    winMatches = models.IntegerField()
    drawMatches = models.IntegerField()
    possition = models.IntegerField()
    def get_absolute_url(self):
                return "/tabela/" 
    
## Klasa do przechowywania danych o boiskach
# @param name: nazwa boiska
# @param address: adres boiska
# @param city: miasto adresowe boiska
# @param phoneNumberToJanitor: numer do dozorcy boiska w celu rezerwacjii   
    
class FootballPitch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30,null=True)
    phoneNumberToJanitor = models.CharField(max_length=15,null=True)
    
## Klasa do przechowywania danych o rezultacie spotkania
# @param team1: referencja do pierwszej drużyny w spotkaniu
# @param team2: referencja do drugiej drużyny w spotkaniu
# @param dateOfMatch: data meczu wraz z godziną
# @param placeOfMatch: miejsce rozgrywki referencja na boiska
# @param resultTeam1: wynik pierwszej drużyny
# @param resultTeam2: wynik drugiej drużyny
# @param isconfirmTeam1: potwierdzony wynik przez druzyne pierwsza
# @param isconfirmTeam2: potwierdzony wynik przez druzyne druga       
    
class MatchesResults(models.Model):
    team1 = models.ManyToManyRel(Team)
    team2 = models.ManyToManyRel(Team)
    dateOfMatch = models.DateTimeField()
    placeOfMatch = models.ForeignKey(FootballPitch)
    resultTeam1 = models.IntegerField()
    resultTeam2 = models.IntegerField()
    isconfirmTeam1 = models.BooleanField()
    isconfirmTeam2 = models.BooleanField()
    
    

    
