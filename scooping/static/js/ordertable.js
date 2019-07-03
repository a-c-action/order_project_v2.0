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
        $.post("/scoping/checktable",msg,
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
        $.post("/scoping/checktable",msg,
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
})