function checkuname() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/checkuname?uname=" + $("#myname").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "1") {
                ret = true;
                $("#uname-show").html("用户名已存在").css("color", "red");
            } else {
                $("#uname-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function checkuemail() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/checkuemail?uemail=" + $("#myemail").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "1") {
                ret = true;
                $("#uemail-show").html("邮箱已存在").css("color", "red");
            } else {
                $("#uemail-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function checkuphone() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/checkuphone?uphone=" + $("#myphone").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "1") {
                ret = true;
                $("#uphone-show").html("手机号码已存在").css("color", "red");
            } else {
                $("#uphone-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function checkuname1() {
    var userinput = $(".userInput").val()
    if (userinput.length == 0) {
        $(".pass-item-error1").css("display", "inline");
        return true;
    }
    var regex = /^[a-zA-Z][a-zA-Z0-9_-]{3,15}$/;
    if (!regex.test(userinput)) {
        $(".pass-item-error1").css("display", "inline");
        return true;
    }
    $(".pass-item-error1").css("display", "none");
    return false;
}

function checkuemail1() {
    var input = $(".emailInput").val()
    if (input.length == 0) {
        $(".pass-item-error2").css("display", "inline");
        return true;
    }
    //邮箱正则表达式
    var regex = /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
    //判断
    if (!regex.test(input)) {
        $(".pass-item-error2").css("display", "inline");
        return true;
    }
    $(".pass-item-error2").css("display", "none");
    return false;
}

function checkuphone1() {
    var teleinput = $(".teleInput").val()
    if (teleinput.length == 0) {
        $(".pass-item-error5").css("display", "inline");
        return true;
    }
    var regex = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
    if (!regex.test(teleinput)) {
        $(".pass-item-error5").css("display", "inline");
        return true;
    }
    $(".pass-item-error5").css("display", "none");
    return false;
}

function checkpasswordInput() {
    var pswdinput = $(".passwordInput").val()
    if (pswdinput.length == 0) {
        $(".pass-item-error3").css("display", "inline");
        return true;
    }
    var regex = /^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$/;
    //最少6位，包括至少1个大写字母，1个小写字母，1个数字，1个特殊字符
    if (!regex.test(pswdinput)) {
        $(".pass-item-error3").css("display", "inline");
        return true;
    }
    $(".pass-item-error3").css("display", "none");
    return false;
}

function checkrestartpasswordInput() {
    var restartInput = $(".restartpasswordInput").val()
    var passwordinput = $(".passwordInput").val()
    if (restartInput != passwordinput) {
        $(".pass-item-error4").css("display", "inline");
        return true;
    }
    $(".pass-item-error4").css("display", "none");
    return false;
}

function checkverify_code(){
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/checkverifycode?verify_code=" + $("#check_verify_code").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "0") {
                ret = true;
                $("#uverify-show").html("验证码为空").css("color", "red");
            } else if(xhr.responseText == "1"){
                ret = true;
                $("#uverify-show").html("验证码错误").css("color", "red");
            }else {
                $("#uverify-show").html("");
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
    $(".togg").click(function () {
        if ($(".TeamServices").css("display") == "none") {
            $(".TeamServices").css("display", "block");
        } else {
            $(".TeamServices").css("display", "none");
        }
    });

    $(".checkAll").click(function () {
        if ($(this).attr("checked")) {
            $(this).removeAttr("checked").attr("src", "/static/images/register/product_normal.png");
        } else {
            $(this).attr("checked", "true").attr("src", "/static/images/register/product_true.png");
        }
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
            url:'/userinfo/smscode',
            data:{
                phone:$("#myphone").val()
            },
            type:"get",
            dataType:'json',
            success:function (data) {
                $("#displaysmscode").html(data.number)
            }
        });
        $(".inputVer").attr("disabled", true)
    });

    $("#aVerImg").click(function () {
        $("#imgVer").attr("src","/userinfo/verify_code"+Math.random())
    });

    /*$(".userInput").blur(function(){
        var userinput = $(".userInput").val()
        if(userinput.length==0){
            $(".pass-item-error1").css("display","inline");
            return false;
        }
        var regex = /^[a-zA-Z][a-zA-Z0-9_-]{3,15}$/;
        if(!regex.test(userinput)){
            $(".pass-item-error1").css("display","inline");
            return false;
        }
        $(".pass-item-error1").css("display","none");
        return true;
    })*/

    /*$(".emailInput").blur(function(){
        var input=$(".emailInput").val()
        if(input.length==0){
            $(".pass-item-error2").css("display","inline");
            return false;
            }
        //邮箱正则表达式
        var regex = /^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/;
        //判断
        if(!regex.test(input)){
            $(".pass-item-error2").css("display","inline");
            return false;
        }
        $(".pass-item-error2").css("display","none");
        return true;
    })*/

    /*$(".passwordInput").blur(function(){
        var pswdinput=$(".passwordInput").val()
        if(pswdinput.length==0){
            $(".pass-item-error3").css("display","inline");
            return false;
            }
        var regex = /^.*(?=.{6,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$/;
        //最少6位，包括至少1个大写字母，1个小写字母，1个数字，1个特殊字符
        if(!regex.test(pswdinput)){
            $(".pass-item-error3").css("display","inline");
            return false;
        }
        $(".pass-item-error3").css("display","none");
        return true;
    })*/

    /*$(".teleInput").blur(function(){
        var teleinput=$(".teleInput").val()
        if(teleinput.length==0){
            $(".pass-item-error5").css("display","inline");
            return false;
            }
        var regex = /^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\d{8}$/;
        if(!regex.test(teleinput)){
            $(".pass-item-error5").css("display","inline");
            return false;
        }
        $(".pass-item-error5").css("display","none");
        return true;
    })*/

    /*$(".restartpasswordInput").blur(function(){
        var restartInput = $(".restartpasswordInput").val()
        var passwordinput = $(".passwordInput").val()
        if(restartInput != passwordinput){
            $(".pass-item-error4").css("display","inline");
            return false;
        }
        $(".pass-item-error4").css("display","none");
        return true;
    })*/

    $("#myname").blur(function () {
        checkuname();
        checkuname1();
    });
    $("#myemail").blur(function () {
        checkuemail();
        checkuemail1();
    });
    $("#myphone").blur(function () {
        checkuphone();
        checkuphone1();
    });
    $("#mypassword").blur(function () {
        checkpasswordInput();
    });
    $("#mypassword2").blur(function () {
        checkrestartpasswordInput();
    });
    $("#check_verify_code").blur(function () {
        checkverify_code();
    });

    $("#smscode").blur(function () {
        check_action_code();
    });

    /*function checkverify_code(){
        $("#check_verify_code").blur(function () {
            var verify_code = $("#check_verify_code").val();
            if(verify_code.length==0){
                return true
            }
            $.ajax({
                url:"/userinfo/checkverify_code",
                type:"get",
                dataType:"json",
                async:false,
                success:function (data) {
                    $(data).each(function (i,obj) {
                        verify_code1 = obj.verify_code;
                        verify_code = verify_code.toLowerCase();
                        verify_code1 = verify_code1.toLowerCase();
                        console.log(verify_code);
                        console.log(verify_code1);
                        if(verify_code != verify_code1){
                            return true
                        }else {
                            return true
                        }
                    });
                },
                error:function () {
                    verify_code1 = "";
                }
            });
        });
    }*/
    // checkverify_code();

    $("#btnRegister").click(function () {
        if (checkuname()) {
            alert("用户名称已存在,不能重复注册");
        } else if (checkuname1()) {
            alert("用户名为空或错误");
        } else if (checkuemail()) {
            alert("邮箱已存在,不能重复注册");
        } else if (checkuemail1()) {
            alert("邮箱为空或错误");
        } else if (checkpasswordInput()) {
            alert("密码为空或强度不够");
        } else if (checkrestartpasswordInput()) {
            alert("两次密码输入不一致");
        } else if (checkuphone()) {
            alert("手机号已存在,不能重复注册");
        } else if (checkuphone1()) {
            alert("手机号为空或错误");
        } else if(checkverify_code()){
            alert("验证码为空或错误")
        } else if(check_action_code()){
            alert("激活码为空或错误")
        } else if($("#myservice[checked]").length == 0){
            alert("请阅读服务条款并勾选");
        } else {
            var xhr = createXhr();
            xhr.open("post", "/userinfo/reguser", true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    alert(xhr.responseText);
                    location.href="/userinfo/login"
                }
            };
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            var uname = $("#myname").val();
            var uemail = $("#myemail").val();
            var uphone = $("#myphone").val();
            var password = $("#mypassword").val();
            var password2 = $("#mypassword2").val();
            var verify_code = $("#check_verify_code").val();
            var action_code = $("#smscode").val();
            var action_code1 = $("#displaysmscode").html();
            var csrf = $("[name = 'csrfmiddlewaretoken']").val();
            var params = "uname=" + uname + "&uemail=" + uemail + "&uphone=" + uphone + "&password=" + password + "&password2=" + password2 + "&verify_code=" + verify_code + "&action_code=" + action_code + "&action_code1=" + action_code1 +  "&csrfmiddlewaretoken=" + csrf;
            xhr.send(params);
        }
    });
});
