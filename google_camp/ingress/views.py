# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import ingressForm,logForm
from .models import Agent
from django.http import HttpResponseRedirect,HttpResponse
import requests

# Create your views here.
def regingress(request):
	form = ingressForm(request.POST or None)
	context = {"form":form} 

	if form.is_valid():
		name = form.cleaned_data['name']
		eat = form.cleaned_data['eat']
		level = form.cleaned_data['level']
		phone = form.cleaned_data['phone']
		password = form.cleaned_data['password']
		password2 = form.cleaned_data['password2']
		if password!=password2:
			return render(request,'ingress.html',{"pw":True,"form":form} )
		mail = form.cleaned_data['mail']
		created = Agent.objects.filter(name=name)
		if len(created)==0:
			new_agent , created = Agent.objects.get_or_create(name=name,eat=eat,level=level,phone=phone,mail=mail,password=password)
			send_complex_message(mail)
			return render(request,'ingress.html',{"success":True} )
		else:
			return render(request,'ingress.html',{"repeat":True,"form":form} )
	return render(request,'ingress.html',context)

def join(request):
	form = logForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['name']
		password = form.cleaned_data['password']
		print name
		# vrify
		agents = Agent.objects.filter(name=name)
		if len(agents) == 0:
			# No Agent
			print 'CCC'
			return render(request,'ingress.html',{"error":True})
		else:
			agent = agents[0]
			# password error
			if agent.password != password:
				print 'QQQ'
				return render(request,'ingress.html',{"error":True})
			else:
				agent.join = True
				agent.save()
				join = Agent.objects.filter(join=True)
				num = len(join)
				unjoin = Agent.objects.filter(join=False)
				return render(request,'event.html',{"my":agent,"join":join,"unjoin":unjoin,"num":num})	
	else:
		print 'NNN'
		return render(request,'ingress.html')

def event(request):
	form = logForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['name']
		password = form.cleaned_data['password']
		# vrify
		agents = Agent.objects.filter(name=name)
		if len(agents) == 0:
			# No Agent
			return render(request,'ingress.html',{"error":True})
		else:
			agent = agents[0]
			# password error
			if agent.password != password:
				return render(request,'ingress.html',{"error":True})
			else:
				join = Agent.objects.filter(join=True)
				num=len(join)
				unjoin = Agent.objects.filter(join=False)
				return render(request,'event.html',{"my":agent,"join":join,"unjoin":unjoin,"num":num})	
	else:
		return render(request,'ingress.html')

def send_complex_message(mail):
    return requests.post(
        "https://api.mailgun.net/v3/shuttlecat.xyz/messages",
        auth=("api", "key-f642bf55652ab7ea0a038f08645640b2"),
        data={"from": " BUPT GoogleCamp <googlecamp@shuttlecat.xyz>",
              "to": mail,
              "cc": "buptjialin@icloud.com",
              "subject": "北邮吃吃吃等你来",
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
<title>北邮吃吃吃等你来</title>

</head>
<body>




<h2>Hi~ 如果你收到了这封邮件，就表示我们已经收到了你的注册。</h2>

<hr />

<h3>接下来请您这样做：</h3>

<ol>
<li>在&lt;专吃八八八>或者&lt;绿军吹水群>中联系Cater#13@BUPT,以证明您的身份。</li>
<li>您将收到关于起8⃣️具体时间地点的通知。</li>
<li>登录<a href="http://115.28.28.165/ingress">刚刚注册的网页</a>查看最新动态。</li>
</ol>


<hr />

<p>Google Camp
Oct 24th, 2015</p>
</body>
</html>'''})