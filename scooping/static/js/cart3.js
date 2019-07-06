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


$(function () {
    $("#aVerImg").click(function () {
        $("#imgVer").attr("src","/userinfo/verify_code"+Math.random())
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
    $("#btnfind").click(function () {
        if(finduname()){
        alert("用户为空或不存在")
        }else if(finduemail()){
            alert("用户邮箱为空或不存在")
        }else if(finduphone()){
            alert("用户手机号为空或不存在")
        }else if(findpassword()){
            alert("新密码为空或强度太低")  
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
            var csrf = $("[name = 'csrfmiddlewaretoken']").val();
            var params = "&uname=" + uname + "&uemail=" + uemail + "&uphone=" + uphone + "&upassword=" + upassword + "&csrfmiddlewaretoken=" + csrf;
            xhr.send(params);
        }
    })
});
