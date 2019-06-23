$(function (){
	$(".togg").click(function(){
		if($(".TeamServices").css("display") == "none"){
			$(".TeamServices").css("display","block");
		}else{
			$(".TeamServices").css("display","none");
		}
	})
	$(".checkAll").click(function (){
		if($(this).attr("checked")){
			$(this).removeAttr("checked").attr("src","./images/product_normal.png");
		}else{
			$(this).attr("checked","true").attr("src","./images/product_true.png");
		}
	})
	$(".inputVer").click(function(){
		var now = new Date();
		console.log(now)
		var i=60;
		var timer=setInterval(function(){
			$(".inputVer").html(i+"s后可再获取")
			$(".inputVer").css("background","gray")
			i--;
			if(i<0){
				clearInterval(timer);
				$(".inputVer").html("获取验证码")
				$(".inputVer").css("background","#2020f9e6")
				$(".inputVer").attr("disabled",false)	
			}
		},1000)	
		$(".inputVer").attr("disabled",true)		
	})
})
