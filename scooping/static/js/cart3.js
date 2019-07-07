function finduname() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/finduname?uname=" + $("#runame").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "0") {
                ret = true;
                $("#uname-show").html("用户为空,请输入").css("color", "red");
            }else if(xhr.responseText == "1"){
                ret = true;
                $("#uname-show").html("用户不存在").css("color", "red");
            }else {
                $("#uname-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function finduemail() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/finduemail?uname="+$("#runame").val()+"&uemail=" + $("#ruemail").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "3") {
                ret = true;
                $("#uname-show").html("用户为空,请输入").css("color", "red");
            }else if(xhr.responseText == "0"){
                ret = true;
                $("#uemail-show").html("邮箱为空,请输入").css("color", "red");
            }else if(xhr.responseText == "1"){
                ret = true;
                $("#uemail-show").html("邮箱或用户不存在,请输入").css("color", "red");
            }else if(xhr.responseText == "4"){
                ret = true;
                $("#uemail-show").html("邮箱和用户不匹配").css("color", "red");
            }else {
                $("#uemail-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function finduphone() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/finduphone?uname="+$("#runame").val()+"&uphone=" + $("#ruphone").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "3") {
                ret = true;
                $("#uname-show").html("用户为空,请输入").css("color", "red");
            }else if(xhr.responseText == "0"){
                ret = true;
                $("#uphone-show").html("手机号为空,请输入").css("color", "red");
            }else if(xhr.responseText == "1"){
                ret = true;
                $("#uphone-show").html("手机号或用户不存在,请输入").css("color", "red");
            }else if(xhr.responseText == "4"){
                ret = true;
                $("#uphone-show").html("手机号和用户不匹配").css("color", "red");
            }else {
                $("#uphone-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function findpassword() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/findpassword?uname="+$("#runame").val()+"&password=" + $("#rpassword").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "5") {
                ret = true;
                $("#uname-show").html("用户为空").css("color", "red");
            }else if(xhr.responseText == "3") {
                ret = true;
                $("#uname-show").html("用户不存在").css("color", "red");
            }else if(xhr.responseText == "0") {
                ret = true;
                $("#upassword-show").html("新密码为空,请输入").css("color", "red");
            }else if(xhr.responseText == "1"){
                ret = true;
                $("#upassword-show").html("新密码强度太低").css("color", "red");
            }else if(xhr.responseText == "2"){
                ret = true;
                $("#upassword-show").html("新密码不能和旧密码一致").css("color", "red");
            }else {
                $("#upassword-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function check_action_code(){
    var setmsg = String($("#smscode").val());
    var getmsg = String($("#displaysmscode").html());
    if(setmsg.length == 0){
        $("#uaction-show").html("激活码为空").css("color","red");
        return true
    }else{
        if(setmsg == getmsg){
            $("#displaysmscode").css('display','none');
            return false;
        }else {
            $("#uaction-show").html("激活码错误").css("color","red");
            return true;
        }
    }
}

$(function () {
    $("#aVerImg").click(function () {
        $("#imgVer").attr("src","/userinfo/verify_code"+Math.random())
    });
    $(".inputVer").click(function () {
        // var now = new Date();
        var i = 60;
        var timer = setInterval(function () {
            $(".inputVer").html(i + "s后可再获取");
            $(".inputVer").css("background", "gray");
            i--;
            if (i < 0) {
                clearInterval(timer);
                $(".inputVer").html("获取验证码");
                $(".inputVer").css("background", "#2020f9e6");
                $(".inputVer").attr("disabled", false)
            }
        }, 1000);
        $.ajax({
            url:'/userinfo/smscode1',
            data:{
                phone:$("#ruphone").val()
            },
            type:"get",
            dataType:'json',
            success:function (data) {
                $("#displaysmscode").html(data.number)
            }
        });
        $(".inputVer").attr("disabled", true)
    });
    $("#runame").blur(function () {
        finduname();
    });
    $("#ruemail").blur(function () {
        finduemail();
    });
    $("#ruphone").blur(function () {
        finduphone();
    });
    $("#rpassword").blur(function () {
        findpassword();
    });
    $("#smscode").blur(function () {
        check_action_code();
    });
    $("#btnfind").click(function () {
        if(finduname()){
        alert("用户为空或不存在")
        }else if(finduemail()){
            alert("用户邮箱为空或不存在")
        }else if(finduphone()){
            alert("用户手机号为空或不存在")
        }else if(findpassword()){
            alert("新密码为空或强度太低或新旧密码一致")
        }else if(check_action_code()){
            alert("激活码为空或错误")
        }else {
            var xhr = createXhr();
            xhr.open("post", "/userinfo/modifyPassword", true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    alert(xhr.responseText);
                    location.href="/userinfo/login"
                }
            };
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            var uname = $("#runame").val();
            var uemail = $("#ruemail").val();
            var uphone = $("#ruphone").val();
            var upassword = $("#rpassword").val();
            var action_code = $("#smscode").val();
            var action_code1 = $("#displaysmscode").html();
            var csrf = $("[name = 'csrfmiddlewaretoken']").val();
            var params = "&uname=" + uname + "&uemail=" + uemail + "&uphone=" + uphone + "&upassword=" + upassword + "&action_code=" + action_code + "&action_code1=" + action_code1 + "&csrfmiddlewaretoken=" + csrf;
            xhr.send(params);
        }
    })
});
