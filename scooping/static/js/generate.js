function param() {
    var params_dic = {};
    $(".checkItem[checked]").each(function (i) {
        var param = $(this).parents(".item").find("#cname").html();
        params_dic["cname" + i] = param;
        i++;
    });
    return params_dic
}

$(function () {
    $("#generatebtn").click(function () {
        params = param();
        if (Object.keys(params).length == 0) {
            alert("请先选择产品")
        } else {
            params["cart_table"] = $("#cart_table").val();
            if (params["cart_table"] == "") {
                alert("请先选择桌号")
            } else {
                params["csrfmiddlewaretoken"] = $("[name='csrfmiddlewaretoken']").val();
                var params_length = Object.keys(params).length;
                params["number"] = params_length - 1;
                var whether = $("input[name=show]:checked").val();
                if (whether == "是") {
                    params["whether"] = whether;
                    var takename = $("#takename").val();
                    var takephone = $("#takephone").val();
                    var takeaddress = $("#takeaddress").val();
                    var takenumber = $("#takenumber").val();
                    params["takename"] = takename;
                    params["takephone"] = takephone;
                    params["takeaddress"] = takeaddress;
                    params["takenumber"] = takenumber;
                } else {
                    params["whether"] = whether;
                }
                $.ajax({
                    url: '/checkout/generate',
                    data: params,
                    type: "post",
                    dataType: "json",
                    async: true,
                    success: function (data) {
                        alert("订单生成完成！");
                        var params_id = {'orderid': data};
                        $.ajax({
                            url: '/payment',
                            data: params_id,
                            type: "get",
                            dataType: "html",
                            async: true,
                            success: function (data) {
                                location.href = "/payment"
                            },
                            error: function (data) {
                                alert(data);
                            }
                        })
                    },
                    error: function (data) {
                        alert(data);
                    }
                })
            }
        }
    })
});
