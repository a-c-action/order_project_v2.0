$(function(){
    $(".orderconsel").click(function (){
		//取消整个商品记录

        orderid=$(this).parents(".contentorder").find("#headorder p label").html()
        console.log(orderid)
        var msg={
            "orderid":orderid
        }
		$.get("/order/cancel",msg,function(data){
		    alert(data)
//		    window.location.href=''
		})
//		$(this).parents(".contentorder").remove();
	})
	$(".orderdelete").click(function (){
		//移除整个商品记录

        orderid=$(this).parents(".contentorder").find("#headorder p label").html()

        console.log(orderid)
        var msg={
            "orderid":orderid
        }
		$.get("/order/delete",msg,function(data){
		    alert(data)
		})
		$(this).parents(".contentorder").remove();
	})
})
