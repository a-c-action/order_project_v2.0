//订餐js
$(function(){
    //时间监控
    $("#timepickerit").blur(function(){
        var timetable=$('#timepickerit').val();
        var datatable=$('#datepicker1').val();
//        var url="/scoping/checktable?time='+time+'&data='+data;
        console.log(timetable,datatable)
        var msg={
            "timetable":timetable,
            "datatable":datatable
        }
        $.get("/scoping/checktable",msg,
        function(data){
               console.log(data,typeof(data));
               data=JSON.parse(data);
               console.log(data,typeof(data));
               var html="";
               for(i=0;i<data.length;i++){
                    html+="<option>"+data[i]+"</option>"
               }
               $("#tablenum").html(html)
               console.log(html);
        })

    })
    //日期监控
    $("#datepicker1").blur(function(){
        var timetable=$('#timepickerit').val();
        var datatable=$('#datepicker1').val();
//        var url="/scoping/checktable?time='+time+'&data='+data;
        console.log(timetable,datatable)
        var msg={
            "timetable":timetable,
            "datatable":datatable
        }
        $.get("/scoping/checktable",msg,
        function(data){
               console.log(data,typeof(data));
               data=JSON.parse(data);
               console.log(data,typeof(data));
               var html="";
               for(i=0;i<data.length;i++){
                    html+="<option>"+data[i]+"</option>"
               }
               $("#tablenum").html(html)
               console.log(html);
        })

    })
    //提交
    $("#tablesubmit").click(function(){
        var timetable=$('#timepickerit').val();
        if(timetable.length==0){
            alert("请选择时间段")
        }
        var datatable=$('#datepicker1').val();
        if(datatable.length==0){
            alert("请选择时间")
        }
        var personnum=$('#personnum').val();
        if(personnum.length==0){
            alert("请选择人数")
        }
        var tablenum=$('#tablenum').val();
        if(tablenum.length==0){
            alert("请选择桌号")
        }
        var phone=$('#phone').val();
        if(!(/^1[3|4|5|8][0-9]\d{4,8}$/.test(phone))){
            alert("请正确输入手机号")
        }
//        var url="/scoping/checktable?time='+time+'&data='+data;
        if(timetable.length!=0&&datatable.length!=0&&personnum.length!=0
        &&tablenum.length!=0&&(/^1[3|4|5|8][0-9]\d{4,8}$/.test(phone))){
            console.log(timetable,datatable)
            var msg={
                "timetable":timetable,
                "datatable":datatable,
                "personnum":personnum,
                "tablenum":tablenum,
                "phone":phone,
                "csrfmiddlewaretoken":$("[name='csrfmiddlewaretoken']").val()
            }
            $.post("/scoping/booktable",msg,
            function(data){
                    if(data=="请登录后操作"){
                        alert("请先登录再操作")
                        location.href="/userinfo/login"
                    }else{
                        alert("预定成功")
                        data=JSON.parse(data);

                    var html="";
                    for(i=0;i<data.length;i++){
                        html+="<option>"+data[i]+"</option>"
                    }
                    $("#tablenum").html(html)
                    }
                    })

            }

    })

})