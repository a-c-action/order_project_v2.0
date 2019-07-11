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
        var datatable=$('#datepicker1').val();
        var personnum=$('#personnum').val();
        var tablenum=$('#tablenum').val();
        var phone=$('#phone').val();
//        var url="/scoping/checktable?time='+time+'&data='+data;
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
                alert("预定成功")
                data=JSON.parse(data);

                var html="";
                for(i=0;i<data.length;i++){
                    html+="<option>"+data[i]+"</option>"
                }
                $("#tablenum").html(html)
                })
                console.log(data,typeof(data));

    })
})