$(function(){
    /*搜索栏提示功能*/
    $('#isFind').change(function(){
        var isFind = $('#isFind').val();
        $.get('/payment/search_server',{isFind:isFind},function(data){
            $('#showFind').html(data)
        });


    })

    /*确认付款*/






















})