function checkuaccount() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/checkuaccount?uaccount=" + $("#uaccount").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "0") {
                ret = true;
                $("#uaccount-show").html("用户为空,请输入").css("color", "red");
            } else if (xhr.responseText == "1") {
                ret = true;
                $("#uaccount-show").html("用户不存在，请注册").css("color", "red");
            } else if (xhr.responseText == "2") {
                ret = true;
                $("#uaccount-show").html("用户已登录").css("color", "red");
            } else {
                $("#uaccount-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function checkupassword() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/checkupassword?uaccount=" + $("#uaccount").val() + "&upassword=" + $("#upassword").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "0") {
                ret = true;
                $("#uaccount-show").html("用户为空,请输入").css("color", "red");
            } else if (xhr.responseText == "1") {
                ret = true;
                $("#upassword-show").html("密码为空,请输入").css("color", "red");
            } else if (xhr.responseText == "3") {
                ret = true;
                $("#upassword-show").html("密码错误").css("color", "red");
            } else if (xhr.responseText == "4") {
                ret = true;
                $("#uaccount-show").html("该用户不存在，请注册").css("color", "red");
            } else {
                $("#upassword-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

function checkverifycode() {
    var ret = false;
    var xhr = createXhr();
    var url = "/userinfo/check_verify_code?verify_code=" + $("#check_verify_code").val();
    xhr.open("get", url, false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            if (xhr.responseText == "0") {
                ret = true;
                $("#verifycode-show").html("验证码为空,请输入").css("color", "red");
            } else if (xhr.responseText == "1") {
                ret = true;
                $("#verifycode-show").html("验证码错误").css("color", "red");
            } else {
                $("#verifycode-show").html("");
            }
        }
    };
    xhr.send(null);
    return ret;
}

$(function () {
    $("#aVerImg").click(function () {
        $("#imgVer").attr("src", "/userinfo/verify_code" + Math.random())
    });
    $("#uaccount").blur(function () {
        checkuaccount();
    });
    $("#upassword").blur(function () {
        checkupassword();
    });
    $("#check_verify_code").blur(function () {
        checkverifycode();
    });
    $("#loginbtn").click(function () {
        if (checkuaccount()) {
            alert("用户不存在或已登录")
        } else if (checkupassword()) {
            alert("密码为空或错误")
        } else if (checkverifycode()) {
            alert("验证码为空或错误")
        } else {
            var xhr = createXhr();
            xhr.open("post", "/userinfo/checklogin", true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    alert(xhr.responseText);
                    location.href = "/"
                }
            };
            xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            var remember = $("#loginbox").val();
            var uaccount = $("#uaccount").val();
            var upassword = $("#upassword").val();
            var verify_code = $("#check_verify_code").val();
            var csrf = $("[name = 'csrfmiddlewaretoken']").val();
            var params = "remember=" + remember + "&uaccount=" + uaccount + "&upassword=" + upassword + "&verify_code=" + verify_code + "&csrfmiddlewaretoken=" + csrf;
            xhr.send(params);
        }
    })
});
