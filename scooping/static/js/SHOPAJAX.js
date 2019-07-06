

$(function(){
    console.log("jfdihoilalalalalal")
    var count=Number($(".cmd").html())
    var si=$("[name='shoe_item_1']").val()
    var caipin=[]
    for(var i=1;i<count+1;i++){
           name='shoe_item_'+i
           countsigle='quantity_'+i
           var info=$("[name='shoe_item_"+i+"']").val()
           var count1=$("[name='quantity_"+i+"']").val()
           var count2=String(count1)
           var obj={
            "name":info
           }
           obj.count=count2
           caipin.push(obj)
           console.log(info,count1)
           console.log(name)
           console.log(caipin)

    }


//    $.get("/checkout/new",msg,function(data){
//        alert(data)
//    })
})