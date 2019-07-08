$(function(){
    $.get("/checkout/list",function(data){
        html=''
        console.log("-----",data);
        data1=JSON.parse(data)
        $(data1).each(function(i,obj){
            console.log(obj)
            html+=`
                <div class="content">
				<!--商品记录-->

				<div class="item">
					<div class="check">
						<img src="${ '/static/images/checkout/product_normal.png' }" class="checkItem">

					</div>
					<div class="gname">
						<img src="${'/static'+obj.pic}">
						<p>       </p>
						<p>${ obj.cname }</p>
						<p>　　　　</p>
					</div>
					<div class="gprice">
						<h3>会员专享价</h3>
						<p>￥ ${ obj.cmarket_price }</p>
					</div>
					<div class="gcount">
						<!--阻止超链接默认事件-->
						<a href="javascript:void(0)" class="minus">-</a>
						<input type="text" value="1">
						<a href="javascript:void(0)" class="add">+</a>

					</div>
					<div class="gsum">￥ ${ obj.cprice }</div>
					<div class="action">移除</div>

				</div>

			</div>

            `
            $(".content").html(html)
        })
    })
})