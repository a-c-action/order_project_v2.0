$(function (){
	//选择支付方式
	$(".check_1").click(function (){
		//判断当前元素是否为选中状态，如果是选中则取消选中
		if($(".check_1").attr("checked")){
			//修改为取消选中
			$(".check_1").removeAttr("checked")
				.attr("src","images_pay/pay_1.png");
            console.log(1)
            //如果不是选中状态，则判断2是否为选中状态，如果是，则控制1选中，控制2取消选中
		}else if($(".check_2").attr("checked")){

			$(".check_1").attr("checked","true")
				.attr("src","images_pay/pay_2.png");
			$(".check_2").removeAttr("checked",'true')
				.attr("src","images_pay/pay_3.png")
		}else{
		    $(".check_1").attr("checked","true")
				.attr("src","images_pay/pay_2.png");
		}
	})


    	//选择支付方式
	$(".check_2").click(function (){
		//判断当前元素是否为选中状态，如果是选中则取消选中
		if($(".check_2").attr("checked")){
			//修改为取消选中
			$(".check_2").removeAttr("checked")
				.attr("src","images_pay/pay_3.png");
            console.log(1)
            //如果不是选中状态，则判断2是否为选中状态，如果是，则控制1选中，控制2取消选中
		}else if($(".check_1").attr("checked")){

			$(".check_2").attr("checked","true")
				.attr("src","images_pay/pay_4.png");
			$(".check_1").removeAttr("checked",'true')
				.attr("src","images_pay/pay_1.png")
		}else{
		    $(".check_2").attr("checked","true")
				.attr("src","images_pay/pay_4.png");
		}


	})



    //结算
    $(".settlement").click(function(){
        if($(".check_1").attr("checked")){
            console.log(1)
            $('#qr_code1').css("display",'block');
            $(".qr_code1").click(function(){
            $('#qr_code1').css("display",'none');
            })
        }else if($(".check_2").attr("checked")){
            $('#qr_code2').css("display",'block');
            $(".qr_code2").click(function(){
            $('#qr_code2').css("display",'none');
            })
        }else{

            window.alert("请先选择付款方式");
        }

    })








})