from django.shortcuts import render, redirect
from django.views import View
from HomePage.models import intruduce
from AboutPage.models import aboutme, Update_Resume
from ResumePage.models import EDUCATION, WORK, SKILLS, SkiilsDescription, MoreText
from TestimonialsPage.models import quotation
from ContactPage.models import info, Copyright, descrip
from ContactPage.forms import ContactUsReceiveFormForm
from django.contrib import messages

class home(View):
    def get(self, request):
        Header = intruduce.objects.first()
        Aboutme = aboutme.objects.all()
        Edu = EDUCATION.objects.all()
        work = WORK.objects.all()
        skill = SKILLS.objects.first()
        des = SkiilsDescription.objects.first()
        koreh = MoreText.objects.first()
        rn = quotation.objects.all()
        inf = info.objects.first()
        foot = Copyright.objects.first()
        descript = descrip.objects.all()
        form = ContactUsReceiveFormForm
        resume = Update_Resume.objects.first()
        return render(request, 'base.html', {'Header': Header,
                                             'Aboutme': Aboutme,
                                             'edu': Edu,
                                             'work': work,
                                             'skills': skill,
                                             'des': des,
                                             'koreh': koreh,
                                             'rn': rn,
                                             'inf': inf,
                                             'foot': foot,
                                             'descript': descript,
                                             'contactform': form,
                                             'resume': resume,

                                             }
                      )



    def post(self, request):
        form = ContactUsReceiveFormForm(request.POST)
        if form.is_valid():
             contact = form.save()
             messages.success(request, 'Your message was sent, thank you!', 'success')
             return redirect('home:home')
