# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import NregForm,modForm
from .models import Camper
from django.http import HttpResponseRedirect,HttpResponse
import requests
# Create your views here.
def mod(request):
    template = "reg.html"
    form = modForm(request.POST or None)
    context = {"form":form}

    if form.is_valid():
        phone = form.cleaned_data['phone']
        school = form.cleaned_data['school']
        gender = form.cleaned_data['gender']
        classNo = form.cleaned_data['classNo']
        created = Camper.objects.filter(phone=phone)
        if len(created)==0:
            return render(request, template, {'success':False,'contact':True})
        else:
            created[0].school = school
            created[0].gender = gender
            created[0].classNo = classNo
            created[0].save()
        return render(request, template, {'success':True,})
    else:
        return render(request, template,context)


def reg(request):

    template = "reg.html"
    form = NregForm(request.POST or None)
    
    context = {"form":form} 

    if form.is_valid():
        name = form.cleaned_data['name']
        student_id = form.cleaned_data['student_id']
        grade = form.cleaned_data['grade']
        phone = form.cleaned_data['phone']
        mail = form.cleaned_data['mail']
        created = Camper.objects.filter(student_id=student_id)
        if len(created)==0:
            JAVA=False
            Python=False
            C=False
            Javascript=False
            PHP=False
            HTML=False
            Ruby=False
            userlist = request.POST.getlist('users')
            for can in userlist:
                if can == 'Java':
                    JAVA=True
                    continue
                elif can == 'PHP':
                    PHP = True
                    continue
                elif can == 'Python':
                    Python = True
                    continue
                elif can == 'C/C++':
                    C = True
                    continue
                elif can == 'Javascript':
                    Javascript = True
                    continue
                elif can == 'Ruby':
                    Ruby = True
                    continue
                elif can == 'HTML/CSS':
                    HTML = True
            Pr=False
            Ps=False
            Ae=False
            Au=False
            FCP=False
            medialist = request.POST.getlist('mediaa')
            for can in medialist:
                if can == 'Pr':
                    Pr=True
                    continue
                elif can == 'Ps':
                    Ps = True
                    continue
                elif can == 'Ae':
                    Ae = True
                    continue
                elif 'Au' == can:
                    Au = True
                    continue
                elif 'Final Cut Pro' == can:
                    FCP = True 
            new_camper , created = Camper.objects.get_or_create(student_id=student_id,phone=phone,mail=mail,name=name,grade=grade,canJAVA=JAVA,canPHP=PHP,
                canC=C,canPython=Python,canJS=Javascript,canHTML=HTML,canRuby=Ruby,
                canPs=Ps,canPr=Pr,canAe=Ae,canAu=Au,canFCP=FCP)
            # send_simple_message(mail)
            send_complex_message(mail)
            return render(request, template, {'success':True,})
        else:
            return render(request, template, {'hhash':True,'form':form})
    return render(request,template,context)

def send_complex_message(mail):
    return requests.post(
        "https://api.mailgun.net/v3/shuttlecat.xyz/messages",
        auth=("api", "key-f642bf55652ab7ea0a038f08645640b2"),
        data={"from": " BUPT GoogleCamp <googlecamp@shuttlecat.xyz>",
              "to": mail,
              "cc": "buptjialin@icloud.com",
              "subject": "欢迎加入BUPT GoogleCamp",
              "html": '''<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<style>
h1,
h2,
h3,
h4,
h5,
h6,
p,
blockquote {
    margin: 0;
    padding: 0;
}
body {
    font-family: "Helvetica Neue", Helvetica, "Hiragino Sans GB", Arial, sans-serif;
    font-size: 13px;
    line-height: 18px;
    color: #737373;
    background-color: white;
    margin: 10px 13px 10px 13px;
}
table {
    margin: 10px 0 15px 0;
    border-collapse: collapse;
}
td,th { 
    border: 1px solid #ddd;
    padding: 3px 10px;
}
th {
    padding: 5px 10px;  
}

a {
    color: #0069d6;
}
a:hover {
    color: #0050a3;
    text-decoration: none;
}
a img {
    border: none;
}
p {
    margin-bottom: 9px;
}
h1,
h2,
h3,
h4,
h5,
h6 {
    color: #404040;
    line-height: 36px;
}
h1 {
    margin-bottom: 18px;
    font-size: 30px;
}
h2 {
    font-size: 24px;
}
h3 {
    font-size: 18px;
}
h4 {
    font-size: 16px;
}
h5 {
    font-size: 14px;
}
h6 {
    font-size: 13px;
}
hr {
    margin: 0 0 19px;
    border: 0;
    border-bottom: 1px solid #ccc;
}
blockquote {
    padding: 13px 13px 21px 15px;
    margin-bottom: 18px;
    font-family:georgia,serif;
    font-style: italic;
}
blockquote:before {
    content:"\201C";
    font-size:40px;
    margin-left:-10px;
    font-family:georgia,serif;
    color:#eee;
}
blockquote p {
    font-size: 14px;
    font-weight: 300;
    line-height: 18px;
    margin-bottom: 0;
    font-style: italic;
}
code, pre {
    font-family: Monaco, Andale Mono, Courier New, monospace;
}
code {
    background-color: #fee9cc;
    color: rgba(0, 0, 0, 0.75);
    padding: 1px 3px;
    font-size: 12px;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
}
pre {
    display: block;
    padding: 14px;
    margin: 0 0 18px;
    line-height: 16px;
    font-size: 11px;
    border: 1px solid #d9d9d9;
    white-space: pre-wrap;
    word-wrap: break-word;
}
pre code {
    background-color: #fff;
    color:#737373;
    font-size: 11px;
    padding: 0;
}
sup {
    font-size: 0.83em;
    vertical-align: super;
    line-height: 0;
}
* {
    -webkit-print-color-adjust: exact;
}
@media screen and (min-width: 914px) {
    body {
        width: 854px;
        margin:10px auto;
    }
}
@media print {
    body,code,pre code,h1,h2,h3,h4,h5,h6 {
        color: black;
    }
    table, pre {
        page-break-inside: avoid;
    }
}
</style>
<title>欢迎加入BUPT Google Camp</title>

</head>
<body>
<h1>欢迎加入BUPT Google Camp</h1>

<hr />

<h2>Hi~感谢您报名GoogleCamp，你的个人信息已经被系统自动保存。请坐等好消息吧...>.&lt;...</h2>

<hr />

<h1>FAQ</h1>

<hr />

<h4>GoogleCamp有什么活动？</h4>

<h5>加入GDG，参观Dev Fest…还有定期的茶话会，重大活动等你来。</h5>

<hr />

<h4>GDG是什么？</h4>

<h5>Google Developer Groups (GDGs) are for developers who are interested in Google's developer technology; everything from the Android, Chrome, Drive, and Google Cloud platforms, to product APIs like the Cast API, Maps API, and YouTube API.</h5>

<hr />

<h4>Dev Fest是什么？</h4>

<h5>GDG DevFests are large, community-run events that can offer speaker sessions across multiple product areas, all-day hack-a-thons, code labs, and more. In 2015, the official DevFest Season runs from September 01st through November 30th.</h5>

<hr />

<h4>成为GoogleCamp成员有什么要求吗？</h4>

<h5>只要是热爱Google，有Geek的热情都可以来参加。</h5>

<hr />

<p>Google Camp
Oct 14th, 2015</p>
</body>
</html>'''})

def send_simple_message(mail):
    return requests.post(
        "https://api.mailgun.net/v3/shuttlecat.xyz/messages",
        auth=("api", "key-f642bf55652ab7ea0a038f08645640b2"),
        data={"from": "BUPT GoogleCamp <googlecamp@shuttlecat.xyz>",
              "to": [mail, "buptjialin@icloud.com"],
              "subject": "GoogleCamp报名成功",
              "text": "Hi~感谢您报名GoogleCamp，你的个人信息已经被系统自动保存。请坐等好消息吧...>.<..."})