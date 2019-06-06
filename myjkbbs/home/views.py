from django.shortcuts import render
from .forms import RegisterForm
from .forms import LoginForm
from .models import Bbsuser
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Bbspost
from .models import Section
from .models import Comment

# Create your views here.
def test1(request):
    if request.session.has_key('username'):
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    else:
        nav1 = "注册"
        nav2 = "/register"
        nav3 = "登录"
        nav4 = "/login"
    return render(request, 'index1.html',{"nav1":nav1,"nav2":nav2,"nav3":nav3,"nav4":nav4})
def register(request):
    if request.session.has_key('username'):
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            passwd = form.cleaned_data["passwd"]
            email = form.cleaned_data["email"]
            Bbsuser.objects.create(username=username, passwd=passwd, email=email, isadmin=0)
            return HttpResponse('恭喜，注册成功了！')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {"form": form})
def login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            passwd=form.cleaned_data["passwd"]
            islogin=Bbsuser.objects.filter(username__exact = username,passwd__exact = passwd)
            if islogin:
                request.session['username'] = username
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')
    else:
        if request.session.has_key('username'):
            # 已登录
            return HttpResponseRedirect('/')
        else:
            form = LoginForm()
    return render(request,'login.html',{"form":form})
def logout(request):
    del request.session["username"]
    return HttpResponseRedirect('/')
def postlist(request):
    if request.session.has_key('username'):
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    else:
        nav1 = "注册"
        nav2 = "/register"
        nav3 = "登录"
        nav4 = "/login"
    posts = Bbspost.objects.values("id", "postname")
    return render(request, 'postlist.html',{"posts":posts,"nav1":nav1,"nav2":nav2,"nav3":nav3,"nav4":nav4})
def sectionlist(request):
    if request.session.has_key('username'):
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    else:
        nav1 = "注册"
        nav2 = "/register"
        nav3 = "登录"
        nav4 = "/login"
    sections = Section.objects.values("id", "secname")
    return render(request, 'sectionlist.html',{"sections": sections, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})
def sectionpostlist(request,secid):
    if request.session.has_key('username'):
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    else:
        nav1 = "注册"
        nav2 = "/register"
        nav3 = "登录"
        nav4 = "/login"
    posts = Bbspost.objects.filter(secid=secid).values("id", "postname", "uid")
    sections = Section.objects.filter(id=secid).values("secname", "detail")
    secname = list(sections)[0]["secname"]
    detail = list(sections)[0]["detail"]
    return render(request, 'sectionpostlist.html',{"posts": posts, "secname": secname, "detail": detail, "nav1": nav1, "nav2": nav2, "nav3": nav3,"nav4": nav4})
def postdetail(request,pid):
    if request.session.has_key('username'):
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    else:
        request.session['username']="游客"
        nav1 = "注册"
        nav2 = "/register"
        nav3 = "登录"
        nav4 = "/login"
    postdetail = Bbspost.objects.filter(id=pid).values()
    thissecid = list(postdetail)[0]["secid"]
    thissecname = list(Section.objects.filter(id=thissecid).values())[0]["secname"]
    # 编写回复显示
    uidall = []
    unameall = []
    pcidall = []
    tonameall = []
    commentall = []
    ismodify = []
    ischat = []
    comments = Comment.objects.filter(postid=pid).values()
    for item in comments:
        uidall.append(item["uid"])
        pcidall.append(item["pcid"])
        commentall.append(item["comment"])
        thisuname = list(Bbsuser.objects.filter(id=item["uid"]).values())[0]["username"]
        unameall.append(thisuname)
        # 评论修改--start-
        if request.session['username'] == thisuname:
            ismodify.append("<a href='/cmodify/" + str(item["id"]) + "'>可修改</a>")
        else:
            ismodify.append("")
        # 评论修改--end-
        # 回复其他用户--start-
        if request.session['username'] == thisuname:
            ischat.append("")
        else:
            ischat.append("<a href='/chat/" + str(item["id"]) + "'>回复TA</a>")
        # 回复其他用户--end-
        if (str(item["pcid"]) == "0"):
            thistoname = "楼主"
        else:
            thisuid = list(Comment.objects.filter(id=item["pcid"]).values())[0]["uid"]
            thistoname = list(Bbsuser.objects.filter(id=thisuid).values())[0]["username"]
        tonameall.append(thistoname)
    commentall = zip(unameall, tonameall, commentall,ismodify,ischat)
    '''
    a=[x,y,z]
    b=[c,d,e]
    zip(a,b)   -----------[(x,c),(y,d),(z,e)]
    '''
    return render(request, 'postdetail.html',{"commentall":commentall,"pid":pid,"thissecid":thissecid,"thissecname":thissecname,"postdetail":postdetail,"nav1":nav1,"nav2":nav2,"nav3":nav3,"nav4":nav4})
def postsub(request):
    if request.session.has_key('username') == False:
        return HttpResponseRedirect('/login')
    else:
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    # 查询所有板块ID与名称
    sectionall = Section.objects.values("id", "secname")
    secid = []
    secname = []
    for item in sectionall:
        secid.append(item["id"])
        secname.append(item["secname"])
    secidandname = zip(secid, secname)
    # 查询当前UID
    uid = list(Bbsuser.objects.filter(username=request.session['username']).values())[0]["id"]
    if request.method == "POST":
        content = request.POST["content"]
        thissecid = request.POST["secid"]
        postname = request.POST["postname"]
        Bbspost.objects.create(postname=postname, content=content, secid=thissecid, uid=uid)
        return HttpResponseRedirect('/posts')
    return render(request, 'postsub.html',{"secidandname": secidandname, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})
def comment(request,pid):
    if request.session.has_key('username')==False:
        return HttpResponseRedirect('/login')
    else:
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    postdetail = Bbspost.objects.filter(id=pid).values()
    postname = list(postdetail)[0]["postname"]
    uid = list(Bbsuser.objects.filter(username=request.session['username']).values())[0]["id"]
    if request.method == "POST":
        comment=request.POST["content"]
        Comment.objects.create(comment=comment, postid=pid, pcid=0,uid=uid)
        return HttpResponseRedirect('/postdetail/'+str(pid))
    return render(request, 'comment.html',{"postname":postname,"nav1":nav1,"nav2":nav2,"nav3":nav3,"nav4":nav4})
def cmodify(request,cid):
    if request.session.has_key('username') == False:
        return HttpResponseRedirect('/login')
    else:
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    # 根据评论ID查用户ID
    commentdetail = Comment.objects.filter(id=cid).values()
    thisuid = list(commentdetail)[0]["uid"]
    loginuid = list(Bbsuser.objects.filter(username=request.session['username']).values())[0]["id"]
    # 判断与当前登录用户是否一致，不一致退出
    if (thisuid != loginuid):
        return HttpResponseRedirect('/')
    # 根据评论ID查帖子ID、原评论内容
    postid = list(commentdetail)[0]["postid"]
    comment = list(commentdetail)[0]["comment"]
    if request.method == "POST":
        newcomment = request.POST["content"]
        Comment.objects.filter(id=cid).update(comment=newcomment)
        return HttpResponseRedirect('/postdetail/' + str(postid))
    return render(request, 'cmodify.html', {"comment": comment, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})
def chat(request,pcid):
    if request.session.has_key('username') == False:
        return HttpResponseRedirect('/login')
    else:
        nav1 = request.session['username']
        nav2 = "/"
        nav3 = "退出"
        nav4 = "/logout"
    oricommentdetail = Comment.objects.filter(id=pcid).values()
    pid = list(oricommentdetail)[0]["postid"]
    postdetail = Bbspost.objects.filter(id=pid).values()
    postname = list(postdetail)[0]["postname"]
    uid = list(Bbsuser.objects.filter(username=request.session['username']).values())[0]["id"]
    if request.method == "POST":
        comment = request.POST["content"]
        Comment.objects.create(comment=comment, postid=pid, pcid=pcid, uid=uid)
        return HttpResponseRedirect('/postdetail/' + str(pid))
    return render(request, 'chat.html', {"postname": postname, "nav1": nav1, "nav2": nav2, "nav3": nav3, "nav4": nav4})