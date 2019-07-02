//订餐js
$(function(){
    $("#timepickerit").blur(function(){
        var xhr=createXhr();
        var time=$('#timepickerit').val();
        var data=$('#datepicker1').val();
        var url="/scoping/checktable?time='+time+'&data='+data;
        xhr.open("get",url,false);
        xhr.oneadystatechange=function(){
                if(xhr.readyState==4 && xhr.status==200){
                    var ordertable=JSON.parse(xhr.responseText)
                    html="";
                    for(i=0;i<ordertable.length;i++){
                            html+="<option>"+ordertable[i]+"</option>"
                    }
                    $(#tablenum).html(html);

                }
            }
            xhr.send(null);

    })
     $("#datepicker1").blur(function(){
        var xhr=createXhr();
        var time=$('#timepickerit').val();
        var data=$('#datepicker1').val();
        var url="/scoping/checktable?time='+time+'&data='+data;
        xhr.open("get",url,false);
        xhr.oneadystatechange=function(){
                if(xhr.readyState==4 && xhr.status==200){
                    var ordertable=JSON.parse(xhr.responseText)
                    html="";
                    for(i=0;i<ordertable.length;i++){
                            html+="<option>"+ordertable[i]+"</option>"
                    }
                    $(#tablenum).html(html);

                }
            }
            xhr.send(null);

    })
})